
The redelv Prop List editor has fairly powerful searching functionality. Obviously, one can type a value into the "Search by..." bar and see only props matching that value. But if instead of putting just a number in the field, you can specify a matching condition other than "exactly equal."  


|**redelv match conditions**|||
|-|-|-|
|**Operator** | **Condition** | **Example**|
|> | Value is greater than X | Flags: >0|
|< | Value is less than X | Index: <0xFF|
|>= | Value is greater than or equal to X||
|<= | Value is less than or equal to X||
|!= | Value is not equal to X | d2: !=10|
|& | Value bitwise-anded with X is not zero |  Flags: &0x01 |
|!& | Value bitwise-anded with X is zero |  Flags: !&0x18 |
|(No operator) | Value is exactly X  |  Index: 35 |
|/ | Value in cell contains the regular expression X | [PropType](PropType): /(goat)|(chicken) |
|_Another Example:_| | [PropType](PropType): /door|



Match conditions are ordinarily integers (decimal, with no prefix, or hexidecimal, prefixed with 0x) but can also have one of three special formats used for matching locations. 


|**redelv match operand formats**|||
|-|-|-|
|**Operator** | **Condition** | **Example**|
|x,y | Location in coordinates | Location: 23,10|
|#x | Inside character inventory | Location: #1|
|@x | Inside container | Location: @559|



Note that these have to be combined with an appropriate Flag filter to avoid false positives (the location search box can only look at its own table column, but to know which category the location of a prop list item belongs, you need to look at the flag column. E.g. Flags:0x18 for an equipped item in the player's inventory.) 
