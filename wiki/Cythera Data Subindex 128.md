
These resources contain lists of prop records, which describe objects in maps of the corresponding index. E.g. Object List 8129 is associated with Map 8029. 

[List of Prop Types](List-of-Prop-Types) may be helpful, also [Delver Eggs](Delver-Eggs) 

Each record is 16 bytes.  


|**Field** | **Type** | **Value**|
|-|-|-|
| Flags?  |  uint8  |  00 for objects in the level |
| Coordinates X, Y |  12 bits, 12 bits  |  Position of the object (or, points to index of prop this is inside) |
| Aspect  |  6 bits  |  Visual aspect (added to base tile ID, e.g. for animations) |
| Prop type  |  10 bits  |  What manner of dingus is this (index into F000 to determine what tile to use; Script object 0x1000 + prop id)|
| d1  |  uint8  |  First persistence data field |
| d2  |  uint8  |  Second persistence data field |
| Other Proper Reference?  |  uint32?  |  |
| Storage reference  |  uint16  |  Reference to the under-utilized storage mechanism used by bellows, troughs, shutters and candlesticks. |
| Unknown  |  uint16  |  |



== Working Notes 

Seems to contain lists of objects in maps of the corresponding index. E.g. Object List 8129 is associated with Map 8029. 

These are 16-byte records. They probably initialize props on the map. 

Note that, per gandreas, altering these records should only affect creating a new game. Indeed, the [Cythera Player File](Cythera-Player-File) appears to contain resources of this type (81xx) although the IDs are slightly sparse. 

Resource 8105, Farmhouse cellar. A fine example, as it contains only two objects. (The ladder and the kidnapped lady Ariadne or maybe an egg) 

```
00    001,003   08 2A   00 09   00 00 00 00  00 00 00 00
42    003,003   20 5D   04 04   00 00 00 00  00 00 00 00
flag?   x   y   ObjID   d1 d2         stref        prprf
```

The first entry is the ladder, identifiable by its player-moving-object-index (09, "next to trapdoor to cellar"). The ladder is located at 1,2 on the map (zero-based coordinates). But Cythera uses 1-based map coordinates, apparently, so really the ladder is considered to be at 2,3. The coordinates are 12-bit fields :( So three bytes for x,y.  

Although, the ladder is a multi-tile prop (32x64). It lives in 8E38+1,2. Prop images start at 0x8E20, or 8E1C if roofs are counted. None of these appear to relate. 

The second entry might be Ariadne, or an egg.  

Gandreas has this to say about props - albeit presumably props in memory:  

```
Props ... are stored in a list. Each prop had a location ... object ID & aspect. The object ID was used to map to which specific tile. The aspect would then be added to that tile ID to tell the renderer what tile to draw (and if that tile included the various multi-part bits, the resulting object would span multiple tiles).

The object ID would also associate a tile with the scripting object system (which will be discussed later). Props also had several additional fields used for storing persistent data with that prop - two single byte values ("d1", "d2", which could be treated as a 16 bit value "d3") a reference to another prop, and a general storage reference (which was kept in the persistent memory storage - this kept things that didn't fit in 2 byte data, such as the on screen window location for an open container).
```

Ariadne's noblewoman sprite is stored in 0x8E63. 

Taking an example from 8129, Harpy Cave above ground. 

There are 29 records, [0..28]. The file contains no indication of the number of records, nor does the 80xx resource, so the number of records is probably inferred from the length of the 81xx resource.  

The 27th (0 based indexing) entry: 

```
00 01000B   01 4C   00 7F   00 00 00 00  00 00 00 00
```

The significance of 00 is not known.  

010 00B are the coordinates, 12 bits each, apparently. 

01 4C is the object resource that has scripts for this object. 114C (i.e. 0x1000 + 0x014C) is the Rock Outcropping. This field appears to be a densely packed structure, it's probably (bletch) 12 bits... 

The rock outcropping is located at 16,11. (Iinitially. Objects in general can be moved around the map.) 

00 7F is the index into the table referenced by zone-changing-objects, as determined by [editing saved games](Cythera-Save-File-Hacks). 

The other eight bytes are probably additional parameters of the object, for objects that have them. 

![](Cythera-Data-Subindex-128/cademia-items.png) 

Object viewer (strictly a quick hack, sorry): <div>
```highlight
#!/usr/bin/env pythonfrom sys import argvfrom PIL import Image,ImageDrawdef bytess(st):	return ' '.join(['%02X'%ord(x) for x in st])def bytesl(st):	return ' '.join(['%02X'%x for x in st])rd = open(argv[1]).read()zoom = int(argv[2])width = int(argv[3])height = int(argv[4])imx = Image.new("RGB", (zoom*width,zoom*height), (0x00,0x00,0x00))im = ImageDraw.Draw(imx)im.rectangle((0,0,0+width*zoom,0+height*zoom),(255,255,255))i = 0j = 0while i < len(rd):	r = [ord(c) for c in rd[i:i+16]]	print " -- Entry %3d @ 0x%04X -- "%(j,i)	print "Raw:",bytesl(r)	# 00 10 03 = 2,3        # 01 00 0B = ,12	u1 = r[0]	x = (((r[1]<<8) | r[2])&0xFFF0 ) >> 4	y = ((r[2]<<8) | r[3])&0x0FFF        u2 = (r[4]&0xF0)>>4	scobj = ((r[4]&0x0F)<<8) | r[5]	im.ellipse((x*zoom+1,y*zoom+1,x*zoom-2+zoom,y*zoom-2+zoom),fill=(scobj&0xFF,u2,(scobj<<4)&0xFF))	print "U1: %d  U2: %d"%(u1,u2)	print "Coordinates: %d,%d   ObjType: %d [%04X]"%(x,y,scobj,scobj)	print "Parameters:", bytesl(r[6:])	i += 16	j += 1	printimx.show()imx.save(argv[1][argv[1].find('/')+1:]+'.png')
```
</div>[objectsview.py](objectsview.py) 

Open question: gandreas says: "* Everything is loosely locked to the same grid that U6 would have (which in Cythera is 32 pixels), as oppposed to U7 which is four times finer (though there is a "subgrid" of 8 pixels that objects can be aligned to)." This seems to imply some kind of object alignment, but nothing of it appears here. Perhaps it relates to animation? 

Cademia items: 

```
The chests in the mint have 540, 0 and 45 oboloi. (left to right)
Oboloi:
0645[0285]@0x2850: (i000382) 0x09 ID 1C82, d1 =   2 [0x02], d2 =  28 [0x1C] | d3 =   540 OtherProp=0x00000000 StoreRef=0x00000000
0646[0286]@0x2860: (i000384) 0x09 ID 1C82, d1 =   0 [0x00], d2 =  45 [0x2D] | d3 =    45 OtherProp=0x00000000 StoreRef=0x00000000
Here are the chests (found by location -only thing there, also, they are right before the oboloi, strengthening the association):
Chests containing them:
0642[0282]@0x2820: ( 18, 28) 0x00 ID 0C8D, d1 =   0 [0x00], d2 =   0 [0x00] | d3 =     0 OtherProp=0x00000000 StoreRef=0x00000000
0643[0283]@0x2830: ( 19, 28) 0x00 ID 0C8D, d1 =   0 [0x00], d2 =   0 [0x00] | d3 =     0 OtherProp=0x00000000 StoreRef=0x00000000
0644[0284]@0x2840: ( 20, 28) 0x00 ID 0C8D, d1 =   0 [0x00], d2 =   0 [0x00] | d3 =     0 OtherProp=0x00000000 StoreRef=0x00000000

Seems to be the oboloi in the right blast-trapped chest of gold in house Comana (854, the number of oboloi, appears as d3 in only one field, also suggesting 
that d1/d2/d3 have been correctly found.)
1172[0494]@0x4940: (i020592) 0x08 ID 1C82, d1 =   3 [0x03], d2 =  86 [0x56] | d3 =   854 OtherProp=0x00000000 StoreRef=0x00000000

House Comana chests:
1170[0492]@0x4920: ( 36, 54) 0x00 ID 088D, d1 =   0 [0x00], d2 =   0 [0x00] | d3 =     0 OtherProp=0x00000000 StoreRef=0x00000000
1171[0493]@0x4930: ( 35, 54) 0x00 ID 088D, d1 =   0 [0x00], d2 =   0 [0x00] | d3 =     0 OtherProp=0x00000000 StoreRef=0x00000000

The pattern emerging is that the prop index has 0x100 added to it... perhaps the first 256 entries are reserved for global props, i.e. characters?
So if the location field was 0x09,000001 that would be in prop 1's inventory (presumably the Hero?) How do the characters drag around their inventories?
Say I pick up that chest with the oboloi in it, and walk to another zone... it seems like the oboloi's pointer would have to be dynamically modified to point at the chest in its new list position somewhere else... because otherwise, what if the player picks up an item with the same index in a different zone?
Maybe all this is just for loading, and it's replaced by proper pointers at runtime... either way, it's no wonder Fetch doesn't work, that could get complicated.

What the high byte of the location field is used for when an item is in another prop's inventory is unclear, but it does seem to have some data.

```


## StoreRef and OtherProp

gandreas said: "Props also had several additional fields used for storing persistent data with that prop - two single byte values ("d1", "d2", which could be treated as a 16 bit value "d3") a reference to another prop, and a general storage reference (which was kept in the persistent memory storage - this kept things that didn't fit in 2 byte data, such as the on screen window location for an open container)." 

There are 8 bytes unaccounted for after the prop ID, basic persistence information, location and flags are accounted for, and we provisionally assume that the other 8 are the "reference to another prop", [OtherProp](OtherProp), and "a general storage reference". 

If [StoreRef](StoreRef) is interpreted as 2 bytes (+8 and +9), then [StoreRef](StoreRef) appears to be unique across all prop files. There are only 12 in the whole game, and an awful lot of them (7)  are in Odemia compared with anywhere else. The appear to, in fact, be the first seven such in the game: 



```
0040[0028]@0x0280: ( 45, 46) 0x00 ID 007B, d1 =   0 [0x00], d2 =   0 [0x00] | d3 =     0 OtherProp=0x00000000 StoreRef=0x00060000
      Bellows at blacksmith shop

0059[003B]@0x03B0: ( 47, 44) 0x00 ID 007F, d1 =   0 [0x00], d2 =   0 [0x00] | d3 =     0 OtherProp=0x00000000 StoreRef=0x00070000
      Water trough at blacksmith shop

0133[0085]@0x0850: ( 28, 41) 0x00 ID 04E2, d1 =   0 [0x00], d2 =   0 [0x00] | d3 =     0 OtherProp=0x00000000 StoreRef=0x00050000
    A candle on a tall stand in the inn 

0134[0086]@0x0860: ( 18, 37) 0x00 ID 04E2, d1 =   0 [0x00], d2 =   0 [0x00] | d3 =     0 OtherProp=0x00000000 StoreRef=0x00030000
    A candle on a tall stand in the inn 

0135[0087]@0x0870: ( 28, 34) 0x00 ID 04E2, d1 =   0 [0x00], d2 =   0 [0x00] | d3 =     0 OtherProp=0x00000000 StoreRef=0x00040000
    A candle on a tall stand in the inn 

0704[02C0]@0x2C00: ( 26, 33) 0x00 ID 8538, d1 =   0 [0x00], d2 =   0 [0x00] | d3 =     0 OtherProp=0x00000000 StoreRef=0x00020000
    A closeable window shutters

0705[02C1]@0x2C10: ( 21, 36) 0x00 ID 8D38, d1 =   0 [0x00], d2 =   0 [0x00] | d3 =     0 OtherProp=0x00000000 StoreRef=0x00010000
    A closeable window shutters
```

This singular collection of objects has one thing in common, in that all are named in resource F015.  F015 appears to assign names to each object, e.g. Od_Candle2 (presumably for Odemia Candle 2) but they do not appear to be in any particular order in that resource. FYI, F015 consists of {short, cstring} pairs. The short seems to be the same as the bytes we're calling [StoreRef](StoreRef), e.g. the water trough in Odemia has [StoreRef](StoreRef)=0007 and its entry in F015 is {0x0007, "Od_Trough1"}. 

The fact that this mechanism is used only early on (various evidence suggests that Odemia was probably the first town gandreas made). The fact that doesn't seem to have much been used goes along with his comment that it didn't work very well. Perhaps F015 is debugging symbols? 

It appears that the [StoreRef](StoreRef) trail goes cold at F015. Perhaps it can be caught again by opening and closing shutters in Odemia, and seeing what changes in the save file, and then looking for similar data in Cythera Data. Or, on the other hand, the persistence data might be manually initialized by a script, and has no initial values stored in the scenario file. 
