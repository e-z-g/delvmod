
Composed Tiles are made up of pieces of other tiles. Tiles with IDs 0x0000 to 0x0FFF are simple tiles, IDs 0x1000 to 0x1FFF are composed. 

The resource 0xF013 describes the composed tiles. It is an array of 0x1000 tile composition descriptions. Each description is 32 bytes, consisting of 16 2-byte words. Each word describes one 8x8 pixel chunk of the composed tile, with the first describing the upper left corner of the composed tile, proceeding left-to-right, top to bottom. The format of the word is thus: 


|**Nybble 0** | **Nybble 1-Nybble 2** | **Nybble 3**|
|-|-|-|
|Segment of source tile to use | 8Exx Resource of source | tile of resource to use|



(I.e. description_word&0x0FFF is the tile-id of the source tile, and (description_word>>12) is the segment to use.) 

Segments are numbered starting from the 8x8 pixel chunk in the upper left corner of the source tile, but going top to bottom, left to right, instead of the way you'd probably expect (L->R, T->B). 
