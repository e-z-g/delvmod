
These resources are very heterogeneous and low-entropy. Their purpose, if indeed they have a common purpose at all, is not clear at this time. Some of them appear to be strings that might involve the interface or other things, others might be memory images for the scripting virtual machine. Some are lists of strings.  

[Narthex](Narthex) used to become confused by some of these resources, thinking they are encrypted when they are in fact not. This is because their resource IDs lead to a degenerate case of the random number generator, causing all bytes 00 to be converted to the same value. Namely: F004, F00C, F014. Thus the entropy doesn't appear to change and Narthex defaults to guessing (wrongly) it is encrypted. 

Resources [F013](Composed-Tile), [F010](F010), [F009](F009), [F008](F008), [F004](F004), [F002](F002) and [F000](F000) have their own articles. 



```
 ---- SUBINDEX 239 ---- 
Index 0, ID F000 Length: 2048 bytes      Relates prop types to tiles. An array of 2-byte integers that are tile IDs. 
Index 1, ID F001 Length: 66 bytes          Appears to contain 33 2-byte integers.
Index 2, ID F002 Length: 32768 bytes     Tile attributes (walkability, etc). 8192 4-byte records (first 0x1000 apply to simple tiles, last 0x1000 to compound.)
Index 4, ID F004 Length: 5786 bytes      Contains tile names.
Index 5, ID F005 Length: 16 bytes          Possibly five 3-byte records followed by a null terminator.
Index 7, ID F007 Length: 167 bytes       A two-byte integer, 0x21 (=33), followed by 33 five-byte records. 
Index 8, ID F008 Length: 2048 bytes      Contains monster stats
Index 9, ID F009 Length: 16384 bytes       Global props
Index 10, ID F00A Length: 1024 bytes       All zeros.
Index 11, ID F00B Length: 5448 bytes       681 8-byte records, no visible length or terminator, some of which (not including the last) are zeros.
Index 12, ID F00C Length: 4096 bytes       Slim evidence favors 2-byte records. Very high entropy. The last nonzero record is the 382nd of 2048. Might have Tile IDs.
Index 13, ID F00D Length: 500 bytes        166 3-byte records consisting of a short and a char. The list is terminated by 0x0000 (n.b. not 0x0000 0x00)
Index 15, ID F00F Length: 1024 bytes       Probably an array of bytes. The values 00, 0E, 01-04 are the only seen. (All bits in the lower nybble.)
Index 16, ID F010 Length: 16384 bytes    Contains faux prop information (1 bit rotation, 5 bit aspect, 10 bit prop type) for each of 0x2000 the tiles, indexed by tile ID.)
Index 17, ID F011 Length: 32768 bytes    Prop X offsets, in pixels, 1 byte per each of 32 aspects
Index 18, ID F012 Length: 32768 bytes    Prop Y offsets, same format as F011
Index 19, ID F013 Length: 131072 bytes   Composed Tile information
Index 20, ID F014 Length: 123 bytes        Unterminated list of {short, null terminated string} pairs of varying length. Possibly interface related ("_WindWidth")
Index 21, ID F015 Length: 179 bytes        Same format is F015, strings of very unclear purpose "Od_Trough1" and so forth, "Bellows" "Shutter" "Candle". May relate to the StoreRef field of props - debugging symbols?
Index 22, ID F016 Length: 8192 bytes       No obvious structure, bytes are all 00 or 8x.
```


## F015 Entries


|0008 | Cad_Bellows1|
|-|-|
|000A | Cad_Candle1|
|000B | Cad_Candle2|
|000C | Cad_Candle3|
|000D | Cad_Candle4|
|0009 | Cad_Trough1|
|0006 | Od_Bellows1|
|0003 | Od_Candle1|
|0004 | Od_Candle2|
|0005 | Od_Candle3|
|0001 | Od_Shutter1|
|0002 | Od_Shutter2|
|0007 | Od_Trough1|



In order of storage reference: Od_Shutter1, Od_Shutter2, Od_Candle1, Od_Candle2, Od_Candle3, Od_Bellows1, Od_Trough1, Cad_Bellows1, Cad_Trough1, Cad_Candle1, Cad_Candle2, Cad_Candle3, Cad_Candle4 
