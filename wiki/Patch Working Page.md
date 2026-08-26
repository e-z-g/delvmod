
Mysterious resource FFFE: 

```
0000: 00 B2 1E 58 A4 7F 11 D4          8A 4A 00 05 02 C9 F8 B7
```

The same 16 bytes are found from 0x08 to 0x17 (16 bytes) in FFFF. Possibly FFFE is a list of applied patch checksums or signatures? 

FFFF begins with the following 8 mysterious bytes: 

```
C4 9B A9 81 07 78 A4 B9
```

}

Then follows the copy of the FFFE 16 bytes, and then  

```
02 38 03 00 00 00 D7 06 00 00 00 00 01 00 80
```

After many zeros, a pascal string begins at 0x138. The resource has enough zeroes after the string for a length-255 pstring. 

Mutations: Changing one letter of the text description causes the patch not to be recognized by magpie, with no comment from the program. Changing one byte elsewhere does not produce this result, or at least not in the two tested cases, but optimizing the file with [Narthex](Narthex) Resulted in an unrecognized file. 

My conclusion is that the special patch resource (FFFF) and possibly the master index and one other thing, but not the data itself, have checksums applied. 

Since Magpie doesn't have any capabilities that Narthex / delv couldn't be easily adapted to do, there is no particular reason to bother figuring this out. 
