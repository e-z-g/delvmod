


```
 ---- SUBINDEX 0 ---- 
Index 1, ID 0101 Length: 1246 bytes
```

This resource appears to be a table with 127 entries. It is direct mode script data of a `table`. It differs from most symbol tables by containing a tremendous number of redundant entries (`0: None`) which might suggest that the position in a symbol table is significant somehow, contrary to earlier thinking. The table associates some of its keys with strings which appear to be symbol names. A particularly curious question is why some keys are followed immediately by another entry with "None" as the value, for example: 



```
    81030324 3026
    5000FFFF 3026 
```

It may be that the table is out of date, only for some half-implemented debugging purpose and it offers little information except for giving the symbolic names of various things otherwise only known to us by a number (e.g. names of methods.) 

The items in the table below fall into four series: 02xx, 16xx 17xx, and 30xx. It has been conjectured, chiefly since 0201 is indeed the resource ID of the character names array, that the 02xx entries are the names of global variables. Unfortunately, 0200 does not contain tile names (they are in F004, in fact), and the test of signs is in 0218. Another problem for the hypothesis is that 16xx and 17xx are not valid resource IDs for Cythera Data. (Itself a bit curious, since 15xx and 18xx _are_, and the resource types are generally densely packed under 3000 with only one other exception. 

In the case of the 16xx names: 


|1664 | [DisplaySign](DisplaySign)|
|-|-|
|1665 | [DisplayScroll](DisplayScroll)|
|1666 | [DisplayContainer](DisplayContainer)|
|1667 | [DisplayInstrument](DisplayInstrument)|



While there are no 16xx resources, the resource called to display a paper calls both (under different circumstances) 0E64 and 0E65. Musical instruments seem to display themselves without calling a helper script, with lots of 9B oo series GUI operations. Crates do call 0E66 (as well as 0E41 and 0E48). While tantalizing, it is quite unclear what, if any connection there could be here - if anything it seems to support the thesis that 0101 is "dead" debugging symbol data, and that at one time in the past the helper scripts that now live in 0Exx lived in 16xx.  


|1711 | deckarma|
|-|-|
|1712 | inckarma|
|1706 | curepoison|



The 17xx series can have identifications made with the 0Fxx resources analogously, although the identification is at this point very tentative, based chiefly on 0F11 and 0F12, which do indeed appear to be decrementing and incrementing a global variable. Further research is needed, especially in relation to e.g. 0F06, which very much does not appear to cure poison. (The antidote potion does not call it, and it does not contain C2(30,41 09)40 / `clear_bit (arg0, 9)` or something to that effect - perhaps it is fossil code, with poison having been implemented differently. The 0f06 script says character.field14 &= 0xFFFFFFD, which does indeed appear to be clearing a flag. Perhaps the opcode C2 was added later and these are equivalent, but 9 seems an extremely odd way to encode the bitmask used to clear poison (conjecturally) in 0F06. The bit cleared has the value 2, its position is at 1 from the LSB or 26 from the MSB.) 

I tested manually manipulating field14 (modified the shovel to bitwise OR it with 2) and found that it did indeed poison the character, so the probable situation here is that the opcodes C1/C2 i.e. setbit/clearbit became available later and this helper script was previously used. writing setbit(character, POISONED) is more elegant than writing a helper function for each status effect, but it's unclear why it had to be an opcode since the VM has a full compliment of the needed bitwise operators.) 

This leaves the 30xx series. This is very interesting since many of the names given in the list represent names for methods of objects (e.g. [UseOn](UseOn), Talk). The keys do not correspond to the method keys corresponding to these actions (e.g. [UseOn](UseOn) is identified in 0101 with 3004; the method key of [UseOn](UseOn) in objects (1xxx) is 0x000A.) 3000 does indeed appear to be [__init__](__init__), or at least, it is called when some objects are created (any monster hatched from an egg, and alchemical ingredients hatched from eggs, but not equipment of e.g. ruffians or objects created by dialogue scripts.) 

3001, which according to this would be "Look", is in fact called when a window is closed (on the originating object, e.g. closing a lyre calls it on the lyre). It is not called when a piece of cheese is eaten. It is not called when leaving an area with hatched monsters. It is not called when a scroll is used. 

3028, one of the mentioned resources in 0101, does not even exist (anymore?). Another resource in 30xx, not mentioned in 0101, is for digging (3039), and it's unclear why this code would not be in the shovel, which is the only object that can dig. 

It would appear that in any case the 3000 series represent default methods that can be overridden. The dig script 3039 after all just prints "You can't dig here!".  

Something that _is_ diggable (loose dirt, 110D) has a method 0039 (a lengthy function giving various dig results).  

My conclusion, provisionally, is that the names in 0101 are out of date with the game. 


|Key | Value|
|-|-|
|3022 | [ToggleLock](ToggleLock)|
|0200 | gTileNames|
|0201 | gCharNames|
|0202 | gSigns|
|3028 | Draw|
|300E | Attack|
|1664 | [DisplaySign](DisplaySign)|
|1665 | [DisplayScroll](DisplayScroll)|
|1666 | [DisplayContainer](DisplayContainer)|
|1667 | [DisplayInstrument](DisplayInstrument)|
|1000 | [DefaultZone](DefaultZone)|
|1700 | setbit|
|1701 | clrbit|
|1702 | tstbit|
|1703 | setworktype|
|1704 | getworktype|
|1705 | heal|
|1706 | curepoison|
|1707 | raisedead|
|1708 | enhorse|
|1709 | adjint|
|170A | adjdex|
|170B | adjstr|
|170C | adjexp|
|170D | adjlevel|
|170E | getinjury|
|170F | ispoisoned|
|1710 | ishorsed|
|1711 | deckarma|
|1712 | inckarma|
|1713 | inparty|
|300D | [CanHold](CanHold)|
|3000 | `__init__`|
|3001 | Look|
|3002 | Examine|
|3003 | Use|
|3004 | [UseOn](UseOn)|
|3005 | [UseAt](UseAt)|
|3006 | Talk|
|3007 | Wear|
|3008 | [UnWear](UnWear)|
|3009 | [CanWear](CanWear)|
|300A | [CanUnWear](CanUnWear)|
|300B | Enter|
|1640 | [DoDoor](DoDoor)|
|1641 | [DoToggle](DoToggle)|
|1642 | [DoLockable](DoLockable)|
|1643 | [DoKey](DoKey)|
|1644 | [DoToggleLock](DoToggleLock)|
|1645 | [DoVolumeCheck](DoVolumeCheck)|
|1646 | [DoFood](DoFood)|
|1647 | [DoClock](DoClock)|
|1648 | [SpillOut](SpillOut)|
|300C | Signal|




## Archived Information

A curious finding is that resource 0201 is indeed a list of character names. But the resource 0218 is the list of sign text, not 0202 (which does not even exist. There is likewise no resource 0200,  and tile names appear to be stored in resource F004. 

Entries 96-116 at least appear to relate to events that the Interface can issue. 


|Index | Field A| | Field B| | Name?|
|-|-|-|-|-|-|
|**0** | -1 | - | 0 | - |         |
|**1** | -1 | - | -1 | - |         |
|**2** | -1 | - | 0 | - |         |
|**3** | 764 | [02FC] | 12322 | [3022] |  0:'[ToggleLock](ToggleLock)'|
|**4** | 775 | [0307] | 512 | [0200] |  1:'gTileNames'|
|**5** | 786 | [0312] | 513 | [0201] |  2:'gCharNames'|
|**6** | 797 | [031D] | 514 | [0202] |  3:'gSigns'|
|**7** | 804 | [0324] | 12326 | [3026] |  4:'Dugged'|
|**8** | -1 | - | 12326 | - |         |
|**9** | 811 | [032B] | 12328 | [3028] |  5:'Draw'|
|**10** | 816 | [0330] | 12302 | [300E] |  6:'Attack'|
|**11** | -1 | - | 5698 | - |         |
|**12** | -1 | - | 0 | - |         |
|**13** | -1 | - | -3 | - |         |
|**14** | -1 | - | 0 | - |         |
|**15** | -1 | - | -1 | - |         |
|**16** | -1 | - | 0 | - |         |
|**17** | 823 | [0337] | 5732 | [1664] |  7:'[DisplaySign](DisplaySign)'|
|**18** | 835 | [0343] | 5733 | [1665] |  8:'[DisplayScroll](DisplayScroll)'|
|**19** | 849 | [0351] | 5734 | [1666] |  9:'[DisplayContainer](DisplayContainer)'|
|**20** | 866 | [0362] | 5735 | [1667] | 10:'[DisplayInstrument](DisplayInstrument)'|
|**21** | -1 | - | 5735 | - |         |
|**22** | -1 | - | -1 | - |         |
|**23** | -1 | - | 0 | - |         |
|**24** | -1 | - | -1 | - |         |
|**25** | -1 | - | 0 | - |         |
|**26** | -1 | - | -1 | - |         |
|**27** | -1 | - | 0 | - |         |
|**28** | -1 | - | -1 | - |         |
|**29** | -1 | - | 0 | - |         |
|**30** | -1 | - | -2 | - |         |
|**31** | -1 | - | 1024 | - |         |
|**32** | 884 | [0374] | 4096 | [1000] | 11:'[DefaultZone](DefaultZone)'|
|**33** | -1 | - | 4096 | - |         |
|**34** | -1 | - | -1 | - |         |
|**35** | -1 | - | 0 | - |         |
|**36** | -1 | - | -1 | - |         |
|**37** | -1 | - | 0 | - |         |
|**38** | -1 | - | -1 | - |         |
|**39** | -1 | - | 0 | - |         |
|**40** | -1 | - | -1 | - |         |
|**41** | -1 | - | 256 | - |         |
|**42** | -1 | - | -1 | - |         |
|**43** | -1 | - | 0 | - |         |
|**44** | -1 | - | -1 | - |         |
|**45** | -1 | - | 0 | - |         |
|**46** | 896 | [0380] | 5888 | [1700] | 12:'setbit'|
|**47** | 903 | [0387] | 5889 | [1701] | 13:'clrbit'|
|**48** | 910 | [038E] | 5890 | [1702] | 14:'tstbit'|
|**49** | 917 | [0395] | 5891 | [1703] | 15:'setworktype'|
|**50** | 929 | [03A1] | 5892 | [1704] | 16:'getworktype'|
|**51** | 941 | [03AD] | 5893 | [1705] | 17:'heal'|
|**52** | 946 | [03B2] | 5894 | [1706] | 18:'curepoison'|
|**53** | 957 | [03BD] | 5895 | [1707] | 19:'raisedead'|
|**54** | 967 | [03C7] | 5896 | [1708] | 20:'enhorse'|
|**55** | 975 | [03CF] | 5897 | [1709] | 21:'adjint'|
|**56** | 982 | [03D6] | 5898 | [170A] | 22:'adjdex'|
|**57** | 989 | [03DD] | 5899 | [170B] | 23:'adjstr'|
|**58** | 996 | [03E4] | 5900 | [170C] | 24:'adjexp'|
|**59** | 1003 | [03EB] | 5901 | [170D] | 25:'adjlevel'|
|**60** | 1012 | [03F4] | 5902 | [170E] | 26:'getinjury'|
|**61** | 1022 | [03FE] | 5903 | [170F] | 27:'ispoisoned'|
|**62** | 1033 | [0409] | 5904 | [1710] | 28:'ishorsed'|
|**63** | 1042 | [0412] | 5905 | [1711] | 29:'deckarma'|
|**64** | 1051 | [041B] | 5906 | [1712] | 30:'inckarma'|
|**65** | 1060 | [0424] | 5907 | [1713] | 31:'inparty'|
|**66** | -1 | - | 5907 | - |         |
|**67** | -1 | - | -1 | - |         |
|**68** | -1 | - | 0 | - |         |
|**69** | -1 | - | -1 | - |         |
|**70** | -1 | - | 0 | - |         |
|**71** | -1 | - | -1 | - |         |
|**72** | -1 | - | 1 | - |         |
|**73** | -1 | - | -1 | - |         |
|**74** | -1 | - | 0 | - |         |
|**75** | -1 | - | -1 | - |         |
|**76** | -1 | - | 0 | - |         |
|**77** | 1068 | [042C] | 12301 | [300D] | 32:'[CanHold](CanHold)'|
|**78** | -1 | - | 5697 | - |         |
|**79** | -1 | - | -1 | - |         |
|**80** | -1 | - | 8336 | - |         |
|**81** | -1 | - | 2048 | - |         |
|**82** | -1 | - | -2049 | - |         |
|**83** | -1 | - | 1 | - |         |
|**84** | -1 | - | -2081 | - |         |
|**85** | -1 | - | 2 | - |         |
|**86** | -1 | - | -1 | - |         |
|**87** | -1 | - | 16 | - |         |
|**88** | -1 | - | -1 | - |         |
|**89** | -1 | - | 0 | - |         |
|**90** | -1 | - | -2049 | - |         |
|**91** | -1 | - | 2048 | - |         |
|**92** | -1 | - | -259 | - |         |
|**93** | -1 | - | 512 | - |         |
|**94** | -1 | - | -1 | - |         |
|**95** | -1 | - | 2064 | - |         |
|**96** | 1076 | [0434] | 12288 | [3000] | 33:'<ins>init</ins>'|
|**97** | 1085 | [043D] | 12289 | [3001] | 34:'Look'|
|**98** | 1090 | [0442] | 12290 | [3002] | 35:'Examine'|
|**99** | 1098 | [044A] | 12291 | [3003] | 36:'Use'|
|**100** | 1102 | [044E] | 12292 | [3004] | 37:'[UseOn](UseOn)'|
|**101** | 1108 | [0454] | 12293 | [3005] | 38:'[UseAt](UseAt)'|
|**102** | 1114 | [045A] | 12294 | [3006] | 39:'Talk'|
|**103** | 1119 | [045F] | 12295 | [3007] | 40:'Wear'|
|**104** | 1124 | [0464] | 12296 | [3008] | 41:'Unwear'|
|**105** | 1131 | [046B] | 12297 | [3009] | 42:'[CanWear](CanWear)'|
|**106** | 1139 | [0473] | 12298 | [300A] | 43:'[CanUnwear](CanUnwear)'|
|**107** | 1149 | [047D] | 12299 | [300B] | 44:'Enter'|
|**108** | 1155 | [0483] | 5696 | [1640] | 45:'[DoDoor](DoDoor)'|
|**109** | 1162 | [048A] | 5697 | [1641] | 46:'[DoToggle](DoToggle)'|
|**110** | 1171 | [0493] | 5698 | [1642] | 47:'[DoLockable](DoLockable)'|
|**111** | 1182 | [049E] | 5699 | [1643] | 48:'[DoKey](DoKey)'|
|**112** | 1188 | [04A4] | 5700 | [1644] | 49:'[DoToggleLock](DoToggleLock)'|
|**113** | 1201 | [04B1] | 5701 | [1645] | 50:'[DoVolumeCheck](DoVolumeCheck)'|
|**114** | 1215 | [04BF] | 5702 | [1646] | 51:'[DoFood](DoFood)'|
|**115** | 1222 | [04C6] | 5703 | [1647] | 52:'[DoClock](DoClock)'|
|**116** | 1230 | [04CE] | 5704 | [1648] | 53:'[SpillOut](SpillOut)'|
|**117** | -1 | - | 5704 | - |         |
|**118** | -1 | - | 0 | - |         |
|**119** | -1 | - | -1025 | - |         |
|**120** | -1 | - | 128 | - |         |
|**121** | -1 | - | -4609 | - |         |
|**122** | -1 | - | 4097 | - |         |
|**123** | 1239 | [04D7] | 12300 | [300C] | 54:'Signal'|
|**124** | -1 | - | 12300 | - |         |
|**125** | -1 | - | -1 | - |         |
|**126** | -1 | - | 0 | - |         |


