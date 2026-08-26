#!/usr/bin/env python
# Encoder/Compressor for Delver Sprite Graphics.
# Usage:
# ./dsencoder.py source.png sprite DEST.bin
#
# Make sure that the source image has the correct indexed color map, or 
# it won't work.
#
# Copyright 2015 Bryce Schroeder, www.bryce.pw, bryce.schroeder@gmail.com
# Version: 0.10
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
import struct, sys, os
from PIL import Image, ImageDraw

class DelverGraphicsEncoder(object):
	S_uint8 = struct.Struct('B')
	S_uint16 = struct.Struct('>H')
	def w_u8(self, uint8):
		assert 0 <= uint8 <= 0xFF
		self.savefile.write(self.S_uint8.pack(uint8))
	def w_u16(self,uint16):
		assert 0 <= uint16 <= 0xFFFF
		self.savefile.write(self.S_uint16.pack(uint16))

	def __init__(self, image,graphic_type='sized'):
		self.graphic_type = graphic_type
		self.image = image

		self.write_header = False
		if graphic_type == 'sized':
			self.write_header = True
			self.width,self.height = image.size
		elif graphic_type == 'portrait':
			self.width,self.height = 64,64
		elif graphic_type == 'sprite':
			self.width,self.height = 32,512
		elif graphic_type == 'landscape':
			self.width,self.height = 288,32
		assert image.size == (self.width,self.height)
	def save(self, filelike):
		self.savefile = filelike
		if self.write_header:
			self.w_u16(self.width)
			self.w_u16(self.height)
		# Don't bother with compression yet.
		assert not (self.width*self.height)%4

		i = 0
		d = self.image.getdata()
		while i < len(d):
			remains = (len(d)-i)
			packet = min(remains/4,0x10)
			self.w_u8(0xC0|(packet-1))
			j = 0
			while j < packet*4:
				self.w_u8(d[i+j])
				j += 1
			i += packet*4
		self.w_u8(0xFF)
		

img = Image.open(sys.argv[1])
dcg = DelverGraphicsEncoder(img,sys.argv[2])
outf = open(sys.argv[3],'wb')
dcg.save(outf)
outf.close()
