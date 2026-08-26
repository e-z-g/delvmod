
Contains [maps](Cythera-Map). 



```
 ---- SUBINDEX 127 ---- 
Index 0, ID 8000 Length: 2080 bytes         Unrecognizable, 32x32 possibly. Res 1400 calls it "Map"
Index 1, ID 8001 Length: 131104 bytes       Main map, 256 x 256, no roofs
Index 2, ID 8002 Length: 10272 bytes        Odemia, 64x64, has roofs
Index 3, ID 8003 Length: 8224 bytes         Land King Hall, 64x64
Index 4, ID 8004 Length: 2080 bytes         Abandoned farmhouse, 32x32
Index 5, ID 8005 Length: 160 bytes          Farmhouse cellar, 8x8
Index 6, ID 8006 Length: 11552 bytes        Catamarca, 64x64. Has roofs.
Index 7, ID 8007 Length: 2080 bytes         Catamarca underground?, 32x32
Index 8, ID 8008 Length: 45856 bytes        Cademia, 128x128, roofs, 
Index 9, ID 8009 Length: 32800 bytes        Underground, 128x128, including Ayrit and caves you travel thourgh to get there.
Index 10, ID 800A Length: 2080 bytes        Headwater ruins, 32x32 (where to find Timon)
Index 11, ID 800B Length: 8352 bytes        Swamp ruins, 64x64 
Index 12, ID 800C Length: 9376 bytes        Pnyx lower story, 64x64, with... roofs? or some other data.
Index 13, ID 800D Length: 12832 bytes       Kosha, 64x64, with roofs
Index 14, ID 800E Length: 8096 bytes        Pnyx upper story and Pnyx crypts, 56x72
Index 15, ID 800F Length: 2080 bytes        House Attusa's Iron mine underground, probably
Index 16, ID 8010 Length: 8224 bytes        Landsend Volcano underground, 64x64, 
Index 17, ID 8011 Length: 800 bytes         Charax's house, 16x16, roof
Index 18, ID 8012 Length: 4512 bytes        North shore vineyard, 32x64, roofs
Index 19, ID 8013 Length: 8224 bytes        Maayti Underground, 64x64
Index 20, ID 8014 Length: 4512 bytes        Southland vineyard, 64x32, roofs
Index 21, ID 8015 Length: 8224 bytes        Cademia sewers, 64x64
Index 22, ID 8016 Length: 2336 bytes        Flax farm, 32x32, unusual roofs
Index 23, ID 8017 Length: 2080 bytes        Kosha Grotto. 32x32
Index 24, ID 8018 Length: 8992 bytes        House Attusa's Iron mine aboveground, 64x64, roofs
Index 25, ID 8019 Length: 8224 bytes        Tyrant's tomb, 64x64
Index 26, ID 801A Length: 4512 bytes        Cult of Scylla, 64x32 
Index 27, ID 801B Length: 8224 bytes        Crab cove south of Kosha, 64x64
Index 28, ID 801C Length: 8224 bytes        Machaon's workship under Cademia, 64x64
Index 29, ID 801D Length: 4640 bytes        Abydos ruins, 48x48
Index 30, ID 801E Length: 2080 bytes        Abydos underground, 32x32
Index 31, ID 801F Length: 5792 bytes        Stronghold of the Brotherhood, 48x48
Index 32, ID 8020 Length: 5792 bytes        Ruffian encampment. 48x48. Roofs.
Index 33, ID 8021 Length: 8224 bytes        Dungeon of the Stronghold of the Brotherhood, 64x64
Index 34, ID 8022 Length: 8224 bytes        Harpy Cave, 64x64
Index 35, ID 8023 Length: 8224 bytes        Eioneus's cave, 64x64
Index 36, ID 8024 Length: 8736 bytes        Tavara's fortress, 64x64, has roof
Index 37, ID 8025 Length: 8224 bytes        Tavara's fortress, 64x64, empty field if it disappears
Index 38, ID 8026 Length: 800 bytes         Cademia bridge, 24x16
Index 39, ID 8027 Length: 8480 bytes        Tree of Life, 64x64, some "roof" data
Index 40, ID 8028 Length: 8224 bytes        Omen's test, 64x64, 
Index 41, ID 8029 Length: 1568 bytes        Harpy cave aboveground, 32x24
```

This is strictly a quick hack, you will have to examine the source to figure out how it works... 
<div>
```highlight
#!/usr/bin/env pythonfrom PIL import Image,ImageDrawfrom sys import argvdat = open(argv[1]).read()width=int(argv[2])zoom=int(argv[4])height = int(argv[5])imx = Image.new("RGB", (zoom*width,zoom*height), (0x80,0x80,0x80))im = ImageDraw.Draw(imx)offset = int(argv[3])print ("%02X "*0x10)%tuple(ord(c) for c in dat[:0x10])i = offsetx = 0y = 0while i < len(dat):	x = 0	while x < width and i < len(dat):		d2 = ord(dat[i])		d = ord(dat[i+1])		im.rectangle((zoom*x,zoom*y,zoom*x+zoom-2,zoom*y+zoom-2), fill=(d&0xF0, (d<<4)&0xFF, d2))		x += 1		i += 2	y += 1 	 print x,yimx.show()imx.save(argv[1][argv[1].find('/')+1:]+'.png')
```
</div>
[mapview.py](mapview.py) 
