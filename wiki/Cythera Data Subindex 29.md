
There is one resource, a script, 1E20. 

```
00 14 
   81 01 00 
      BF 
         41 0D 
         43 00 00 00 92 
         41 00 
      40 

      8B 
        41 00 
      40 

A0 03 
   50 00 FF FF 61 31 
   50 00 FF FF 74 6E 
   9E 20 00 02 00 14
```

It would appear that this object changes the player's position in response to a method call (0x14), which transports the player to the Tree of Life region (92). Highly mysterious! 
