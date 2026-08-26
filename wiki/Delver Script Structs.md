

|**Prop**|||
|-|-|-|
|**Field** | **Name** | **Comment**|
|00 | flags | UNCHECKED|
|01 | x |  (you need to set both x and y to set an inside-other-prop location)|
|02 | y | |
|03 | aspect | Current [Aspect](Aspect) of the prop|
|04 | prop_type | [List of Prop-Tile Associations](List-of-Prop-Tile-Associations), [List of Prop Types](List-of-Prop-Types) |
|05 | this field &0x03FF is prop type, &0xFC00 is aspect.  | |
|06 | d1 |  First persistence data byte|
|07 | d2 |  Second persistence data byte|
|08 | d3 |  d1 and d2 as one 16-bit persistence value |
|09 | ?? |  Has not been seen with a value other than 1.|




### Cast Opcode (0x63) Working Area

Sightings: 6300 in res 10F4 (landking amulet), the global for the current character (48 09) is cast to 00 in the system call E1 (magicaura). Curiously the spell scripts (which obviously make heavy use of magicaura) do not consistently perform this cast. My guess is that it is a down cast (perhaps from Character to Prop) and it isn't actually necessary since all Characters are Props.  

But experimentally, it is necessary to cast a prop (obtained as what was passed to the 3039 dig action script by a shovel) to a character (possibly, 63 40) to retrieve character-specific properties like magic points or nutrition.  

63 30 is seen in the script 1175 (strange device) in the system call 9E, and nowhere else in the object scripts. 

63 40 is seen numerous times. In 1A15 (Resist Blows) an interesting occurrence is seen; the arg0 and arg1 of the spell [UseOn](UseOn) script are both cast to 40 and then compared. If they are the same it says "You feel safer" otherwise "(the target) feels safer". This is perplexing for a variety of reasons.  

First, as confirmed by printing experiments, arg0 of a skill or spell's .[UseOn](UseOn) is the skill, not the skill user. The other curious thing is that the spell itself does not do what it the script seems to intend. (It will in fact say "Bellerophon feels safer").  

```
Resist_Blows.UseOn
printing arg0, arg1: Resist Blows, Hector
arg0 cast 40, arg1 cast 40: None, Hector


Presumably the script should instead use 48 09  to get the caster.
casting on self:
arg1: Bellerophon
global 9: Bellerophon
arg1==global9? false
arg1 cast 40 == global9? true
arg1 == global9 cast 40? false
arg1 cast == global9 cast? true
arg1 cast: Bellerophon
global9 cast: Bellerophon


```

Casting semantics: casting will make istype stop saying it is part of the old type, even if the new type inherits from the old type. If you cast from prop to character and access a prop field on the casted object, it will only work if the prop was indeed part of a character - if it wasn't, None is returned even for fields that a prop does have. 
