


```
8E02 - water borders grass
8E91 - certain trees
8E33 - Bookshelves.



16: C3

12: C2

8: C1  
    11000001

4: C0  
    11000000

3: 18,1C,19   
    00011000  18
    00011100  1C 
    00011001  19

2: 16,32,10
    00010110  16
    00110010  32
    00010000  10

1: 08,18, *32*, **C0**, 09, 0A, 38
    00001000  08
    00011000  18
    00001001  09
    00001010  0A
    00111000  38
    00110010  32*
    11000000  C0**
```


## Archived Stuff

This is a bytestream of op-codes and their operands (i.e. literal pixels). The examples found in subindex 141 of [Cythera Data](Cythera-Data) are not encrypted with the regular [Delver Archive](Delver-Archive) encryption, just compressed. It seems likely that the graphics are decompressed when the game loads, rather than when they are used - probably immediately before tiles are composited. 

An aside by your editor: All of the subindex 141 resources take up 595852 bytes, whereas a PNG of all of Cythera's sprites in indexed color with maximum compression takes up 622571 bytes, a savings of... 4.3%. libpng has existed since 1995 and is licensed under a permissive license that would have allowed its inclusion in a closed-source game. If I sound bitter, it's because figuring out this graphics format has just eaten its fourth weekend with many details still to be addressed... 

The following facts have been determined: It consists of a stream of commands and literal pixels. Pixels are drawn left-to-right, top-to-bottom, in general. The primary mode of compression is callbacks to sequences that have already appeared. Data can be repeated in whole or only in part, i.e. you can recall less than the entire previous sequence, and either they can be recalled in multiple directions, or rotation is applied to 32x32 tiles to facilitate better compression (see 8E33.) Border positions and content pixels seem strangely independent during mutation experiments, but it remains unclear why, if there are facilities for absolute repositioning of the cursor, there are so many low-entropy sequences which seem to serve only to advance the cursor position. 

It seems probable that each resources represents 16 32x32 tiles, organized as a 32 pixel / 1 tile wide, 512 pixel / 16 tile high image. (The earlier 128x128 theory was falsified by experiments with 8E22.) 

The parser begins expecting an opcode. Known opcodes (names provisional): 


|Opcode | Name | Meaning | Notes|
|-|-|-|-|
|0xCn | Extended Data |  (n+1)*4 bytes of image data follow, 1 byte per pixel  |  |
|0xFF | Terminate | Signifies the end of the opcode stream | Always seen at the end of resources. |
|0xF0 nn bb | Extended Run |  Repeat pixel bb nn+3 times. (E.g. 0xF001FF would make a run of 4 black pixels) | It is probable that there are bitflags in the first byte, as yet uninvestigated.|
|0xEn bb | Short Run |  Repeat pixel bb n+3 times. |  Does it also set the border color? |
|0x80 nn 0f [f literal bytes]  |  Other Run  |  Followed by f bytes of literal data, the last of which will be repeated nn+3 times. (for a total of nn+4) |  What differentiates it from 0xF0 ... ?|
|0xA0 ?? 0f [f literal data bytes] |  Unknown  |   |  ?? values seen include 2F, 0C, 0D |



The resource often begins with F0. The pattern 1F 00 80 is often seen in the bytestream. The most over-abundant bytes in the whole subindex 141 corpus are: (cutoff 1%) 


|**Byte** | **Percent Enrichment**|
|-|-|
|00 | 8.0|
|1F | 3.6|
|BF | 2.8|
|80 | 2.7|
|04 | 2.1|
|FF | 2.0|
|9F | 1.7|
|01 | 1.6|
|20 | 1.6|
|0C | 1.3|
|10 | 1.1|
|A0 | 1.0|



Bytes with 0 < enrichment < 1%: E0,E1,C0,C1,BE,A1,A2,9E,87,7F,61,60,41,40,3F,2C,22,21,1E,1D,1C,1B,19,18,17,16,14,12,11,0D,01,09,07,06,05,03,02. Particularly negative enrichment: none, interestingly. All negative enrichments (i.e. percent shortage from what is expected) vary from 0 to -.38%, with a (to the eye) apparently unremarkable distribution. 

Note that all bytes 00-0D excluding 0B are at least slightly more abundant than random chance would dictate. My guess would be that small numbers are more likely to occur as the number of repeats of a pattern. 


|Byte following 0x00 | Percent enrichment|
|-|-|
|80 | 24 |  81-83 also enriched < 1% |
|BF | 5.3 |  BB, BD-BE, also enriched.|
|9F | 5.0 |  9C-9E also enriched < 1%. |
|A0 | 2.3 |  A1-A3 also enriched < 1%. |
|00 | 2.2 |  01-08 also enriched < 1%. |
|1F | 2.1 |  1D-1E also enriched < 1%. |
|20 | 2.0 |  21 also enriched 0.16% |
|C0 | 2.0 |  C1 0.038% |




|Byte following 0x1F | Percent enrichment|
|-|-|
|00 | 65|
|08 | 5.3|
|01 | 3.1|
|10 | 3.0|
|02 | 2.0|
|04 | 1.6|
|03 | 1.5|
|05 | 0.93 |  0-09 all enriched |



Other things occasionally occur, but almost no enrichment (18: 0.62%, 40: -0.04%) 


|Byte following 0xBF | Percent enriched |
|-|-|
|FF | 32|
|1F | 1.9|
|E8,E9 | 1.3 | All DF-FC are somewhat enriched (~.5%)|
|EA | 1.0|
|3F | 0.97|
|00,04,08,09,0A  |  < 1% |
|7F | 1.4|
|5F |  0|
|9F |  0|
|18 | 1.0|




|Byte following 0x80  |  Percent enriched|
|-|-|
|1F | 68|
|08 | 1.1|
|09 | .32|
|0C | .73|
|0D,10,14,20,C0 | Minor|




|Byte following 0x04  |  Percent enriched|
|-|-|
|BF | 22|
|9F | 4.6|
|80 | 3.8|
|A0 | 3.3 | A1-A3,A5 minor|
|20 | 2.0|
|9E,BE | 1.5 | B7,B9-BC minor|
|1F | 1.5 | 1E,1D,10 minor|
|00 | 1,2 | 01-04 minor.|
|C0 | 1.0|
|5F,3F,7F | minor|




|Byte following 0xFF | Percent enrichment|
|-|-|
|0C | 8.39|
|FF | 2.7|
|00 | 2.2|
|14 | 2.6|
|24 | 1.5|
|3C | 1.0|
|F0,C0,BF,A0,9F,6C-6F |  Minor|
|5C,4C,44,2C,34 |  minor |




|Byte following 0x9F | Enrichment % |
|-|-|
|1F | 10|
|10 | 2.1|
|00-20 |  All ~ 1% except 01,02,1F-1E (<1%), 03,05-07 (<0%) |
|FF | 2.0|
|3F | 1.1|
|E0,DF,9F,A0,7F,5F, | minor|



Note: these are probably really 80 1F 00 etc... Some 1F bb bb seen in 8E3B: 

* 1F 01 81 
* 1F 00 61 
* 1F 07 41 
* 1F 01 20 
* 1F 00 80 (trice in a row) 
* 1F 00 06 (immediately following that 3x 1F 00 80) 
* 1F 28 2F 
* 1F 22 20 
* 1F 20 C1 
* 1F 05 C1 
* 1F 05 17 
* 1F 31 04 04 (if this is a run length of 04, the immediately following 04 surely would have been included in the run) 
* 1F 00 5E 
* 1F 45 1B 
* 1F 07 2B 
* 1F 02 2A 
* 1F 65 7E 
* 1F 00 80 (twice) 
* 1F 00 96 (immediately follows) 
* 1F 06 6E 
* 1F 05 3F 78 1E 28 FF 
* 1F 0D 4C 
* others 
* 1F 02 1F 09 1B - is it one or two, with the second 1F just being coincidental? 
* 1F 03 20 00  
Other observations: 1F bb bb often occur in clusters, consecutively or with small numbers of high entropy bytes intervening. No preference for inter-1F distances other than +3 is apparent, except possibly a slight preference for +4, suggesting that the command word is usually 3 bytes (nF bb bb) 

After 1F 03, a distinct preference for 20 is noted. 

Other interesting things: 

* 05 6F A9 BF 05 6F 80 1F 00 80 1F 00 80 1F 00 80 1F 00 00 06 00  
[http://sfiera.net/~sfiera/cythera/clut.html](http://sfiera.net/~sfiera/cythera/clut.html) 

It is not impossible that the color indexes might be scrambled, although there isn't really any logical reason to encrypt them, since graphical modifications would not allow the registration scheme to be bypassed, and it would add to the complexity of the decoding algorithm. 

Here are some graphics plotted with the Cythera CLUT, and their counterparts in the Pumpkin Patch: 

![](Cythera-Graphics-Working-Page/patchgraph.gif) 

Effects of replacing just one subindex 141 resource, 0x8E91, with the pumpkin patch version. Note multiple kinds of trees affected: ![](Cythera-Graphics-Working-Page/treecolor.gif) 

The resource 0x8E91. More consistent with a dictionary/table followed by callbacks to it, than with RLE. 

![](Cythera-Graphics-Working-Page/trees.gif) 
