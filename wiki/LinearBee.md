

## Overview of Delver Sprite Graphics

Cythera stores most of its graphics in a format which we call Delver Sprite Graphics (although perhaps "Delver Compressed Graphics" would be a better term). Unfortunately, a custom graphics format was employed, rather than a standard format like GIF or PNG. This was a curious choice, since libpng was available and permissively licensed in 1995. 


## Performance

Despite the fact that the format was custom made for this application, its design seems surprisingly convoluted, with bits packed in everywhere. [DelvEd](DelvEd)'s compressor does not appear to produce optimal results (it often generates numerous Copy operations where one Run operation could do the job more efficiently, for example), so in theory it could have had better compression performance. 

The compression implementation in [delv](delv) is about 6-7% better than that of [DelvEd](DelvEd) in terms of the size of the compressed files, mainly by making appropriate use of the run length encoding opcodes. It is probable that delv's algorithm is vastly slower than [DelvEd](DelvEd)'s, though, even allowing for the fact that delv is written in Python and [DelvEd](DelvEd) was written in C++. 


|**All Compressed Graphics**|||
|-|-|-|
|**Original Size ([DelvEd](DelvEd)'s Compressor)** | **Size in PNG (PIL default)** | **delv's Compressor**|
|1,735,476 bytes  | 1,571,763 bytes | 1,610,826 bytes|
|**Unsized Graphics Only**|||
|1,028,645 bytes  | 1,006,790 bytes | 968,131 bytes|
|**Tiles (8Exx) Only**|||
|595,852 bytes  | 542,024 bytes | 537,132 bytes|



Unsurprisingly, given the design and implementation resources available to a major graphics format, PNG comes out ahead in many cases. (To be fair, I don't know if libpng in 1995 had as good of performance.) PNG is suffering here under the considerable handicap of having to include the colormap in each file, whereas the colormap is implicit in DCG. If the graphics had been broken up into only a few PNG images (e.g. all tiles in one image, all portraits in one image, etc) it might prevail more definitively. In total, there are about 290 kB of colormaps (palettes) in the PNG version of the graphics, meaning that PNG would trounce DelvED DCG by 24% and delv DCG by 17% if the colormaps were stored separately. 

It takes delv about 2 minutes to compress all the data except the sized graphics (subindex 131), and about five minutes in total. We have no information about how long it would take [DelvEd](DelvEd) to compress Cythera's graphics. 


## Nature of the Format

The format is a sliding-window compression scheme similar to LZ77. 

The format in files are organized as a sequence of drawing commands interspersed with pixel data. The decompressed image produced is treated in a strictly linear manner; the drawing position cursor advances with no backtracking or skipping pixels. Certain commands can copy pixels that have already been drawn - this copying is always with reference to the linear sequence of pixels already drawn, and not with reference to the underlying file or command structure. 

Note that although the decoded image has two dimensions - width and height - the decompression commands are totally agnostic to this, and see the image as just a linear sequence of pixels. They are displayed ordered left to right, then top to bottom. 

Delver Sprite Graphics always use 8 bit indexed color, and the color palette is implicitly the [one used by the game](http://sfiera.net/~sfiera/cythera/clut.html). Colors 0xE0-0xFB inclusive are subject to palette animation. 


## Header and Image Size

Some resources have a four-byte header, namely those in [Cythera Data Subindex 142](Cythera-Data-Subindex-142), which describes the size of the image. Other resources of this type do not have a header, and their size must be inferred from their type. 


|**Optional Header**|||||
|-|-|-|-|-|
|(Found only in [Sized Image](Cythera-Data-Subindex-142) resources, 8Fxx)|||||
|**Byte 0** | **Byte 1**| | **Byte 2** | **Byte 3**|
|_X size_, high bits | _X size_, low bits | _Flags_ | _Y size_, high bits | _Y size_, low bits|
|0bXXXXXXXXXXXXXX| | 0bFF | 0bYYYYYYYYYYYYYYYY||



If flags is set, the image contains additional data, which is encoded in the same bytes and with the same method as the image data, but which should not be shown to the user. It appears logically to the right of the image data. This data has not been analyzed at this time. It may relate to objects that are clickable or can be the target of dragged-and-dropped objects only in certain areas. The following ad hoc values have been determined:  


|_Flags_ | **Visual Width** | **Logical Width**|
|-|-|-|
|0b00 | _X size_ | _X size_|
|0b01 | _X size_+1 | _X size_+4|
|0b10 | _X size_+2 | _X size_+4|
|0b11 | _X size_+3 | _X size_+4|




|**Implicit Sizes**|||
|-|-|-|
|**Type** | **Width** | **Height**|
|[Sprite or Tile](Cythera-Data-Subindex-141) (8Exx) | 32 | 512|
|[Landscape](Cythera-Data-Subindex-131) (84xx)  | 288 | 32|
|[Portrait](Cythera-Data-Subindex-135) (88xx)  | 64 | 64|




## Algorithm for Reading

After reading the header (if applicable), initialize the drawing position cursor (hereafter, the cursor) to 0,0. 

* Read one command (documented below) and any associated data bytes from the file. 
* Execute the command. 
* Repeat until reaching the termination command. 

|**Decoding Commands**||
|-|-|
|Prefix | Command|
|0b1111111* | Terminate 0xFF|
|0b11110*** | Long Run 0xF0|
|0b1110**** | Short run [0xE0-0xEF]|
|0b1101**** | Unknown [0xD0-0xDF]|
|0b1100**** | Pixel Data [0xC0-0xCF]|
|0b10****** | Long Copy [0x80-0xBF]|
|0b0******* | Short Copy [0x00-0x7F]|




## List of Commands


### Short Copy (0x00-0x7F)


|**Copy (2-Byte form)**||||||
|-|-|-|-|-|-|
|**Byte 0**| | **Byte 1**|| | **0 or more bytes**|
|OPCODE | _Index_ | _Index (High Bits)_ | _Literals_ | _Length_ | DATA|
|0b0 | 0bBBBBBBB | 0bCCC | 0bDD | 0bFFF | 8-bit Indexed Color Pixels|



Draw _Literals_ pixels to the image, if there are any. (Which advances the cursor.)  

The index is 0bCCCBBBBBBBB. It can be calculated as Byte0 | (Byte1&0xE0)<<3. 

Starting from -1*(index+1), (where the cursor is 0, the previous pixel is -1, and so forth), copy a total _Length_+3 pixels to the cursor. If there are less than _Length_+3 pixels, the copied pixels are repeated to fill the required length. 

The maximum distance that can be copied from is -1024, but the short form's maximum copy length is only 10. 


### Long Copy (0x80-0xBF)


|**Run (3-Byte form)**||||||||
|-|-|-|-|-|-|-|-|
|**Byte 0**| | **Byte 1**| | **Byte 2**| | **0 or more bytes|
|OPCODE | _Index_ | _Index (High bits)_ | _Length_ | _Index (Higher bits)_ | _Literals_ | DATA|
|0b10 | 0bAAAAAA | 0bBBB | 0bCCCCC | 0bDDDDDD | 0bEE | 8-bit Indexed Color Pixels|



Copy length is _Length_ + 3. The index is -(0bDDDDDDBBBAAAAA + 1), same semantics as Short Copy, including for following literals if any there be. The maximum copy length is 34, and the maximum copy distance is 32768. 


### Long Run (0xF0-0xF7)


|**Run (3-Byte form)**||||
|-|-|-|-|
|**Byte 0** | **Byte 1** | **Byte 2**|
|OPCODE | _Length_ | _Color_|
|0b11110000 | 0bBBBBBBBB | 0bCCCCCCCC|



Draw _Length_+3 pixels of color _Color_ to the image. This can encode runs from 3 to 258 pixels of one color. 

It is not clear why it does _not_ draw *_Length_+19 pixels, since presumably the Short Run (0xEX) could be used in any case where less than 19 pixels of the same color need to be drawn. But this is how it is. 

In the existing corpus of Cythera graphics, we only see Long Runs beginning with 0xF0, and thus, conservatively, the opcode is 0xF0. However, Opcodes from 0xF0 to 0xF7 seem to be interpreted as Long Run. The three extra bits do not appear to affect anything, though. 


### Short Run (0xEX)


|**Run (2-Byte form)**|||
|-|-|-|
|**Byte 0**| | **Byte 1**|
|OPCODE | _Length_ | _Color_|
|0b1110 | 0bBBBB | 0bCCCCCCCC|



Draw _Length_+3 pixels of color _Color_ to the image. This can encode runs from 3 to 18 pixels of one color. 

For example 0xBE 0x00 would make a run of 17 pixels of transparency (Color 0x00). 


### Pixel Data (0xCX)


|**Pixel Data**|||
|-|-|-|
|**Byte 0**| | ** 4 or more bytes...**|
|OPCODE | _Length_ | DATA|
|0b1100 | 0bBBBB | 8-bit Indexed Color Pixels|



The number of data bytes following is (_Length_+1)*4, e.g. 0xC0 is followed by four data bytes, and 0xC2 is followed by 12 data bytes. 
### Terminate (0xFF)


|**Terminate**|
|-|
|**Byte 0**|
|OPCODE|
|0b11111111|



Stop executing graphics commands. The command used in the Cythera graphics is 0xFF, but experimentally, 0xFE also seems to terminate the stream. 


### Short Data (0xDx)

0xD2 and 0xD1 appear in the corpus. It has not been tested at present if more than 2 bits are devoted to literals - if so, presumably there are 0bBBCC literals following. Why it is not _literals_+1 is not known. 


|**Short Data 0xDx**||||
|-|-|-|-|
|**Byte 0**|| | ** 0 or more bytes...**|
|OPCODE | _Unknown_ | _Literals_ | DATA|
|0b1101 | 0bBB | 0bCC | 8-bit Indexed Color Pixels|




### Unknown Opcode (0xF1-0xFE)

What any of these commands do is not currently known. Most of them haven't been seen, and might simply be unimplemented. 0xFE at least is interpreted the same as 0xFF and 0xF1 is interpreted as 0xF0. 


## Editing

For the convenience of anyone undertaking to edit Delver Sprite Graphics, provided here is a template with the correct indexed color map and grid for a sprite. The 0x00 color map entry, which appears white in the editor, is transparent. Do not use actual transparency provided by your graphics editor. Note also that although it's called "sprite", the template can be used for other kinds of graphics (resize it to 64x64 for a portrait, for example). Definitely do not change it from indexed color to RGB or alter the color map. 

Here is the file in PNG format: [sprite_template.png](sprite_template.png) XCF: [sprite_template.xcf](sprite_template.xcf) 

GIMP Palette for Cythera: [Cythera-Colors.gpl](Cythera-Colors.gpl) (Note that using this palette is not enough if you are creating an image _de novo_ for importation by redelv or dsencoder, it needs to be the color map of your indexed-color image. When you convert to indexed color in GIMP, it provides you the option to use a custom palette - choose this one. Also, uncheck any option to remove unused colors.) 

[LinearBee](LinearBee) can view individual resources in this format, and save them to PNG. 

A simple tool, [dsencoder.py](dsencoder.py), is available to convert graphics back into the sprite format.  

Archived notes and working theories: [Cythera Graphics Working Page](Cythera-Graphics-Working-Page) 
