

## General Nature

The Delver Archive ([DelvTechWiki](DelvTechWiki)'s name for it, the file format is not publicly named) is a resource container file. That is, it aggregates many logically separate resources into one file. A form of weak encryption is intended to protect some parts of the file from casual examination. 

The design is broadly similar to the resource fork familiar to all classic Mac programmers, although it almost totally lacks metadata - the Cythera executable is relied upon to know what the resources are and what should be done with them. The format uses four-byte integers for resource sizes and offsets throughout, so it can in principle store a maximum of four gigabytes of data. This would seem to be amply sufficient for its purposes.  

Why Cythera does not make more extensive use of the native Macintosh resource fork for this purpose is unclear. Delver was probably not intended to be readily portable to systems other than the Macintosh. It does not appear that it has any resources that exceed the limitations of that system, and there is no particular reason to think that the encryption system could not have been layered on top of a conventional resource fork. Certainly, most Mac-native games of the era used the resource fork extensively for the kinds of things Cythera does with the Delver Archive. According to Glenn Andreas, "The game data is stored in a custom format (the resource manager had too many limitations and was too slow)." 

Delver Archives are used by Cythera for the [Cythera Data](Cythera-Data) file itself, patches made with [Magpie](Magpie) (of which the [Pumpkin Patch](Pumpkin-Patch) is the only first-party example), and for Cythera's [saved game](Cythera-player-file)s. 

In 2014, [Bryce](Bryce) wrote [Narthex](Narthex), a python-based tool for examining Delver Archives. 


## Concepts

The file is segmented into numerous parts we call here "resources." A resource might represent something like an AI script or a sound effect. Resources can be retrieved from the archive by Cythera using a 16-bit (i.e. short int) number which we will term a "resource ID," or "resid", the existence of which is inferred by analogy with the Mac OS Resource Manager and [from other evidence](Cythera-Data-Subindex-0). 

The data within the archive is sometimes encrypted, but the Delver Archive format itself is technically encryption-agnostic - there does not appear to be anything marking particular resources as being encrypted. Presumably, the Cythera executable simply knows which resources, or more probably which types of resources, are always encrypted. Fortunately, the encryption status of almost all resources can be reliably inferred by examination of their information entropy. 

Some resources also appear to contain compressed data, particularly for graphics. This data has high information entropy, and it might be difficult to tell if it is encrypted or not besides being compressed. 


## File Format Details

The format uses big-endian (most significant byte first) as its byte order, like the classic Macintosh. All values should be assumed to use big-endian unless otherwise specified. All offsets are absolute, i.e. from the beginning of the file, unless otherwise specified. 


### Header

The header consists of the first 136 bytes of the file. All bytes are zero in all files examined so far, except for what is explained below.  

The header begins with a pascal-string (i.e. a one-byte integer for the length of the string, followed by one-byte ASCII characters - as opposed to a null-terminated C-string of indefinite length). This string gives the title of the game associated with the file, which is "Cythera: Fate of Alaric" for all known Cythera-related Delver Archives.  

The Mystery Integers: 

* At offset 0x3D, what is presumptively a long integer is stored, with the value 0x00000013 in all known Delver Archives. 
* At offset 0x41, the presumptive short integer 0x0002 in all known archives. 
* At offset 0x48, a byte, with value 0x02, in all known archives. 
* At offset 0x80, a presumptive long integer, value 0x00000080 in all known archives.   
* At offset 0x84, a presumptive long integer, value 0x00000800 in all known archives. 
It is possible that 0x84 represents the length of the master index, because that index is indeed 2048 bytes long. If that is the case, one might well expect 0x80's long integer to point to the beginning of that table... but it points to itself instead.  

The bytes from offset 0x01 - 0x040 can readily be explained by leaving space for the title pascal-string, but why the rest of the header has so much padding is unclear. Perhaps some of the zeros represent variables that happen to be zero, but there is no convenient way to know and it seems to be of no immediate practical importance. 

Narthex preserves the mystery integers when copying a Delver Archive, but as of this writing, the necessity of doing so has not been explored. 


### Master Index

The master index immediately follows the header, with its first record beginning at offset 0x88. (The structure itself might be said to begins at 0x80, if you interpret the fourth and fifth mystery integers above as being part of the master index, describing its offset and length.) 

Each master index record consists of two four-byte integers, which are the length and offset of a subindex page. There are 256 entries. If the length and offset are zero (which will be the case most of the time, as the index is sparely populated), then there is no corresponding subindex page. 

As an example, at offset 0x108 in the Cythera Data file, the record {0x0054C226 0x00000800} is stored, describing a subindex found at file offset 0x54C226 of length 2048. In all known archives, all subindex pages have length 2048, and Narthex always chooses this size of subindex page when it writes a Delver Archive. It is not known if Cythera would tolerate other sizes. Having more than 256 resources on a subindex page (corresponding to a subindex page length of 2048 / 0x800) would probably break the resource ID system, though. 


### Data

Immediately following the master index is the actual data of each resource. In the original Cythera data file, the resources are mostly packed tightly together, one after another, and usually - but not entirely - in order of their resource ID. There is no delimiter separating resources; the subindex pages are relied upon for determining which data goes with which resource ID. "Cythera Data" contains various data that is not pointed to by any subindex page entry, and appears to represent older versions of some resources. 

The formats of each kind of resource is discussed separately, on the pages of the various known Delver Archives: [Cythera Data](Cythera-Data), [Pumpkin Patch](Pumpkin-Patch), and [Cythera player file](Cythera-player-file). 

Narthex closely packs resources and does not copy any data that is not pointed to by an index (apart from the header and master index themselves, obviously). Cythera does not seem to mind using a data file that has been "optimized" by Narthex in this way. 


### Subindex Pages

A subindex page describes the individual resources. It consists of 8 byte resource records, each directly following the next (i.e. it is an array of these records.) The record consists of two four-byte integers. The first describes the offset in the file of the resource. The second describes the length of the resource. Note that the resource ID is implicit in the array index, and is not explicitly stored; this is an important difference with the data format of the Macintosh resource fork, if you are familiar with it. 


## Calculating Resource IDs

The resource ID is interchangeable with the index of resource in its subindex and the index of that subindex in the master index, according to these relationships: 



```
resource_id = 256*(master_index + 1) + sub_index;

master_index = resource_id/256 - 1

sub_index = resource & 0xFF /* Bitwise AND */

```

Resource IDs appear to be sixteen-bit quantities, having values in the range of 0 to 65,536 (0xFFFF). Thus, there is a limit of 256 resources per subindex, and 256 subindices. 


## Encryption

The argument could be made that since it is not marked in any way in the Delver Archive, the format is entirely agnostic to the format of the resources, including any encryption or compression that might be applied to them. However, the same form of encryption appears to be applied to all encrypted resources in "Cythera Data", and the parameters of that encryption are related to the resource IDs described above. Therefore, it is described here. 

Narthex performs encryption and decryption when it thinks it ought to. Since (not to belabor the point) the archive format does not mark if a resource is encrypted or not, Narthex is just guessing, but it turns out that it's really good at guessing, thanks to the ideas of some guy named Shannon. 

The encryption algorithm used is a simple [stream cipher](https://en.wikipedia.org/wiki/Stream_cipher), with a small enough keyspace to be very susceptible to a brute force attack. (Even on 1999 hardware, at least for a patient person.) That is not necessary, though, since a clear pattern emerges between the key used to encrypt a resource and its resource ID. (Or, originally and equivalently, to its master index and sub index, which are interchangeable with the resource ID.) That pattern is described below. 


### Key

The encryption key consists of three parameters, which we call key_0, m, and b. The key used for a resource is derived from the resource ID thusly:  



```
uint16 key_0, m, b;

key_0 = resource_id ^ (resource_id >> 8);
m = ((resource_id & 0x3F) << 2) | 1;
b = resource_id >> 6;
```

The purpose of bitwise ORing m with 1 is likely to avoid the case of m=0, which would cause degenerate behavior of the algorithm described below. 


### Algorithm

The algorithm essentially combines the output of a pseudorandom number generator with the cleartext to yield the ciphertext. It does this byte-by-byte and there is no padding or salts. This implies that a one-byte change to the cleartext at an offset _n_ will result in a one-byte change to the ciphertext at offset _n_, and that the ciphertext is exactly as long as the plaintext. For these and other reasons, such as the cryptographic insufficiency of extremely elementary PRNG used, this algorithm is not secure.  

In any case, even if a stronger algorithm not susceptible to trivial attacks had been used, it is not truly possible to secure a game's data file by encrypting it -  by necessity the encryption key must be provided to the user along with the algorithm for decrypting it, in order that the game can decrypt the data and play it. The best that can be hoped for is to make the key and algorithm inconvenient to retrieve by hiding them in the executable. 

The algorithm used is described below. key0, m, and b come from the code segment above. 



```
uint8 *cleartext, *ciphertext;
uint16 key = key_0;

for (int i = 0; i < data_length; ++i) {
    key = key*m + b;
    cleartext[i] = ciphertext[i] ^ key;
}
```

As the algorithm is completely symmetrical, exactly the same code can be employed to encrypt the cleartext. 
