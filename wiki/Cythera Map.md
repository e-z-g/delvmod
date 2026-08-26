

## Header

The map begins with a 32-byte header. 


|**Field** | **Type** | **Value**|
|-|-|-|
|Width | uint16 | Width of the map, in tiles.|
|Height | uint16 | Height of the map, in tiles.|
|Flags? | uint16 | Always 0|
|Size of roof data | uint16 | 0x40*size words (uint16) of roof data follow the header.|
|Size of roof data | uint16 |  Always the same. |
|Horizontal edge propagation | uint8 | See below|
|Vertical edge propagation | uint8 | See below|
|North exit port | uint16 | Where does the player go if exiting off the north edge?|
|East exit port | uint16 | Same, but for east edge|
|South exit port | uint16 | Same, but for south edge|
|West exit port | uint16 | Same, but for west edge|
|Padding | char[12] | Always 0s.|



If an edge propagation parameter is 0, the world past the edge of the map appears black. (Also, the player cannot exit the map by walking off it, except to the north?)  If it is an integer (at least 1,2,4 and 8 are legal values) the world past the edge of the map is instead formed by copying the edge tiles, and this parameter controls the length of the repeated pattern.  

Maps should not exceed 4096x4096 in size because prop coordinates are 12-bit. 


## Roof Data

Immediately follows the header, if there is any roof data. The roofs appear to be stored in 8-tile strips. Much is yet to be elucidated.  


|**Field** | **Type** | **Value**|
|-|-|-|
|Roof tiles | uint16[0x40*roof_data_size] | Tiles making up various roofs|




## Map Data

Immediately follows the roof data (or header, if no roof data). It is stored left to right, top to bottom. 


|**Field** | **Type** | **Value**|
|-|-|-|
|Map tiles | uint16[width*height] | Tiles making up the map|



Note that the tiles can be [Composed Tiles](Composed-Tiles) 


## Notes

See [Cythera Map Working Page](Cythera-Map-Working-Page) 

Starts with two short integers, probably the dimensions of the map, e.g resource 8026: 



```
00 18 00 10         //  24 by 16 map.
```

Some other stuff, the meaning of which is yet to be elucidated, beyond that the overlined bytes are zero if there is not an extended block:  

```
                   __A__   __B__
             00 00 00 00   00 00 04 04  00 00 00 8E
00 00 00 8F  00 00 00 00   00 00 00 00  00 00 00 00
```

A == B, it seems. There will be A*0x80 bytes between the end of the header (byte index 0x20, the 33rd byte of the resource from the first) and the start of the map data. 

The total header size is 32 bytes. 

In some resources, following this immediately is an array of 2-byte integers, the number of items being the width times the height in the header. This is probably the map data. Conjecturally, they may be tile IDs as seen in [Delver editor stamp](Delver-editor-stamp)s. 

At least some resources are not fully described by this, e.g. 8024, which is longer. It has an extended block structure between the header and the array of the presumptive map data. This might represent roofs or something. 



```
Resource 8024 Header (followed by extended block of 0x200 bytes)
00 40   00 40   00 00   00 04   00 04   08 08   00 84   00 84
00 84   00 84   00 00   00 00   00 00   00 00   00 00   00 00

Resource 8016 Header (followed by extended block of 0x100 bytes)
00 20   00 20   00 00   00 02   00 02   08 08   00 5C   00 5C
00 5C   00 5C   00 00   00 00   00 00   00 00   00 00   00 00

Resource Header 8026 (not followed by an extended block)
00 18   00 10   00 00   00 00   00 00   04 04   00 00   00 8E
00 00   00 8F   00 00   00 00   00 00   00 00   00 00   00 00

Resource Header 8025 (not followed by an extended block)
00 40   00 40   00 00   00 00   00 00   08 08   00 84   00 84
00 84   00 84   00 00   00 00   00 00   00 00   00 00   00 00

Resource Header 8012 (followed by an extended block of 0x180 bytes)
00 20   00 40   00 00   00 03   00 03   08 08   00 4C   00 4C
00 4C   00 4C   00 00   00 00   00 00   00 00   00 00   00 00

Resource Header 8006 (followed by an extended block of 0xD00 bytes possibly with substructure)
00 40   00 40   00 00   00 1A   00 1A   08 08   00 0A   00 0A
00 0A   00 0A   00 00   00 00   00 00   00 00   00 00   00 00


```
