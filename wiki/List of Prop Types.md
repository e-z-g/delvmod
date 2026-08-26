
_For the big unfiltered list, see [List of Prop-Tile Associations](List-of-Prop-Tile-Associations)_ 


|**Proptype** | **Description** | **Aspect...** | ** Parameters...**|
|-|-|-|-|
|0x01F | Potion | Potion type (and appearance) | Unused|
|0x02A | Ladder/Trapdoor | 0 = trapdoor, 2 = ladder | d3 = [Zoneport](Zoneport)|
|0x04B | Scroll  | NA | d1=[Spell Number](List-of-Spells) d2 = 0.|
|0x105 | Tome (teaches spell) | NA | d1=[Spell Number](List-of-Spells) d2 = 0.|




|**[Aspect](Aspect)** | **Potion Type**|
|-|-|
|0 | sustenance|
|1 | healing|
|2 | mana|
|3 | free motion|
|4 | antidote|
|5 | clear mind|
|6 | resist fire|
|7 | farsight|




## Working Notes

Scripts for an object are located in 0x1000 + proptype. 
