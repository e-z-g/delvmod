
The corpus consists of 40 small files, ranging in size from 7 to 805 bytes. It is likely that the small entries represent something the minimum script in the [81 ... 40 Script Type](81-...-40-Script-Type). 



```
 ---- SUBINDEX 47 ---- 
Index 0, ID 3000 Length: 31 bytes

Index 1, ID 3001 Length: 7 bytes

Index 2, ID 3002 Length: 14 bytes

Index 3, ID 3003 Length: 11 bytes

Index 4, ID 3004 Length: 51 bytes

Index 5, ID 3005 Length: 33 bytes

Index 6, ID 3006 Length: 7 bytes

Index 7, ID 3007 Length: 252 bytes

Index 8, ID 3008 Length: 75 bytes

Index 9, ID 3009 Length: 7 bytes

Index 10, ID 300A Length: 7 bytes

Index 11, ID 300B Length: 7 bytes

Index 12, ID 300C Length: 39 bytes

Index 13, ID 300D Length: 7 bytes

Index 14, ID 300E Length: 7 bytes

Index 15, ID 300F Length: 583 bytes

Index 16, ID 3010 Length: 7 bytes

Index 17, ID 3011 Length: 7 bytes

Index 18, ID 3012 Length: 14 bytes

Index 19, ID 3013 Length: 14 bytes

Index 20, ID 3014 Length: 7 bytes

Index 21, ID 3015 Length: 88 bytes

Index 23, ID 3017 Length: 14 bytes

Index 24, ID 3018 Length: 14 bytes

Index 25, ID 3019 Length: 28 bytes

Index 26, ID 301A Length: 154 bytes

Index 27, ID 301B Length: 7 bytes

Index 28, ID 301C Length: 172 bytes

Index 29, ID 301D Length: 39 bytes

Index 31, ID 301F Length: 190 bytes

Index 32, ID 3020 Length: 805 bytes

Index 33, ID 3021 Length: 19 bytes

Index 53, ID 3035 Length: 7 bytes

Index 57, ID 3039 Length: 27 bytes

Index 61, ID 303D Length: 7 bytes

Index 62, ID 303E Length: 14 bytes

Index 64, ID 3040 Length: 275 bytes

Index 65, ID 3041 Length: 362 bytes

Index 66, ID 3042 Length: 654 bytes

Index 67, ID 3043 Length: 161 bytes

```


### 7-byte Subindex 47 Resources



```
3001, 3009, 300D, 300E, 3010, 3011, 3014, 3035:
    81 01 00               SubXXXX(arg1):                        
    8B 41 00 40                return 0 # Maybe this is returning none? What is the calling convention?



3006, 300A, 301B, 303D:  
    81 02 00              SubXXXX(arg1,arg2):            
    8B 41 00 40               return 0

300B:
    81 03 00              SubXXXX(arg1,arg2,arg3):
    8B 41 00 40               return 0

```

=== 11-byte ===  

```
3003:
    81 01 00            Sub3003(arg1):
    8B 41 00 40             return 0  # Maybe it has a side effect on the return stack?
    8B 41 00 40             return 0 ??
```


### 14-byte Subindex 47 Resources



```
3002: 
    81 01 00                   Sub3002(arg1):
    8B 43 50 00 FF FF 40           return 0x5000FFFF, 0
    8B 41 00 40                    

3012, 3013, 3018:
    81 01 00                   Sub30xx(arg1):
    8B 43 50 00 00 01 40           return 0x50000001, 0
    8B 41 00 40

3017, 303E:
    81 02 00                  Sub30xx(arg1,arg2):
    8B 43 50 00 00 00 40           return 0x50000000, 0
    8B 41 00 40
```


### 19-byte subindex 47 resource 3021



```
    81 05 00                                  Sub3021(arg1,arg2,arg3,arg4,arg5):
    8B                                            return Sub9C0C??(arg2)(arg1,arg3,arg4,arg5), 0
       9C 0C 00 31 40 
         30 32 33 34    40 40           
    8B 41 00 40
```


### 27-39 bytes and selected longer ones



```
3039: 27 bytes                                
    81 01 00                           Sub3039(arg1):                     
    You can't dig here! 0A                 print "You can't dig here!"
    8B 41 00 40                            return 0
300C:
    81 01 00      
    You are met with stony silence. 0A                           
    8B 41 00 40

3019: 28 bytes
    81 01 00
    8D 30 60 27 40 00 18 
    8D 30 61 27 00 41 10 56 40 00 18 A7 30 40
    8B 41 00 40   

3000: 31 bytes
    81 01 01
    8D 30 64 48 5E 40 00 1B
    82 00 30 63 48 40 
    8D 00 40 00 1B 9D 00 00 30 40
    8B 41 00 40


3005: 33 bytes 
    81 03 02
    8D 30 64 00 00 40 00 1D 
    82 00 30 63 00 40 
    82 01 00 62 12 40 
    84 01 40 31 40 32 40
    8B 41 00 40

301D: 39 bytes
    81 02 01
    8D 02 01
    8D 30 64 40 40 00 1E
    82 00 30 63 48 40   
    8D 00 40 00 1E 9D 1D 00 30 40    
!   8B 41 00 40 9F 0E                  
    8D 31 40   
    8B 41 00 40

3008:
    81 01 00   
    8D 30 63 40 40 00 2A 9F 0E 48 30 
    44 
    They are carrying 00
    43 50 00 00 00 40
    88 00 47 9F 0E 48 30 
    44 
    Searching Reveals 00 
    43 50 00 00 01 40     
    8B 41 00 40


301F: 
    81 02 01   
    82 00 30 63 48 40   
    8D 41 FB 31 50 31 41 FE 50 5C 40 00 65   
    8D C4 30 41 1F 40 5E 00 62 32 41 40 56 41 00 54 5C 40 00 62 
    8D AC 41 01 41 0A 40 41 03 54 40 00 62 
    86 26 30 40 
    44 
    Ouch! Something bit me! 00 
    40 C1 30 41 09 40 9D 41 30 41 01 41 02 40 
    88 00 BA    
    8D 31 42 FF 23 54 40 00 AF   
    8D C4 30 41 17 40 5E 00 62 32 43 00 00 00 
    80 56 41 00 54 5C 40 00 AC 
    86 26 30 40 
    44 
    Ouch! That's hot! 00 
    40 
    9D 41 30 AC 41 00 41 04 40 41 01 4A 41 08 40 
    88 00 BA 
    82 31 31 63 00 40 9D 0A 31 30 40 
    8B 41 00 40
  
```

Long test example 3041 

```
81 03 04 
82 00 30 63 
40 
40 
8D 00 
40 01 66 E3 30 62 01 30 62 02 43 00 00 01 B2 
40 C2 00 41 16 40 
8D C4 00 41 0E 
40 
40 00 3A 
8D AC 31 41 14 4A 40 31 4F 40 00 3A C2 00 41 0E 40 
82 01 30 63 48 40 
82 02 43 50 00 FF FF 40 
8D 30 60 3B 40 00 59 
82 02 30 61 3B 00 40 
88 00 
8E 
8D 01 60 3B 40 00 6A 
82 02 01 61 3B 00 40 
88 00 
8E 
82 02 45 00 1E 90 07 00 00 00 00 00 00 00 10 00 00 00 11 00 00 00 13 00 00 00 14 00 00 00 15 00 00 00 16 40 
8D 31 00 62 1C 52 40 00 C9 
"-- ^" 
8A 00 40 
" Killed! --" 0A
82 03 02 41 06 46 40 
8D 03 40 00 BF D3 03 30 62 01 30 62 02 40 
86 1C 00 40 41 00 40 88 01 66 86 1C 00 40 00 62 1C 31 4B 40 
8D 00 62 1C 00 62 1D 41 04 4D 50 40 01 09 
82 03 02 41 05 46 
40 
"-- ^" 
8A 00 
40 " Critically wounded!-- " 0A 
88 01 3B 8D 00 62 1C 00 62 1D 
41 02 4D 50 40 01 34 82 03 02 41 04 46 40 "-- ^" 
8A 00 
40 
" Wounded -- " 0A 
88 01 3B 
82 03 02 41 03 46 40 
8D 03 40 01 49 D3 03 30 62 01 30 62 02 40 
8D 32 43 00 00 01 00 56 40 01 66 
8D 01 62 32 41 40 56 40 01 61 
88 01 66 C1 30 41 09 40 
8B 41 00 40

```
