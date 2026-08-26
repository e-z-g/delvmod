
A fragment of Delver scripting code posted by gandreas. It is as follows, with python-style indentation restored:  

```
rpgutil GainExp(char,amount):
    oldexp = char.exp
    if oldexp + amount < 0x0ffff:
        char.exp = char.exp + amount
    else:
        char.exp = 0x0ffff
    if char.exp > (1 << (char.level - 1)) * 100:
        AdjCharLevel(char,1)
```

This fragment of code was of tremendous use in reverse engineering the Delver scripting language - it would not be going too far to say that it was our [Rosetta Stone](https://en.wikipedia.org/wiki/Rosetta_Stone). Indeed that analogy goes farther than one might think -- much as cartouches with proper names allowed the hieroglyphic text of the Rosetta Stone to be aligned with the other languages on the stele, the numerical constants seen in the [GainExp](GainExp) fragment allowed the text of the program to be matched up with the bytecode. (Unlike the Rosetta Stone, where the various languages were all helpfully stuck together on one stele, the bytecode of the [GainExp](GainExp) fragment also had to be _found_ first, among the huge amount of compiled bytecode. This was also done by using the integer constants, as alluded to below.)  


## Archived Article Content

Identifying it in the script corpus would be very useful; the several candidates were advanced on the basis of being scripts containing "00 00 64" and "00 FF FF", but all of them can be identified as other things.  108E was advanced as a candidate, but later turned out to be the object scripts for a Coffer (proptype 0x8E.) Further militating against this candidate is that the resource contains 100 (0x000064) and 65535 (0x00FFFF) in wide spatial separation, and has the number 0xffff four times, not twice. The resource also seems rather longer than would be accounted for by the code above, although not knowing much about the virtual machine language at this point, we can't be conclusive. It seems likely then that the machine language can encode integer constants other than as full 24-bit signed integers. Worst case, common constants like 1 and -1 could have special opcodes to put them on the stack, as in the Java virtual machine, with no obvious numerical relationship. 

A search for resources containing 0x000064, 0x00FFFF and 0xFFFFFF (i.e. 100, 65535, and -1) returned nothing, as did a check for the same but with -1 encoded as 0x800001. 

0E8B is advanced on the basis of containing 0x64, 0x00FFFF, and indeed contains the following immediate constants (4x... opcodes):  

```
 43 00 00 FF FF (load 32 bit word 0x0000FFFF)
 43 00 00 FF FF 
 41 01
 41 01
 41 64
 41 01
 41 00 (in return block 8B 41 00 40 -- 'return 0;'?)
```

This sequence of constants is the same as the [GainExp](GainExp) fragment.  

0E8B 

```
81 02 01 
   82 00 30 62 1A 
   40 
   8D 00 31 4A 
   43 00 00 FF FF // if oldexp + amount < 0x0ffff
   4F 
   40 
   00 23 
   86 1A 30 
   40 
   30 62 1A 31 4A 
   40 
   88 00 2D 
   86 1A 30 
   40 
   43 00 00 FF FF // char.exp = 0x0ffff
   40 
   8D 30 62 1A 
   41 01       // 1 << (char.level  or char.leevl -1 
   30 62 1B 
   41 01      // char.level - 1 or 1 << 
   4B 5A 
   41 64     // * 100
   4C 51 
   40 
   00 48 
   9F 0E 86 30 
   41 01        // probably parameter char,1)
   40 
8B 41 00 40
```

See also [Delver Script Opcodes](Delver-Script-Opcodes) 
