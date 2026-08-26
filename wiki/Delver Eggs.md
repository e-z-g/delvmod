
Working notes. 

```
Aspect seems to be the egg type.
Flags, aspect, PT, D3
kosha.
0x42 8 0x142 0x0204 - room script 1C42
0x42 8 0x13A 0x0205 - room script 1C3A (room scripts start at 1B00)
overworld.
0x42 0 0x000 0x1414 - egg with titans in it
0x42 0 0x003 0x0146 - egg with polyp in it
omen's test
0x42 1 0x09E  0x0000 - teleporter egg
0x42 1 0x09B  0x0000 

Aspect 6 - switch egg - sends its proptype field as a signal (at least the 14xx zone object can receive it.) D1/D3 probably relate triggering conditions.
Example in tyrant's tomb / 1419 -- making rocks visible/interactable (0x80 -> 0x00 flags.)
```



---

 

Egg in odemia 566,  

Object type = 0x0E4 (same as chicken) What determines if it is a one-shot egg? 

d1 = ??? d2 = Percent chance to occur? 

aspect = 0 

Contents: Prop type = kind of monster. d1 = ai type or flags?  d2 = quantity of this monster to produce. 


|**AI Type** | **Effect** | **Combat?**|
|-|-|-|
| 0  |  Do nothing?  |  No |
| 6  |  Look for trouble  |  Yes |
| 8  |  Stand guard  |  Yes |
| 10  |  wander randomly (about origin?)  |  No |
| 15  |  pace horizontally  |  No |
| 16  |  pace vertically  |  No |


