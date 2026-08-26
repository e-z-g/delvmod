
Analysis of 1A00. This is the script for the spell-skill Directed Nexus. [List of Spells](List-of-Spells) appears to be in native order, going by Selax's work on this subindex. 

The strings seem to either be 00 or 0A terminated, with both terminations appearing in these resources. 



```
  0: 00 F9            
This integer appears to point to the very next byte after the last script.

  2: 90 01 00 00 00 00  
Header for a script?

  8: 81 01 00 8B 44 44 69 72 65 63 74 65 64 20 4E 65 78 75 73 00 40 8B 41 00 40
                    D  i  r  e  c  t  e  d     N  e  x  u  s
A script of the 81...40 type, containing a string.

 21: 90 02 00 00 00 01 50 00 FF FF
Header? Contains the popular 80,-1 sequence following.


 2b: 81 01 00 This spell creates opens a portal to a specified location, which will instantly transport you and your party to its nexus point in LandKing Hall 0A 8B 41 00 40
A script (mistake - "creates opens" - not mine)

 c4: 81 01 00 8D 9F 0E A1 30 62 0B 41 01 41 01 40 40 00 F5 E1 48 09 63 00 43 00 00 00 F0 40 D3 41 30 48 09 62 01 48 09 62 02 40 BF 41 01 41 01 41 00 40 8B 41 00 40
A script (method?) follows immediately without a header this time.

 f9: A0 07 50 00 FF FF 
The start of this sequence is pointed to by the integer at the start.

 ff: 06 95 9A 00 00 2B 00 08 9A 00 00 08 00 02 9A 00 00 21 00 33 9A 00 00 C4 00 09 9A 00 00 02

11d: 00 36 50 00 FF FF 06 96
```



```
100D, end table
00 02 
A0 03     50 00 FF FF 00 24      50 00 00 01 00 25      50 00 FF FF 00 1A

1089, sandals              
00 0E     90 01 00 00 00 02      90 01 00 00 00 08 
A0 03     90 89 00 02 00 24      50 00 FF FF 00 24      90 89 00 08 00 26

1088, cloak
00 14     90 01 00 00 00 0A      90 01 00 00 00 09      90 01 00 00 00 01 
A0 07     50 00 FF FF 00 27      90 88 00 02 00 24      90 88 00 0E 00 2C 
          90 88 00 08 00 26      50 00 FF FF 6A 65      50 00 FF FF 00 0E 
          50 00 FF FF 61 6D


1098, lute
00 52    90 01 00 00 00 06 
         81 01 01 8D DB 30   40   40   00 16   8B 41 00 40 
         82 00 9B 04 30      41 12     41 01   41 18   41 5A   41 34   40   40   9B 0F 00 
            41 00   41 00    41 5A     41 34   41 19   45 00 16 
               90 05   00 00 00 0F   00 00 00 0C 
                       00 00 00 09   00 00 00 06 
                       00 00 00 03 
            40   8B 41 00 40 
A0 03     90 98 00 02 00 24       90 98 00 08 00 09     50 00 FF FF 2E 42



1099, panpipes
00 BB     90 01 00 00 00 02      90 01 00 00 00 08      
   @E:    81 01 01 8D DB 30   40   40   00 1C   8B 41 00 40 
   @1C:   82 00 9B 04 30 
             41 12   41 00   41 16   43 00 00 00 A0   41 61   40 40 8D 30 62 06 
             41 01   54 40 00 67 9B 0F 00   41 00     41 00   43 00 00 00   A0   41 61 
             41 4C   45 00 16    
                  90 05       00 00 00 0F    00 00 00 0C    00 00 00 09 
                              00 00 00 07    00 00 00 03 
             40   88 00 91 9B 0F 00   41 00   41 00    43 00 00 00 A0   41 61   41 4C   
             45 00 16 
                  90 05       00 00 00 0F    00 00 00 0C    00 00 00 09 
                              00 00 00 06    00 00 00 03 
             40    8B 41 00 40 
    @95:  81 02 00 8D 31 
             43 00 0F FF FF    56    43 00 0F 79 C3     54    30 62 06 
             41 01    54 5C   40   00 B7 C5 
             43 00 00 00 81   40    8B 41 00 40 
A0 07     50 00 FF FF 00 2A      90 99 00 02 00 24      90 99 00 0E 00 09        This may be a jump table. 00 0E and 00 95 are offsets of 81...40 scripts.
          90 99 00 95 00 0A      90 99 00 08 00 27      50 00 FF FF 00 28        (????) offset-in-resource  message-type?/method-id?
          50 00 FF FF 00 30


109A, lyre
00 7B     90 01 00 00 00 04 
    @8    81 01 01 8D DB 30     40   40   00 16    8B 41 00 40 
          82 00 9B  04 30       41 14   41 61   41 48   41 55   43 00 00 00 A7 
            40   40   9B 0F 00  41 00   41 00   41 55           43 00 00 00 A7 
                                41 2F   45 00 1A 
            90 06 
               00 00 00 12   00 00 00 0F   00 00 00 0C 
               00 00 00 09   00 00 00 06   00 00 00 03 
            40   8B 41 00 40 
          81 02 00  8D 31    43 00 00 0F FF   56   43 00 00 0F C6   54 
            40  00 77 C5     43 00 00 00 83   40   8B 41 00 40 
A0 07
          50 00 FF FF 00 2A    90 9A 00 02 00 24   90 9A 00 08 00 09 
          90 9A 00 5C 00 0A    50 00 FF FF 00 27   50 00 FF FF 00 28 
          50 00 FF FF 00 30

```



```
0241, death text      -  There is no offset to the table here, instead the table is first.
90 02                  // two things follow
     82 41 00 0A       // A string at 000A
     82 41 01 85       // A string at 0185
(the strings follow immediately.) 

0203, character class names
90 09 
     82 03 00 26     82 03 00 2F  
     82 03 00 37     82 03 00 41 
     82 03 00 4A     82 03 00 4F 
     82 03 00 56     82 03 00 5D 
     82 03 00 69 
Strings follow immediately, densely packed cstrings starting at 26, 2F ... 69.


0201, character names
91 00  
     91 65 04 02     91 65 04 04     91 65 04 09
     ...
     91 65 09 F1     91 65 09 F5  
CStrings follow immediately at 0402, 0404, 0409 ... 09f1, 09f5.

0219, scroll text
90 0D
     82 19 00 36     82 19 00 37     82 19 00 84 
     82 19 00 F4     82 19 01 8F     82 19 01 D1 
     82 19 02 80     82 19 03 16     82 19 05 94 
     82 19 07 A9     82 19 08 B0     82 19 09 4D 
     82 19 0A 6A
Packed strings follow immediately (including one at 36 which is just a NUL).
Interesting how this is clearly some kind of global table being populated (0219 / 8219)
in 2019 and 0203, but 0201 is different... (9165, not the expected *8201)
```

Dialogue (no null terminator implied by quotes) 

```
00 D9 
  81 01 00 "You see a very serious looking guard" 2A 8E 
        90 "job" 
          00 00 5D "\"I guard Alaric here in LandKing Hall.\"" 
          88 00 2B 
        90 "bye" 
          00 00 7F "\"Goodbye, stranger.\"" 
        8B 41 00 40 
  
  88 00 2B 
        90 2A 
           00 00 D2   8D 9F 08 09 30   40   5E   40   00 CF 
                      8D 9F 08 01 30   40   5E   40   00 CF 
                      "\"I am just a guard, and not permitted to talk of such.\"" 
  88 00 2B 
  88 00 2B   
        8B 41 00 40 
A0 03 
  98 07 00 02 00 0C    50 00 FF FF 00 0C    50 00 FF FF 00 20
```

Excerpt from 180A 

```
88 02 AC "\"Ah, you must be the mysterious hero"
   8D 49 05 00 00   10   40   00 F3 "ine I've heard so much of.\""
```
