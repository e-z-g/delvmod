
List of globals, as used e.g. by the _global XX' opcode, and global-setting command in [Delver Scripts](Delver-Scripts). 


|**Global** | **redelv Name** | **Description** | **Type**|
|-|-|-|-|
|0x00 |  --  | prints "9"|
|0x01 |  --  | prints "morning" (probably time of day)|
|0x02 |  --  |  Player character (name?)  | |
|0x03 |  --  |  prints "???"|
|0x04 |  Minute = (global4 & 0xFFF) / 68  |  printed "38572" (keeps adding 11 each movement) - time of day? | 0E47|
|0x05 | --  | The player character (as a Character?). Seems to be used without casting e.g. with [GetSkill](GetSkill)  | Unknown|
|0x06 |  number of persons in party, counting the PC; used for e.g. meal costs  |  print "5"|
|0x07 |  -- seems to be the same as 0x06, but used in different resources.  |  prints "5" |
|0x08 |  unobserved in ddasm_src  |  prints None |
|0x09 | --  | The active/current character  | Unknown|
|0x0A |  --  |  Last conversation response |
|0x0b |  --  |  prints None |
|0x0c |  karma  |  prints 100|
|0x0d |  registered  |  true |
|0x0e |  languages known. Seldane = 1.  |  prints 1 |
|0x0f |  --  |  25 |
|0x10 |  current zone  |  8 |
|0x11 |  --  |  None |
|0x12 |  some kind of early, less general state tracking mechanism? invoked in 1806 to deal with hector's earthquake dialogue  |  0 |
|0x13 |  isplayerturn??  |  true |
|0x14-0x19 |  --  | None|


