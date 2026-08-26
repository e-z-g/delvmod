
Properties of tiles are stored in resource F002. Names of tiles are in F004. 



```
Byte 0: Top nybble, mutually exclusive bits (layer?). Bottom nybble, unused.
0x80 Set on mouseholes only
0x40 Set on ropes and fences
0x20 Set on passthrough, oak door, windowed door, metal door, stone door, wooden door, curtain - second parts of some closed versions
0x10 Set on ethereal void (and some props: crack,vines,slime,floor, b0=0x10
0x08 Unused
0x04 Unused
0x02 Unused
0x01 Unused

Byte 1:
0x80
0x40
0x20 Unused
0x10
0x08 Unused
0x04 
0x02
0x01 Script parameter if there is script?

Byte 2:
0x80 Direction bits for reshaper?
0x40 Direction bits for reshaper?
0x20 Direction bits for reshaper?
0x10 Direction bits for reshaper?
0x08 Has associated script for when something moves onto it (traps, lava, swamp etc) 
0x04 
0x02 Blocks terrestrial movement
0x01 Is water

Byte 3:
0x80 Extends leftward
0x40 Extends upward
0x20 
0x10 
0x08 Blocks Vision unless adjacent
0x04 Blocks Vision
0x02 Light source high bit
0x01 Light source low bit 

```

How tiles are stored and referenced is a very important open question. 

We know where and how the tile graphics are stored, and how they are referred to in maps, but where are tiles defined? Things like pseudo-props (e.g. a tree on a ground tile that doesn't appear in the prop list for the level), special terrain type (e.g. swamp that runs a script that poisons people sometimes when walking over it), line of sight blocking, walkability for different types of creatures -- where is all this united with a graphic? 31f 

Some examples of tile entries: WARNING, SOME OF THE LATER ONES ARE INCORRECT 


|**ID** | **Description**|
|-|-|
|0000 | White square "Nothing"|
|0001 | Grass|
|0002-0004 | Swamp|
|0005 | Swamp with shrub|
|0006 | Swamp with broadleafed plant pseudoprop|
|0007 | Swamp with large flowering plant pp|
|0008-000B | Ocean (going in different directions)|
|000C-000F | Ocean (going different directions)|
|0010 | Shore (north)|
|0011 | Shore (northeast)|
|0012 | Shore (east)|
|0013 | Shore (southeast)|
|0014 | Shore (south)|
|0015 | Shore (southwest)|
|0016 | Shore (west)|
|0017 | Shore (northwest)|
|0018-001B | Shore interior corners (SE,SW,NE,NW)|
|001C-001F | Straight shore (NESW) red dirt)|
|0020-0023 | More regular shore|
|0024-002F | Repeat of previous (002C=001C) but with different water animation/direction?|
|0030-0033 | Broadleaf plant on interior corners of shore|
|0034 | Grass with some red dirt visible|
|0035 | Grass with some red dirt visible and a small stone at the top|
|0036 | Grass with some red dirt visible and a different small stone near the bottom right|
|0037 | Grass with some red dirt visible|
|0038 | Grass with some red dirt visible and a different long stone near the top|
|0039 | Grass with some red dirt visible|
|003A | Verdant grass (lower right)|
|003B | Verdant grass (upper right)|
|003C-003F | More verdant grass (horizontal, ul,lr,vertical)|
|0040 | pp Tree on grass|
|0050 | grass-red dirt transition red dirt lower right|
|0060 | grass-plateau transition (plateau lower right)|
|0070 | mountain|
|0080 | Mountain peak?|
|0090 | Horizontal gray cut stone (or brick?) wall|
|00A0 | Adobe wall horizontal|
|00B0 | Rough stone wall horizontal|
|00C0 | Cut stone wall with small window|
|00D0 | Wooden floor (verticla planks)|
|00E0 | Large stone wall|
|00F0 | red ground|
|0100 | *Farm rows vertical on plain whtie background (probably not a real tile?)|
|0110 | *Ruffian encampment on white|
|0120 | *Cut stone wall with corner out of it|
|0130 | *Plant?|
|0140 | Lower part of slate roof tile?|
|0150 | *White, empty|
|0160 | *"Z" button|
|0170 | *"Party"/"Solo" unused buttons|
|0180 | *Move/attack buttons|
|0190 | *Interface elements|
|01a0 | *North-going fireball|
|01b0 | Pnyx upper-right corner?|



Tile entries in maps are known to be invariant across maps and across roof versus ground layer data. 

Tiles have a direct correspondence with subindex 141/8Exx resources, each of which contains 16 tiles. This includes 8EXX resources that describe things that should not be used as tiles, e.g. character sprites, interface elements, and objects - all can be made to appear as ground tiles on maps. 8Exx resources are densely packed from 0x8E00 to 0x8E9F. (The only other 8Exx resource is 8EFF, which is not tiles, but an image of a tombstone.) 

E.g, tile 0x09D3 corresponds to the resource 8E9D, the fourth tile from the top of the resource. (Counting from one.) 

An experiment to create a new tile graphic, insert it as 8EA0, and refer to it with tile references was not successful. The tiles appeared as the corresponding tiles from 8E00, instead (with some irregular flashing of corrupted data -- presumably wherever it is looking for the information about these tiles walkability etc is not initialized.) All were called "floor" by the game and were walkable and nonpoisoning (in spite of appearing to be a swamp and ocean in two cases.) Why tiles should be mapped back onto earlier ones is not clear. The obvious possibility of the 16-bit tile field actually being 4 and 12 bit fields does not appear to apply, because the transition from 09FF to 0A00 is unremarkable in binary. (The highest bit set is still 0x0800).  
