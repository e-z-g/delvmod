#!/usr/bin/env python
from PIL import Image,ImageDraw
from sys import argv
dat = open(argv[1]).read()
width=int(argv[2])
zoom=int(argv[4])
height = int(argv[5])
imx = Image.new("RGB", (zoom*width,zoom*height), (0x80,0x80,0x80))
im = ImageDraw.Draw(imx)
offset = int(argv[3])
print ("%02X "*0x10)%tuple(ord(c) for c in dat[:0x10])
i = offset
x = 0
y = 0
while i < len(dat):
	x = 0
	while x < width and i < len(dat):
		d2 = ord(dat[i])
		d = ord(dat[i+1])
		im.rectangle((zoom*x,zoom*y,zoom*x+zoom-2,zoom*y+zoom-2), fill=(d&0xF0, (d<<4)&0xFF, d2))
		x += 1
		i += 2
	y += 1 
	 
print x,y
imx.show()
imx.save(argv[1][argv[1].find('/')+1:]+'.png')
