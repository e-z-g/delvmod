
_This page concerns the [81 ... 40 Script Type](81-...-40-Script-Type), seen in subindices 8, 13, possibly 15, and many others._ 

This describes Cythera's dialogue tree format, i.e. the prompts and responses that characters give you during conversation.  

Prompts are typically four characters long and case insensitive; e.g. you can type "prop" for "Propontis" (Saves time when playing the game once you know about it! Also, this works on the password-protected doors in Pnyx, if you don't want to remember the whole word.) 

The data format is somewhat unusual for its purpose, and probably represent a compiled script for the scripting system. Hopefully, as the technical documentation project continues, exploration of the known scripts will ultimately prove illuminating. Until then, this page just describes it in isolation. 


### Preamble

Each resource begins with an identical preamble: 

```
81 01 00
```


### Prompt Strings

Each response begins with the byte 0x90. Following this byte is a comma-separated list of prompts, as a NUL-terminated ASCII string. For example, in the shared dialogue of the indigenous Seldane ([Cythera Data](Cythera-Data) subindex 7, 0x080F), the following are the set of prompts for "Magpie" (or his original Seldane name): 



```
90 6D 61 67 70 2C 62 61 68 6F 00                .magp,baho.
```

The prompt strings can be less than four bytes, for example, the prompt for "air" (I.e. the classical element) in the same resource: 



```
90 61 69 72 00                                     .air.
```

An apparent error in resource 080F is illuminating, as errors often are when approaching an unknown form of communication. Seldane are evidentally supposed to respond to "corr[uption]" in the same way as they respond to "crol[na]". (Offset 0xC6). However, there is a typo, and the string reads: 



```
90 63 72 6F 6C 2C 20 63 6F 72 72 00                .crol, corr.
```

Instead of the expected: 



```
90 63 72 6F 6C 2C 63 6F 72 72 00                .crol,corr.
```

The Seldane in the game do not respond to "corr" or " cor". They respond, however, to " corr", i.e. "corr" with a space in front of it, demonstrating that you can have dialogue keys exceeding four characters. At this time, the maximum length is not known, nor is it known if the keys must be unique in the first four characters. (E.g. would it be possible to distinguish between "Hippostratos" and "Hippokrates"?) 


### Response Strings

Following is a two byte short integer, which contains the offset in the resource of the next prompt string (i.e. the stuff that begins with 0x90). In the case of the last prompt-response pair in the dialogue file, it points to an ending block (described below) without a prompt string preceeding it.  

Typically, the response follows directly, e.g: 

```
"Dangerous, and lost."
```

The response can be multiple lines; for example, when you ask a Seldane about their old city, Maayti, you get a response which is divided into two replies: "Maayti, city of Truth, was our home." and "Now we are here, and around Maayti the land sank, becoming a swamp." You have to click to get to the next one. These lines are separated by '*' characters, e.g: 



```
"Maayti, city of Truth, was our home."*"Now we are here, and around Maayti the land sank, becoming a swamp."
```

Naively, the strings appear to be terminated by 0x8B. This would be a strange choice of terminator (it corresponds to "ã" in the Mac OS Roman) and indeed it does not appear to be a terminator. It could be simply that a non-printing or non-ASCII character signals the end of the string, or whatever is interpreting the format does so by matching the quotation marks, and knows that a quotation mark followed by something other than an '*' (which would indicate another line to follow) means that it is done. It would be helpful to consider, e.g. the response to "demo"[docus] in resource 0x080C or others in which the famous bard is mentioned. 

This stuff following the response string is almost certainly compiled scripting language code. Our understanding of this scripting language is currently not even rudamentary. However, the following virtual machine code is what is necessary for a simple line of dialogue that does not change anything, i.e. it is just an informational response: 



```
8B 43 50 00   00 01 40
```

The final item in the resource ends with: 



```
8B 43 50 00   00 00 40   8B 41 00 40
```


## Work in progress - Decoding the Demodocus prompt-response item



```
0070: -- 90 64 65 6D 6F 00 01 0D 8D DC 41 04 40 41 04 
             d  e  m  o

0080: 54 40 00 8A DD 41 04 41 06 40 8D DC 41 04 40 41 

               _____
0090: 06 54 40 00 D2 22 44 65 6D 6F 64 6F 63 75 73 20 
                      "  D  e  m  o  d  o  c  u  s  

00A0: 70 65 72 66 6F 72 6D 65 64 20 68 65 72 65 20 72 
       p  e  r  f  o  r  m  e  d     h  e  r  e     r

00B0: 65 63 65 6E 74 6C 79 2C 20 62 75 74 20 49 20 62 
       e  c  e  n  t  l  y  ,     b  u  t     I     b

00C0: 65 6C 69 65 76 65 20 68 65 20 6C 65 66 74 22 88 
       e  l  i  e  v  e     h  e     l  e  f  t  "

offs  _____ D2
00D0: 01 06 22 57 65 20 68 61 76 65 6E 27 74 20 73 65 
             "  W  e     h  a  v  e  n  '  t     s  e

00E0: 65 6E 20 44 65 6D 6F 64 6F 63 75 73 20 61 72 6F
       e  n     D  e  m  o  d  o  c  u  s     a  r  o 

00F0: 75 6E 64 20 68 65 72 65 20 66 6F 72 20 61 20 77
       u  n  d     h  e  r  e     f  o  r     a     w 
offs                   106
0100: 68 69 6C 65 2E 22 8B 43 50 00 00 01 40 -- -- --
       h  i  l  e  .  " 

```

What is really curious here is that the "next string" pointer points to the beinning of the string, not the "offset of the next string" information as one might expect... 
