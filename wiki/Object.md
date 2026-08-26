
This page describes the classes of objects encountered in the scripting system. This information is distinct from what we are calling 'structs' which have fields we access with opcodes 86xx/62xx (set_field, field) and rather refer to the keys seen at the tables at the end of classes in e.g. resources 10xx.  


### Provisional Names for Classes


|**Name** | **Resource IDs**|
|-|-|
|Item | 10xx, 11xx|
|Zone | 14xx|
|[SubZone](SubZone) | 15xx|
|Character | 18xx|
|[MonsterDeaths](MonsterDeaths) | 19xx | Unclear what it does besides generating loot.|
|Skill | 1Axx|
|Room | 1Bxx,1Cxx|
|Unknown1E | 1Exx | Only one of these. Method_14 changes zone to 0x92, exit to tree of life map.|



30xx contains default methods. Conjecturally, 10xx-30xx may be set aside for class code. 


## Item (10xx,11xx)

(Presumably 1000-13FF) 


|_Key_ | _Field_ | _Description_|
|-|-|-|
|0024 | Weight | Array containing a single integer, the weight in "grains"|




### Room

Are 1Cxx and 1Bxx really the same? There is a break in the resource IDs (1BD8, 1BD9, 1C2D, 1C2E...) Evidence suggesting they are - eggs seem to refer to them with a common mechanism, and eggs from the same place are in sequence, not separated into types. The flags for this type of egg is 0x42 and the "prop type" is the resource number, i.e. 007 = 1B07,  The "none values" are obscure. They do not seem to be unique e.g. 1B03 and 1B02  

Larisa's house. 


|**Key** | Example values | Name | Type | Notes|
|-|-|-|-|-|
|6174 | None|
|0007 | method|
|0014 | method|



"a common, informal eating area" 


|**Key** | Example values | Name | Type | Notes|
|-|-|-|-|-|
|534C | none|
|0007 | method | Enter? | function | Seems to be what is triggered when the player enters the room. In this case it does nothing but print the description.|
|504C | none|



"small storage area, probably some sort of armory" 


|**Key** | Example values | Name | Type | Notes|
|-|-|-|-|-|
|534C | none|
|0007 | method (with description|
|504C | none|



Conjurer's Triangle 


|**Key** | Example values | Name | Type | Notes|
|-|-|-|-|-|
|FFFF | none|
|0007 | method|
|0000 | none|



spartan bedroom 1B02 


|**Key** | Example values | Name | Type | Notes|
|-|-|-|-|-|
|0000 | none|
|0007 | description method|
|7373 | none|



library LKH? 1B03 


|0000 | none|
|-|-|
|0007 | description|
|7373 | none|



Throne room 1B04 


|706F | none|
|-|-|



||0007||description as usual 


|0000 | none|
|-|-|



Kosha parlor 1C35 


|0007 | description as usual|
|-|-|
|6C69 | none|
|7373 | none|



Omen's test (entering "his" room.) 1CC3 


|6131 | none|
|-|-|
|0007 | usual|
|6F62 | none|



Decaying seaweed chapel 


|2031 | none|
|-|-|
|0007 | usual|
|6544 | none|



1BD9 - 7320 none, 0007 usual, 2041 none  1BD8 -6D70, 206D 1BD7 - 0D62, 2863 1BD6 - 6C61, 6174 1BD5 (jail) - 0014 (aethon's comment), 0007 (name), 6973 1B6F - 7065, 7269 1B37 - 696E, 0000 
### Unknown1E


|**Key** | Example values | Name | Type | Notes|
|-|-|-|-|-|
|6131 | none|
|746E | none|
|0014 | N/A | ??? | method | Appears to change zone to the conjectural Tree of Life exit port.|


