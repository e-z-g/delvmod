

|**Value** | **Comment**|
|-|-|
|0x0 xxxxxxx |  28-bit signed integer|
|0x1 xxxxxxx |  Pointer?|
|0x2 xxxxxxx |  String of Global (at least 0x200000xx). Doesn't seem to work properly for non-string globals. Unclear what the point is; doing arithmetic on them does not seem to be possible. How to store in globals?|
|0x3 iii rrrr |  Resource rrrr, index entry iii (not sure if non-array resources can be loaded)|
| You can add or subtract from the resources word to index it. e.g. 43.3.019.0219 41.01 4A  -> resource 0219, array index 0x19+1||
|0x404000 cc | Character cc. Can it retrieve from other proplists in theory? | E.g. 0x40400001 is the player character.|
|0x5 000 0000 |  False value|
|0x5 000 0001 |  True value|
|0x5 000 FFFF |  None value|
|0x6 xxx xxxx |  Crashes interpreter for x=0|
|0x7 xxx xxxx |  Crashes interpreter for x=0|
|0xrrrr ffff |  Resource rrrr-0x8000, offset ffff|




### 0x20.xxxxxx

(414, '1860.bin', 52, '1') 

0x43 20 00 00 01 - time of day (see 48 01 push global "morning", "evening" etc string time of day) 


### Unraveling 0x40xxxxxx



```
1025 - Using Crolna on Alaric

10E5 - Guard object. 
Method_000C(self): 
   local0 = 0x40400064  ; 0x0064 - "Gate Guard"
   call_method 0x0c (local0)
   return 0


1B11 - Finding a secret tunnel in the wall of LKH.
Hector is retrieved with 0x40400006 to comment.

1B5E - The "Look! A path to the NW!" script. An object.
Hector is retrieved with 0x40400006

1BCA - 0x40400061 (Aethon "Smells like money!")

3043, 301C - Unidentified functions.
It checks to see if its first argument is the hero using 0x40400001. 


40 is the cast value for casting to characters... perhaps some kinds of objects are "registered" and can be retrieved like this?
Or is this retrieving from the prop list, and 40 is just telling it what class to return it as?

40 does appear to be the type to return it as, but it also may change which list it is retrieved from; it's unclear. I tried 40480006 and got 'something (48/06)' I tried 40000006 and got 'Hector' (presumably as a prop). 



```
