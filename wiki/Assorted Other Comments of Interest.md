
Notes about relevant things gandreas has said about Delver's internals. 



```
The internal scripting system (which actually does all this sort of calculation) uses 24 bit signed integers (using the other bits to tell the difference between integers, different kinds of objects, pointers to strings, etc...). So 2^23-1 would have been the largest value that could be calculated.

However, the character storage record only kept 16 bits for experience, and so, in the end, 11 is the highest level that can legitimately come from experience - here's the actual code used:

rpgutil GainExp(char,amount):
oldexp = char.exp
if oldexp + amount < 0x0ffff:
char.exp = char.exp + amount
else:
char.exp = 0x0ffff
if char.exp > (1 << (char.level - 1)) * 100:
AdjCharLevel(char,1)
```
