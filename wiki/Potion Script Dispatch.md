


```
01 10 
    90 01 
       00 00 00 01                 ; Method 24

    81 01 01                       ; Method 02 (Look? Returns name of object)
       82 00                   ; local00 = ...
          45 00 B4             ;  Load 0xb4 bytes onto stack
             90 08             ;  90 nn must be analogous to A0 nn...
                90 1F 00 32    ;  Here we see 901F, with global meaning
                90 1F 00 44    ;   Possibly this is static local data for this method, only loaded 
                90 1F 00 53    ;   once into a global table? It has been determined that this is 
                90 1F 00 68    ;   loaded each time the game starts, at least.
                90 1F 00 7B 
                90 1F 00 8B 
                90 1F 00 9D 
                90 1F 00 B3 
         32: "Sustenance Potion" 00
         44: "Healing Potion" 00
         53: "Mage's Friend Potion" 00
         68: "Free Motion Potion" 00
         7B: "Antidote Potion" 00
         8B: "Clear Mind Potion" 00
         9D: "Smith's Friend Potion" 00
         B3: "Far Sight Potion" 00
         40 ; finish storing into local00
       8B   ; return stack push (...   
          00    ; push local00                   ; replacing with 00 41 03 46 40 causes them to all be called
          30    ; push arg0                         ; free motion potions (aspect 3). Also, strmode output
          62 03 ; get field3  - presumably .aspect      ;  of this method is not displayed
          46    ; probably an array get-item operation -  0x4A is arithmetical add.
          40 ; ... )
       8B    41 00   40    ; probably returns the result code 0/success

    81 01 00                        ; Method 09 (Use)
       8D    48 13 40 00 F3 "Whom should quaff potion?" 0A   
          8B    41 08   40  ; Probably tells it this needs UseOn - might also specify that it has to be on a character, as well
          8B    41 00   40 

    81 02 00                        ; Method 0A (UseOn)      ; The resources 0A00-0A07 are individual scripts mediating potion effects.
       9C    0A 00    30   62 03    40    31    63 40    40   ; call 0A00[self.aspect] (target.field40) ; or maybe 63 40 is a cast to Monster?
       A7    30    40       ;  deletes the potion (removing it causes the potion to persist.)
       8B    41 00    40    ; return OK

    A0 07 
       50 00 FF FF 00 27 
       90 1F 00 02 00 24  ; 90 certainly appears to have a different meaning here, 
       90 1F 00 08 00 02  ; here it is
       90 1F 00 D0 00 09  ; apparently associated with a global meaning (0x8000+0x101F=0x901F)
       50 00 FF FF 67 65  ; Likely the context for that meaning is the A0 nn block.
       50 00 FF FF 00 0F 
       90 1F 00 FB 00 0A
```


## Potion Scripts

0A04, The Antidote Potion. This potion effect script is called from [UseOn](UseOn) dispatch in the potion object above. 

```
 81 01 00  ; One parameter, which we know is the target's... field40, or possibly cast to something. 
    C2    30    41 09    40                  ; signal (arg, 9)   # unpoison? and is this a signal mechanism or a general method call?
    8D    30    48 05    54    40   00 2A    ; if we are the player character... otherwise skip the message
    "Very good, and satisfying."    0A 
2A: 8B    41 00    40  ; return ok
```

0A01, Healing Potion. 

```
   81 01 00 
      86 1C    30    40  ; push &character.hp
         30    62 1C     ; push character.hp
         41 0A           ; push 10
         4A              ; add
         AC   41 01   41 0A    40     ; randint(1,10) ?   
         4A              ; add
         40              ;           character.hp += 10 + randint(1,10)
      8D    30    48 05 54    40     00 33 ; if target is player character goto 0033
      "Tasty and refreshing." 0A 
33:   8B    41 00    40
```

excerpt from 0a03 free motion 

```
C2    30    41 16    40    ; clear paralysis and sleep... dunno which is which
C2    30    41 0E    40 
8D 30 48 05 54 40 00 3D ; skip message if not pc, yada yada
```

business end of far sight 

```
E7    41 02    40
```

smith's friend 

```
C3    30    41 17    41 64    41 0A   ;  What is difference between C3 and C2? num of args?
      AC    41 01    41 0A    40      ; rand(1,10)
      4C 
      4A 
      40    ; something3(target, 0x17, 100+10*rand(1,10))
```

sustenance  

```
   86 28    30    40    41 18    40   ; character.nutrition = 24 # n.b. not adding!!
```

clear mind 

```
C2    30    41 15    40   ; signal(character, 0x15)  or a method call?
```

mage's friend excerpts  

```
local1 = randint(1,10)+10
if target.field1E == target.field1F: goto 003D  # == == 0x54?
if not player character: goto 003A
"Nothing seems to happen"
003A: goto end:
003D:
     if target.field1F - target.field1E <= ? local1: goto 00 54
     local1  = target.field1F - target.field1E 
     if local1 (0x51) target.field1C: goto 0066
     local1 = target.field1C - 1 
0066:if local1 (0x51) 0: goto 00B7
     if not is player character: goto A0
     "you experience a brief pain and weakness." 0A
00A0: 
     target.field1E += local1
     target.field1C -= local1
     goto 00D8
00B7:
     if not is player character: goto end
     "Nothing seems to happen." 0A
0054:
    "Nothing seems to happen"
end: return
```
