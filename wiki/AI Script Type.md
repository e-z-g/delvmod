
The data format, probably a compiled script, seen in at least [Cythera Data Subindex 4](Cythera-Data-Subindex-4). It is different from the [81 ... 40 Script Type](81-...-40-Script-Type) that represents Delver virtual machine code. It seems to have 8-byte instructions or at any rate some kind of repeating structure every 8 bytes, including many nulls, which is very different from the [81 ... 40 Script Type](81-...-40-Script-Type)'s high density code.  

Cythera comes with a variety of uncompiled AI scripts, with names corresponding to the names seen in Subindex 4. Undoubtedly, a productive line of investigation would be to examine how these text files correspond to compiled scripts. 

Resource 0430: (The "Attack Nearest" script.)  



```
NAME "Attack Nearest"
; If somebody else is attack me, 75% of the time attack them
IF HasMeleeWeapon(myself) THEN
IF Exists(myself.LastAttacker) THEN
IF NOT IsTarget(myself.LastAttacker) THEN
IF InRange(myself.LastAttacker,2) THEN
        #75             SetTarget(last)
                        DoAttack()
        #25             Continue()

IF Exists(enemy.ByRange.Pick) THEN
        #100    SetTarget(last)
                        DoAttack()

; no enemy exists at this point...
IF True() THEN
        #100    FinishCombat()
```

Attack Nearest script above copyright 1999 Ambrosia Software, inc. 

This script is chosen because it contains three different probability literals (#25, #75 and #100, base 10, i.e. hex 19, 4B, 64) to look for in the compiled code.  

These scripts all begin with a Pascal-string (length byte followed by that many characters) naming the script: 

```
0E 41 74 74 61 63 6B 20 4E 65 61 72 65 73 74
15  A  t  t  a  c  k     N  e  a  r  e  s  t
```

(As a bit of trivia, it was this subindex that allowed the whole [Delver Archive](Delver-Archive) format to be interpreted, because each resource begins with such a recognizable data type.) 



```
From Attack Nearest
                     _____
0E 06 00  05 0D 00   00 64   82 F3 00 00 00 00 00 00 8B
        ____
        #100    FinishCombat()

                                            _____
10 00 00 00 65 0A F0 02 10 00 00 10 00 00   00 4B   82 F3 00 00 00 00 00 00 8B 00 00
        ___
        #75             SetTarget(last)
                        DoAttack()

                           _____
00 00 8B 00 00 00 00 00    00 19    01 00 00 00 00 00 00 65 0E 06 00 05
        ___
        #25             Continue()
```



```
From Attack Strongest

_____
00 64    82 F3 00 00 00 00 00 00 8B
        ____
        #100    FinishCombat()
```
