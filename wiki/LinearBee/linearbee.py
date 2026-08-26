#!/usr/bin/env python
# Copyright 2015 Bryce Schroeder, www.bryce.pw, bryce.schroeder@gmail.com
# Version: 0.23
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
# Remember that the "Cythera Data" file is copyrighted by Ambrosia and/or
# Glenn Andreas, and publishing modified versions without their permission
# would violate that copyright. 
#
# "Cythera" and "Delver" are trademarks of either Glenn Andreas or 
# Ambrosia Software, Inc. 
#


# Cythera CLUT in python array format provided by Sfiera
CLUT = [
    'ffffff', '0000a8', '00a800', '00a8a8', 'a80000', 'a800a8', 'a85400', 'a8a8a8', '545454', '5454fc', '54fc54', '54fcfc', 'fc5454', 'fc54fc', 'fcfc54', 'fcfcfc',
    'fcfcfc', 'ececec', 'd8d8d8', 'c8c8c8', 'b8b8b8', 'a8a8a8', '989898', '848484', '747474', '646464', '545454', '444444', '343434', '202020', '101010', '080808',
    'fcf400', 'f8c800', 'f4a400', 'ec8000', 'e86000', 'e44000', 'e02000', 'dc0000', 'c80000', 'b40000', 'a00000', '8c0000', '7c0000', '680000', '540000', '400000',
    'fcfcfc', 'fcf4c0', 'fcec84', 'fce448', 'fcdc38', 'fcd024', 'fcc814', 'fcb800', 'e89000', 'd07000', 'bc5400', 'a83c00', '942800', '7c1800', '680800', '540000',
    'e8905c', 'dc7848', 'd0603c', 'c04c2c', 'b4381c', 'a82414', '9c1008', '900000', '800000', '6c0000', '5c0000', '480000', '380000', '240000', '100000', '000000',
    'f8fcd8', 'f4fcb8', 'e8fc9c', 'e0fc7c', 'd0fc5c', 'c4fc40', 'b4fc20', 'a0fc00', '90e400', '80cc00', '74b400', '609c00', '508400', '447000', '345800', '284000',
    'd8fcd8', 'bcfcb8', '9cfc9c', '80fc7c', '60fc5c', '40fc40', '20fc20', '00fc00', '00e400', '04cc00', '04b400', '049c00', '088400', '047000', '045800', '044000',
    'd8ecfc', 'b8dcfc', '9cd0fc', '7cbcfc', '5cacfc', '4094fc', '2084fc', '0070fc', '0068e4', '005ccc', '0058b4', '00509c', '004484', '003c70', '003058', '002440',
    'fcc87c', 'f0b870', 'e8a868', 'dc9c60', 'd09058', 'c88450', 'bc784c', 'b46c44', 'a0643c', '906034', '80542c', '6c4c24', '5c401c', '483818', '382c10', '28200c',
    'fcd8fc', 'fcb8fc', 'fc9cfc', 'fc7cfc', 'fc5cfc', 'fc40fc', 'fc20fc', 'fc00fc', 'e000e4', 'c800cc', 'b400b4', '9c009c', '840084', '6c0070', '580058', '400040',
    'fce8dc', 'fce0d0', 'fcd8c4', 'fcd4bc', 'fcccb0', 'fcc4a4', 'fcbc9c', 'fcb890', 'e8a47c', 'd0946c', 'bc8458', 'a8744c', '94643c', '805830', '684824', '543c1c',
    'fce8dc', 'f4c8b4', 'e8b090', 'e09470', 'd47850', 'cc6034', 'c44818', 'bc3400', 'a82800', '981c00', '881400', '781000', '680800', '580400', '480000', '380000',
    'fcf46c', 'f0f060', 'dce454', 'ccdc48', 'b8d040', 'a8c434', '94b82c', '84b024', '749820', '64841c', '506c14', '405810', '30400c', '202c08', '101404', '000000',
    'fcfcfc', 'e8e8f0', 'd4d4e8', 'c0c4dc', 'b4b4d0', 'a0a0c8', '9494bc', '8484b4', '74749c', '646484', '505470', '404058', '303044', '20202c', '101018', '000000',
    'fc0000', 'fc1c00', 'fc4000', 'fc6000', 'fc7c00', 'fc9800', 'fcbc00', 'fcdc00', '0010fc', '1028fc', '1c44fc', '2c5cfc', '3874fc', '4484fc', '5498fc', '60a8fc',
    'd02094', 'dc34c0', 'ec48e8', 'ec60fc', '704820', '84542c', '9c6038', 'b46c44', '24a800', '1cbc00', '10d000', '00e400', '000000', '000000', 'fcf4c0', '000000',
  ]
CLUT = [[int(c[:2],16), int(c[2:4],16), int(c[4:],16)] for c in CLUT]
Pal = []
for c in CLUT: Pal.extend(c)
from PIL import Image, ImageDraw
ZOOM=1
WIDTH=32
MINWIDTH=32# set it to 128 or something if you are tired of not being able to drag the window.
#im = Image.new("P", (max(WIDTH*ZOOM,MINWIDTH),ZOOM*WIDTH*TILES_PER_RESOURCE), 0x0d)
#im.putpalette(Pal)
#imd = ImageDraw.Draw(im)

from sys import argv
data = map(ord,open(argv[2]).read())
print "#"*78
#	
class DelverGraphicsDecompressor(object):
	def __init__(self, data,br=None,width_hint=None,height_hint=512,header=False):
		self.data=data
		self.x,self.y=0,0
		self.width=width_hint
		self.height = height_hint
		self.pixels = {}
		self.ops_decoded = 0
		self.pixels_flat = []
		self.ftable = []
		self.ops_seen = {}
		self.visual_width = self.width
		if header:
			self.flags = data[1]&0x03
			if not width_hint:
				self.width = (data[0]<<8) | (data[1]&0xFC)
				self.visual_width = self.width
				self.height = (data[2]<<8) | data[3]
				if self.flags: 
					self.width += 4
					self.visual_width += self.flags
			self.data = data[4:]
		self.img = Image.new("P", (max(self.visual_width*ZOOM,MINWIDTH),ZOOM*self.height), 0x0d)
		print "IMAGE SIZE: %d*%d"%(self.width,self.height)
		self.img.putpalette(Pal)
		self.imd = ImageDraw.Draw(self.img)
		
		self.decompress(br)
	def putpixel(self, px, mode=True):
		try:
			if mode:
				self.imd.rectangle ((self.x*ZOOM,self.y*ZOOM,self.x*ZOOM+ZOOM,self.y*ZOOM+ZOOM), px)
			else:
				self.imd.rectangle ((self.x*ZOOM,self.y*ZOOM,self.x*ZOOM+ZOOM,self.y*ZOOM+ZOOM), self.ops_decoded&0xFF)
		except:
			print " --- CURSOR OUT OF BOUNDS: %d,%d --- "%(self.x,self.y)
		self.pixels[self.x,self.y] = px
		self.pixels_flat.append(px)
		self.x += 1
		if self.x >= self.width:
			self.x = 0
			self.y += 1
	def sl(self,i,n=1):
		d = self.data
		print "%02d,%03d %03d@0x%04X:"%(self.x,self.y,self.ops_decoded,i),
		print ' '.join(["%02X"%b for b in d[i:i+n]])
	def op_er(self, i, d):
		self.sl(i)
                print "        Error: unrecognized opcode."
		i += 1
		return i
	def op_Fx(self, i,d): # Special operations?
		if d[i] == 0xFF:
			self.sl(i)
			print "        TERM ; Orderly termination with cursor at: (%d,%d)"%(self.x,self.y)
			i += 1
		elif d[i] == 0xF0:
			self.sl(i,3)
			run_length = d[i+1] + 3
			run_color = d[i+2]
			print "        RUN %d, [%02X] ; Long run"%(run_length, run_color)
			self.color_run(run_length,run_color)
			i += 3
		else:
			self.sl(i)
                	print "        Error: unrecognized 0xFx opcode."
			i += 1
		return i
	def op_0x(self, i,d): # This is another copying opcode, but it didn't unify with 80x...
		lits_follow = (d[i+1]&0x18)>>3
		perverse_bits = (d[i+1]&0xE0)>>5
		self.sl(i,2+lits_follow)
		if lits_follow: self.literals(i+2, lits_follow)
		copy_length = (d[i+1]&0x07) + 3
		copy_index = -(d[i]+1+(perverse_bits<<7))
		print "        COPY %d, %d ; Short copy perverse bits=%02X"%(copy_length, copy_index,perverse_bits)
		self.copy_pixels(copy_length, copy_index)
		i += 2
		i += lits_follow
		return i
	def op_8x(self, i,d):
		lits_follow = d[i+2]&0x03
		horrid_bits = (d[i+2]&0xFC)>>2
		self.sl(i,3+lits_follow)
		if lits_follow: self.literals(i+3, lits_follow)
		perverse_bits = (d[i+1]&0xE0)>>5
		copy_index = -((d[i]&0x7F) + 1 + (perverse_bits<<6) + (horrid_bits<<9))
		copy_length = (d[i+1]&0x1F)+3
		print "        COPY %d, %d ; Long copy"%(copy_length, copy_index)
		self.copy_pixels(copy_length,copy_index)
		i += lits_follow
		i += 3
		return i
	#def op_9x(self, i,d): return i+1
	def op_Dx(self, i,d): # Don't know what these do yet... this may not be accurate.
		self.sl(i,2)
		print "        UNKNOWN %d"%d[i+1]
		variant = d[i]&0x0F
		if variant == 2:
			i += 3
		else:
			i += 2
		return i
	def op_Cx(self, i,d):
		lennyb = d[i]&0x0F
		data_length = (lennyb+1)*4
		#data_length = lennyb - 6 if lennyb > 0x0A else (lennyb+1)*4
		#if lennyb > 0x0A: print "lennyb > 0x0A"
		self.sl(i,1+data_length)
		self.literals(i+1,data_length)
		i += 1
		i += data_length
		return i
	def op_Ex(self, i,d):
		self.sl(i,2)
		run_length = (d[i]&0x0F) + 3
		run_color = d[i+1]
		print "        RUN %d, [%02X] ; Short run"%(run_length,run_color)
		self.color_run(run_length,run_color)
		i += 2
		return i
	def copy_pixels(self, copy_length, copy_index):
		cdata = self.pixels_flat[copy_index:]
		
		for n in xrange(copy_length):
			self.putpixel(cdata[n%len(cdata)])
	def literals(self, i, n):
		lits = self.data[i:i+n]
		for lit in lits: self.putpixel(lit)
		print "        DRAW", ', '.join(["[%02X]"%b for b in lits])
	def color_run(self,run_length,run_color):
		for _ in xrange(run_length): self.putpixel(run_color)

	def decompress(self, break_lim=None):
		i = 0
		d = self.data
		self.ftable = [
			self.op_0x, #
			self.op_0x, #
			self.op_0x,
			self.op_0x, #
			self.op_0x,
			self.op_0x,
			self.op_0x, #
			self.op_0x,
			self.op_8x, #
			self.op_8x, #
			self.op_8x, #
			self.op_8x, #
			self.op_Cx, #
			self.op_Dx, 
			self.op_Ex, #
			self.op_Fx  #
		]		
		
		while i < len(d) and (break_lim is None or break_lim >= self.ops_decoded):
			opcode = d[i]
			#self.ops_seen[opcode] = True
			i = self.ftable[(d[i]&0xF0)>>4](i,d)
			self.ops_decoded += 1
			
# uncomment if you want to support breaking at an opcode (useful for debugging)
#br = int(argv[3]) if len(argv) > 3 else None
br=None
#dgc = DelverGraphicsDecompressor(data)#,br)

if argv[1] == 'sprite':
	dgc = DelverGraphicsDecompressor(data, br=br,  width_hint=32, height_hint=512)
elif argv[1] == 'portrait':
	dgc = DelverGraphicsDecompressor(data, br=br,  width_hint=64, height_hint=64)
elif argv[1] == 'landscape':
	dgc = DelverGraphicsDecompressor(data, br=br, width_hint=288, height_hint=32)
elif argv[1] == 'sized':
	dgc = DelverGraphicsDecompressor(data, br=br,  width_hint=None,header=True)
elif argv[1] == 'manual':
	dgc = DelverGraphicsDecompressor(data, br=br,  width_hint=int(argv[4]), height_hint=int(argv[5]), header=int(argv[6]))

if len(argv)>3: 
	dgc.img.save(argv[3]) # Uncomment if you want transparency (messes up color map),transparency=0x00
else:
	dgc.img.show()
#k = dgc.ops_seen.keys()
#k.sort()
#for v in k: print "%02X"%v,
#print "\nFLAGS", dgc.flags
