#!/usr/bin/env python
# Copyright 2014-2015 Bryce Schroeder, www.bryce.pw, bryce.schroeder@gmail.com
# Version: 0.20
# 
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Please do not make trouble for me or the Technical Documentation Project by
# using this software to create versions of the "Cythera Data" file which 
# have bypassed registration checks.
# Also, remember that the "Cythera Data" file is copyrighted by Ambrosia and
# /or Glenn Andreas, and publishing modified versions without their permission
# would violate that copyright. 
#
# "Cythera" and "Delver" are trademarks of either Glenn Andreas or 
# Ambrosia Software, Inc. 
#
# Operation:
#  Print file info and list of subindices:
# ./narthex.py "Cythera Data" 
#
#  Print out a list of valid resources in a subindex (e.g. 20):
# ./narthex.py "Cythera Data" 20
#
#  Print out a particular resource:
# ./narthex.py "Cythera Data" 1427
#
#  Force to print the raw data (hokey, will be replaced by better interface)
# ./narthex.py "Cythera Data" -1427
#  Useful in cases of incorrect decryption.
#
# Narthex also works on the Pumpkin Patch, and other Cythera patches
# designed to be applied with Magpie.
# ./narthex.py "Pumpkin Patch"
#
#  Dump the data file to a directory for examination in some other
#  program of your choice:
# ./narthex.py "Cythera Data" yoursubdirectory/
#
#  You can read resources from a directory you dumped the file to, should you
#  wish, although it will probably be faster just to use the file. E.g:
# ./narthex.py yoursubdirectory/ 0801
# 
# In a future version, you will be able to do this:
# ./narthex.py yoursubdirectory/ "Modified Cythera Data"
# to pack the directory back into a file, presumably after having
# modified it in some way. This feature isn't available yet, though, sorry.
#
# It might occur to you do this for some reason:
# ./narthex.py yoursubdirectory/ acopythereof/
# This will indeed copy the data file, but it will purge all information
# about the correct encryption state of the segments in acopythereof/
# and if you later attempt to make an archive file from acopythereof/,
# it will not work, because everything will be stored as cleartext and
# cythera will always assume certain of the resources are encrypted,
# and scramble them inappropriately. I will probably change/fix this 
# behavior at some point; as it is, it's working as designed, but the
# design wasn't the best.

# FUTURE IDEAS:
# create (hopefully) Magpie-compatible patches thusly:
# ./narthex.py -diff "Cythera Data" "Modified Data" "PatchName"
#
# If you want to set the description of your patch visible in Magpie,
# Add a data item "patch_description" to the metadata.py file in the
# modified data. (Which, in that case, will have to be in a directory
# rather than in a Delver Archive as shown here.
#
# Magpie is a PPC only application, and if you're running cythera on
# a 68k mac or an emulator thereof, it won't run. So narthex has been
# provided with patch-applying functionality.
# ./narthex.py -patch "Cythera Data" "Newly Created Patched Data" "PatchName"

import sys, os
import struct       # Because ASCII was invented after Cythera :D

import numpy        # For array-wise math to speed things up
                    # We use it for entropy calculation - don't ask us to
                    # guess if things are encrypted and we don't need it.

import glob         # We need this only for packing a directory
                    # don't ask us to open a directory representing a
                    # delver data file and we won't need it.

class _BinaryFileManipulator(object):
    """Private class for reading/writing binaries.
       Probably already debuggedish."""
    S_uint32 = struct.Struct('>L')
    S_uint8 = struct.Struct('B')
    S_uint16 = struct.Struct('>H')
    # I admit that not having separate read and
    # write methods here wasn't my best idea
    def uint8(self,addr,data=None,advance=False):
        if data is None:
            return self.S_uint8.unpack(self.data[addr])[0]
        radr = self.savefile.tell()
        if not addr is None: self.savefile.seek(addr)
        self.savefile.write(self.S_uint8.pack(data))
        if not advance: self.savefile.seek(radr)
    def uint16(self,addr,data=None,advance=False):
        if data is None:
            return self.S_uint16.unpack(self.data[addr:addr+2])[0]
        radr = self.savefile.tell()
        if not addr is None: self.savefile.seek(addr)
        self.savefile.write(self.S_uint16.pack(data))
        if not advance: self.savefile.seek(radr)
    def uint32(self,addr,data=None,advance=False):
        if data is None:
            return self.S_uint32.unpack(self.data[addr:addr+4])[0]
        radr = self.savefile.tell()
        if not addr is None: self.savefile.seek(addr)
        self.savefile.write(self.S_uint32.pack(data))
        if not advance: self.savefile.seek(radr)

class DelverArchiveResourceIDException(Exception):
    """Raised when a resource ID is invalid because it is outside the
       allowable range of a short integer (0-0xFFFF) or because it 
       does not point to a loaded resource."""
    pass

class DelverArchiveException(Exception):
    """Raised for general problems related to the archive."""
    pass

class DelverArchive(_BinaryFileManipulator):
    """This object handles reading and writing from a Delver Archive,
       and access to the archived files. It can be a real archive or
       a directory with folders structured in a certain way documented
       in DelverArchive.unpack()."""

    # Constants.
    _MASTER_INDEX_START = 0x0088
    _MASTER_INDEX_END =   0x0880
    _ECT = -0.01 # Encryption guess threshold: if decryption removes more than
    # this much entropy, assume it's encrypted. 

    # All items are loaded immediately from
    # the file; no provision is made for reading or writing piecewise,
    # so its time performance is good but its memory performance is bad
    # (though Cythera Data is only a few megs, so that isn't important
    # anymore.)

    def __init__(self):
        self.master_index = {}
        self.loaded_from = None
        self.title = 'Untitled'
        self.encryption_beliefs = {}
        self.encryption_commands = {}
    ####################### API for loading and saving. ######################
    def load(self, path, log=None):
        """Open a Delver Archive on the disk and load it into this
           object for use. All the data will be loaded and ready immediately.
        """

        #if self.loaded_from:
        #    raise DelverArchiveException("Archive already loaded from \"%s\"",
        #        self.loaded_from)

        if not os.path.isfile(path):
            raise IOError("Is not a file: '%s'"%path)

        inf = open(path, 'rb')

        self.loaded_from = "file '%s'"%path

        # slurp the whole file into memory in one go. Efficiency!
        self.data = inf.read()

        # Interpret the header such as we can.
        title_length = self.uint8(0)
        self.title = self.data[1:title_length+1]
        if log: print>>log, "TITLE:", self.title

        # I don't know what any of these things are. But we must
        # preserve them on the assumption that Cythera does.
        self.unknown_1l = self.uint32(0x3D)
        if log: print>>log, "Unknown 1l:", self.unknown_1l
        self.unknown_2s = self.uint16(0x41)
        if log: print>>log, "Unknown 2s:", self.unknown_2s
        self.unknown_3b = self.uint8(0x48)
        if log: print>>log, "Unknown 3b:", self.unknown_3b
        self.unknown_4l = self.uint32(0x80)
        if log: print>>log, "Unknown 4l:", self.unknown_4l
        self.unknown_5s = self.uint32(0x84)
        if log: print>>log, "Unknown 5s:", self.unknown_5s

        print "Unknown Integers %08X %04X %02X %08X %08X"%(self.unknown_1l,self.unknown_2s,self.unknown_3b,self.unknown_4l,self.unknown_5s)
        # Table entries
        i = self._MASTER_INDEX_START; j = 0
        while i < self._MASTER_INDEX_END:
            if log: print>>log, "\tReading index %3d,0x%08X: 0x%08X,%d"%(
                j,i,self.uint32(i),self.uint32(i+4))
            start = self.uint32(i)
            if start: 
                self.master_index[j] = self._Subindex(
                    self.uint32(i),    # Start
                    self.uint32(i+4),  # Length
                    j,                # Index - need it for resource ids
                    self.data)
            j += 1; i += 8
        self.master_index_table_size = j


    def pack(self, path):
        """Load the contents of a directory with a specific structure
           into this reader.
           (Such a directory is created by DelverArchive.unpack())
        """

        if self.loaded_from:
            raise DelverArchiveException("Archive already loaded from \"%s\"",
                self.from_loaded)

        if not os.path.isdir(path):
            raise IOError("Is not a directory: '%s'"%path)
        ind = path if path[-1] == '/' else path+'/'

        self.loaded_from = "directory '%s'"%path

        # It goes without saying that this should only be used on trusted
        # files. Did not use json to avoid dependence on recent version of 
        # python (relatively recent); did not use pickle so as to keep human 
        # readable format. But switch to json if this has to be untrusted.
        meta = eval(open(ind+'metadata.py','r').read())
        self.unknown_1l = meta['unknown_1l']
        self.unknown_2s = meta['unknown_2s']
        self.unknown_3b = meta['unknown_3b']
        self.unknown_4l = meta['unknown_4l']
        self.unknown_5s = meta['unknown_5s']
        self.title = meta['title']
        self.data = ''
        # So, everything in the directory should be in cleartext; if we
        # were to blindly use the encryption_beliefs array as our own it
        # would be wrong. But we do need to keep the information.
        self.encryption_commands = meta['encryption_beliefs']
        self.encryption_beliefs = {r:False for r in self.encryption_commands}


        for i in xrange(255): # not a typo, 255 is illegal - it would correspond
                              # to resource ID's begining at 0x10000.
            self.master_index[i] = self._Subindex(None,None,i,self.data)

        for respath in glob.glob(ind+"????.bin"): #gobble not too promiscuously
            resid = int(respath[-8:-4],16)
            mi,ri = self.indices(resid)
            f = open(respath, 'rb')
            self.put(resid, f.read())
            f.close()


    def save(self, path):
        """Save the contents of this reader onto the disk in Delver Archive 
           format."""
        outf = open(path, 'wb')
        self.savefile = outf # For uint8, etc.
        
        outf.write('\x00'*0x880)
        
        # Write the title
        outf.seek(0)
        outf.write(chr(len(self.title)))
        outf.write(self.title)



        # Write the unknowns (which appear to be the same in Magpie
        # patches as well.
        self.uint32(0x3D, self.unknown_1l)
        self.uint16(0x41, self.unknown_2s)
        self.uint8(0x48, self.unknown_3b)
        self.uint32(0x80, self.unknown_4l)
        self.uint32(0x84, self.unknown_5s) #... this is really not a short

        # Our master table will come next, but we don't know what to put 
        # here yet, which is why we wrote so many zeros.
        self.save_positions = {}
        # Instead we proceed with writing the data.
        outf.seek(0x880)
        sorted_master_index = self.master_index.items()
        sorted_master_index.sort()
        for mi, sidx in sorted_master_index:
            resources_sorted = sidx.resources.items()
            if not resources_sorted: continue
            resources_sorted.sort()
            for ri, res in resources_sorted:
                if res[1] is 0: continue # this has gotten so messed up
                if res[0] is None and not res[1]: continue
                # We use get so that if it's been modified in memory,
                # we will write out the modified version.
                resid = self.resid(mi,ri)
                new_offset = outf.tell()
                resdata = self.get(resid)
                if self.encryption_commands.get(resid, False): # CHECK
                    resdata = self.encrypt(resdata, resid)
                outf.write(resdata)
                self.save_positions[resid] = (
                    new_offset, outf.tell()-new_offset)

        self.indices_of_subindices = {}
        # Now we can write our subindices. Exciting.
        for mi, sidx in sorted_master_index:
            startoff = outf.tell()
            # .. in retrospect I should have just used an array
            resources_sorted = sidx.resources.items()
            if not resources_sorted: continue
            resources_sorted.sort()
            empty = True
            for si,res in resources_sorted:
                if res[1]:
                    empty = False
                    break
            if empty: continue
            for si,res in resources_sorted:
                noff, nlen = self.save_positions.get(self.resid(mi,si),
                    (0,0))
                self.uint32(None,noff,advance=True)
                self.uint32(None,nlen,advance=True)

            self.indices_of_subindices[mi]=(startoff,outf.tell()-startoff)

        # NOW we can write our master index
        outf.seek(self._MASTER_INDEX_START)
        for i in xrange(256):
            offs,ilen = self.indices_of_subindices.get(i,(0,0))
            self.uint32(None,offs,advance=True)
            self.uint32(None,ilen,advance=True)

        outf.close()


    
    def unpack(self, path, decrypt=True):
        """Save the contents of this reader onto the disk as individual data 
           files."""
        if not os.path.isdir(path):
            raise IOError("Is not a directory: '%s'"%path)
        outd = path if path[-1] == '/' else path+'/'


        if decrypt: self.guess_if_encrypted()

        metafile = open(outd+'metadata.py','w')
        meta = {
            'title': self.title,
            'unknown_1l': self.unknown_1l,
            'unknown_2s': self.unknown_2s,
            "unknown_3b": self.unknown_3b,
            'unknown_4l': self.unknown_4l,
            'unknown_5s': self.unknown_5s,
            'encryption_beliefs': self.encryption_beliefs,

        }
        metafile.write(repr(meta)+'\n')
        metafile.close()

        for mi,sidx in self.master_index.items():
            if not sidx.length: continue
            for ri,res in sidx.resources.items():
                if not res[1]: continue
                resid = self.resid(mi,ri)
                f = open(outd+"%04X.bin"%resid, 'wb')
                f.write(self.get(resid))
                f.close()

    
    ########################## API for data access. #########################

    # Thought of calling this 'fetch' but it might be ill-Omened. Pun totally
    # intended there.
    CLEAR = 0
    ENCRYPTED = 1
    SMART = 2
    def get(self, resid, decryption=SMART,probe=False):
        """Retrieve an item from the archive by its numerical ID.
           A bytestring is returned. Optionally decrypts it if it thinks
           it is encrypted. If probe is set, it returns an empty string
           instead of raising an exception if pointed at a valid, but
           as it happens empty, resource."""
        self._resid_validation_check(resid)

        mi,si = self.indices(resid)
        subindex = self.master_index[mi]
        data = subindex.get(si,probe=probe)
        if decryption== self.ENCRYPTED or (decryption==self.SMART 
                and self._is_encrypted(resid)):
            return self.decrypt(data, resid) # yup, the resource id is the key
        elif decryption == self.CLEAR or decryption == self.SMART:
            return data
        else:
            raise DelverArchiveException("What are you smoking? %d"%decryption)
    def tell_offset(self, resid):
        self._resid_validation_check(resid)
        mi,si = self.indices(resid)
        subi = self.master_index[mi]
        return subi.tell_offset(si)

    def __getitem__(self, resid):
        """Syntactic sugar for DelverArchive.get(); allows you to use
           the DelverArchive as if it were a dictionary."""
        return self.get(resid,decryption=self.SMART)

    def put(self, resid, data):
        """Add a resource to the archive, possibly creating it and 
           if necessary its subindex page."""
        self._resid_validation_check(resid)
        
        mi,ri = self.indices(resid)

        self.master_index[mi].put(ri, data)

    def __setitem__(self, resid, data):
        """Syntactic sugar for DelverArchive.put(). Works basically
           like a dictionary."""
        return self.put(resid,data)

    #########################

    ################   Handling resource ids ############################
    def indices(self, resid):
        """Returns the master index and subindex positions for a resource,
           given its resource id."""
        self._resid_validation_check(resid)
        return self._master_index(resid),self._subindex(resid)

    def _master_index(self,resid):
        return ((resid&0xFF00)>>8)-1
    
    def _subindex(self,resid):
        return resid&0xFF

    def resid(self, master_index, subindex):
        v = 256*(1+master_index) + subindex
        self._resid_validation_check(v)
        return v

    ################ Stuff related to scrambling / encryption ###############
    # The big issue confronting us is that the Delver archive does not mark 
    # which segments are encrypted - Cythera knows, and it decrypts them if
    # appropriate, but the information is not contained in the data file. 
    # Indeed, it's remarkably spartan as an archive format, just consisting of
    # offsets and lengths. Even the resource IDs are implicit in the index
    # positions of the resource. The best we can do is guess about which 
    # segments are encrypted, unfortunately. Fortunately, we do have a 
    # statistical means of guessing, so the computer can do it for us.
    # In practice this appears to work fine so far.
    def declare_encryption(self, resid, is_encrypted=True):
        """Tells this code that a certain resource is encrypted (or not).
           It will trust you regardless of guess_if_encrypted's result,
           assuming you have some special knowledge about it, such as one
           might obtain, say, from tracing the decryption code on one's
           debugger while Cythera is loading, if one wished to do such a
           thing.
           
           resid may also be a list of resource IDs."""
        if type(resid) is not list: resid = [resid]
        for r in resid: 
            self._resid_validation_check(r)
            self.encryption_beliefs[r] = is_encrypted

    def command_encryption(self, resid, do_encrypt=True):
        """Tells the program to encrypt a certain segment when saving
           to an archive file. This is really only for if you have a
           directory loaded and are adding a new segment manually."""
        self.encryption_commands[resid] = do_encrypt

    def encryption_is_mandated(self, resid):
        """"Tells the caller if a resource is slated to be encrypted
            when writing to an archive file."""
        return self.encryption_commands.get(resid, False)
           

    def _is_encrypted(self, resid):
        """Gives the best information available about the encryption status
           of a resource, from an encryption declaration if available, 
           otherwise from .guess_if_encrypted. This is a private method.
           """
        self._resid_validation_check(resid)
        return self.encryption_beliefs.get(resid, False)

    def guess_encryption(self, resid):
        """Guess if one resource is encrypted. Caches the result for
           use of .get(), etc."""
        data = self.get(resid, decryption=self.CLEAR)
        guess = self.entropy(data) - self.entropy(
                    self.decrypt(data,resid))

        mi,si = self.indices(resid)
        self.encryption_beliefs[self.resid(mi,si)] = guess > self._ECT
        return guess

    def guess_if_encrypted(self, log=None, force=False):
        """Tells the code to guess which resources are encrypted.
           This guess can be used when unpacking files.
           If it is wrong, the archive can still be repacked successfully. Some
           unknown portion of the unpacked files should be assumed to be
           erroneously encrypted, though. User beware.
           
           This operation takes some time since it has to presumptively
           decrypt each and every resource and then compare the original with
           the result to see which is more random-looking."""
        for mi,subindex in self.master_index.items():
            for si,resource in subindex.resources.items():
                resid = self.resid(mi,si)
                if self.encryption_beliefs.has_key(resid) and not force: continue
                data = self.get(resid, decryption=self.CLEAR,probe=True)
                if not data: continue
                guess = self.entropy(data) - self.entropy(
                    self.decrypt(data,resid))
                if log: print >> log,"Encryption guess", resid,mi,si,guess
                self.encryption_beliefs[self.resid(mi,si)] = guess > self._ECT
    def entropy(self, data):
        """Return a statistical measure of the entropy of the given data.
           Encrypted (or compressed) data has high entropy. Note that this is
           not infallable and if the cleartext has very high entropy, e.g. in
           the case of compressed data, it may not be able to distinguish
           a successful decryption, at least in principle."""
        counts = numpy.zeros(256)
        for c in data: counts[ord(c)] += 1
        counts -= len(data)/256.0
        counts *= counts
        return 1 - ((counts.sum()**0.5)/len(data))

    def decrypt(self, data, prokey):
        """Decrypt the data provided with the given pro-key. The prokey is
           used to generate the seed value and parameters for the 
           pseudorandom number generator that is used to create the key."""
        self._resid_validation_check(prokey)

	#if "odd helmet" in data: print "Warning, bad decryption decision %04X"%prokey

        # The stuff in that inner loop might be the real magic, but 
        # this took annoyingly longer to figure out :/
        key = prokey^(prokey>>8)
        m = ((prokey & 0x3F) << 2) + 1
        b = (prokey >> 6)

        # This is an elementary pseudo random number generator. It is
        # not very cryptographically secure and should not be used for
        # protecting data.
        
        rv = []
        i = 0
        for char in data:
            key = (key*m + b) & 0xFFFF
            rv.append(chr((key^ord(char))&0xFF))
            i += 1

        return ''.join(rv)

    def encrypt(self, data, prokey):
        """Encrypt the data provided with the given pro-key. See .decrypt()
           for documentation."""
        return self.decrypt(data, prokey) # it's symmetric.

    ########################## Misc. Behaviors ##############################
    def __len__(self):
        """Returns the number of actual resources contained in the archive."""
        return sum((len(subindex) for subindex in self.master_index.values()))

    def __str__(self):
        """Summarize the file as a string."""
        return "<DelverArchive \"%s\" with %d resources%s>"%(
            self.title,
            len(self), 
            " loaded from "+self.loaded_from if self.loaded_from else (
                ", unloaded."))
    
                   

    ###################### PRIVATE / HELPER METHODS #########################
    # Use at your own risk, may change freely between versions.             #
    #########################################################################
    def _resid_validation_check(self, resid):
        if resid < 0 or resid > 0xFFFF:
            raise DelverArchiveResourceIDException(
                "Resource ID 0x%04X is not valid."%resid)
    
    def show_res(self, index):
        idx = self.master_index[index]
        print " ---- SUBINDEX %d ---- "%index
        ird = idx._real_id()
        ird.sort()
        for j,length in ird:
            print "Index %d, ID %04X"%(j,self.resid(index,j)),  
            print "Length:",
            print length if type(length) is int else len(length), "bytes"

    def show_subi(self,log=sys.stdout):
        iditems = self.master_index.items()
        iditems.sort()
        for mi,idx in iditems: 
            if idx.length:
                print "Subindex %3d:"%mi,
                ird = idx._real_id()
                print "found %5d"%len(ird), "resource%s"%('' if len(ird) == 1 else 's')
            else:
                continue
                #print "empty index."


    class _Subindex(_BinaryFileManipulator):
        """Holds an entry for one subindex. The delver archive has
           lots of these index pages; they're put at the end of the file
           although in principle I guess they could go in another place since
           the master index says where they are and how long they are.
           
           start=None: deferred mode start (offset, length) to be
           calculated later."""
        def __init__(self, start, length, index, data):

            self.index = index
            self.offset = start
            self.length = length
            self.data = data
            if start is None:
                self.length = 0
                self.resources = {j:(None,'') for j in xrange(256)}
                return

            self.resources = {}
            i = self.offset; j = 0
            end = self.offset + self.length
            while i < end:
                # offset, length
                length = self.uint32(i+4)
                self.resources[j] = (self.uint32(i), length)
                i += 8; j += 1
        def put(self,subindex_key,data):
            # This dirties the resource, of course
            self.length += 8
            self.resources[subindex_key] = (None,data)
        UNSAVED = -1
        def tell_offset(self,subindex_key):
            if not self.resources.has_key(subindex_key):
                raise DelverArchiveResourceIDException(
                    "Could not find resource %d,%d"%(self.index,subindex_key))
            offset,length = self.resources[subindex_key]
            return -1 if offset is None else offset

        def get(self,subindex_key,probe=False):
            if not self.resources.has_key(subindex_key):
                raise DelverArchiveResourceIDException(
                    "Could not find resource %d,%d"%(self.index,subindex_key))
            offset, length = self.resources[subindex_key]
            if not length and not probe:
                raise DelverArchiveResourceIDException(
                    "That resource %d,%d is empty."%(
                        self.index,subindex_key))
            if offset is not None:
                return self.data[offset:offset+length]
            else: # In this case it has not been written to the disk.
                return length if length else ''
        def __setitem__(self, key, value):
            return self.put(key,value)
        def __getitem__(self, key):
            return self.get(key)
        def __len__(self):
            return sum((bool(r[1][1]) for r in self.resources.items()))
        def _real_id(self, log=sys.stdout):
            real_ones = []
            for j,r in self.resources.items():
                if r[1]: real_ones.append((j,r[1]))
            return real_ones



# This could be much, much fancier.
import string
if __name__ == '__main__':


    if len(sys.argv) < 2:
        print >> sys.stderr, "Specify a delver archive on the command line."
        sys.exit(-1)

   

    d = DelverArchive()
    if os.path.isdir(sys.argv[1]):
        d.pack(sys.argv[1])
    else:
        d.load(sys.argv[1])#,log=sys.stderr)

    # There is a degenerate case of the encryption algorithm
    # for resources in subindex 239. This tells it they're not
    # really encrypted.
    d.declare_encryption([0xF004, 0xF00C, 0xF014], False)
    d.declare_encryption([0x8000|x for x in xrange(255)], False)
 
    #d.save("Saveout-mod")


    if len(sys.argv) < 3:
        print d
        print "List of valid subindices:"
        d.show_subi()
        sys.exit(0)

    if len(sys.argv[2]) < 4:
       d.show_res(int(sys.argv[2]))
       sys.exit(0)

    if sys.argv[2][-1] == '/':
        print "Unpacking; this may take a while."
    	d.guess_if_encrypted() # It is very important to do this before saving.
        d.unpack(sys.argv[2])
        sys.exit(0)

    doguess = True
    resource = int(sys.argv[2],16)
    if resource < 0: 
        resource *= -1
        doguess = False

    mi,ri = d.indices(resource)
    print "Major index:", mi, "Minor index", ri

    if doguess:
        guess =d.guess_encryption(resource)
        print "Encryption guess:", guess, "(Probably encrypted)" if guess > -0.01 else "(Probably clear)"

   
    
    result = d[resource]

    print "Length:", len(result), "bytes"
    print "Offset in file: 0x%06X"%d.tell_offset(resource)
    

    okay_char = {c: ' ' if c in string.whitespace else c for c in string.printable}
    print " --- DATA AS TEXT ---",
    for n,c in enumerate(result):
        if not n%32: print "\n%04X: "%n,
        sys.stdout.write(okay_char.get(c,'.'))


    print "\n --- DATA AS BINARY --- ",
    for n,c in enumerate(result):
        if not n%16: print "\n%04X:"%n,
        print "%02X"%ord(c),


  
