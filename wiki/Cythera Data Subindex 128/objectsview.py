#!/usr/bin/env python
from sys import argv

from PIL import Image,ImageDraw


def bytess(st):
	return ' '.join(['%02X'%ord(x) for x in st])
def bytesl(st):
	return ' '.join(['%02X'%x for x in st])


rd = open(argv[1]).read()

zoom = int(argv[2])

width = int(argv[3])
height = int(argv[4])
imx = Image.new("RGB", (zoom*width,zoom*height), (0x00,0x00,0x00))
im = ImageDraw.Draw(imx)
im.rectangle((0,0,0+width*zoom,0+height*zoom),(255,255,255))
i = 0
j = 0
while i < len(rd):
	r = [ord(c) for c in rd[i:i+16]]
	print " -- Entry %3d @ 0x%04X -- "%(j,i)
	print "Raw:",bytesl(r)
	# 00 10 03 = 2,3
        # 01 00 0B = ,12
	u1 = r[0]
	x = (((r[1]<<8) | r[2])&0xFFF0 ) >> 4
	y = ((r[2]<<8) | r[3])&0x0FFF
        u2 = (r[4]&0xF0)>>4
	scobj = ((r[4]&0x0F)<<8) | r[5]
	im.ellipse((x*zoom+1,y*zoom+1,x*zoom-2+zoom,y*zoom-2+zoom),fill=(scobj&0xFF,u2,(scobj<<4)&0xFF))
	print "U1: %d  U2: %d"%(u1,u2)
	print "Coordinates: %d,%d   ObjType: %d [%04X]"%(x,y,scobj,scobj)
	print "Parameters:", bytesl(r[6:])

	i += 16
	j += 1
	print


imx.show()
imx.save(argv[1][argv[1].find('/')+1:]+'.png')
