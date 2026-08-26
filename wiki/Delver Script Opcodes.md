
The stack values are S0 (top of stack), S1 (the value below the top) etc, and are popped if not otherwise specified. E.g. we say S <- S1 % S0 to mean "pops two numbers from the stack, divides the lower by the upper, and pushes the quotient onto it." 

If a statement involves multiple stacks, they will be designated by capital letters with analogous numbering. Lower-case letters are single hex digits. 


|**Local Variables and Parameters**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|0x | pushl x | S <- locals[x] | Push the xth local variable onto the stack.|
|3x | pusha x | S <- args[x] | Push the xth argument of the function onto the stack.|




|**Constant values**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|41 xx | pushb | S <- xx | Push a signed 1-byte integer onto the stack|
|42 xxxx | pushs | S <- xxxx | Push a signed 2-byte integer onto the stack|
|43 fxxxxxxx | pushw fxxxxxxx | S <- fxxxxxxx | Push a [Word](Word). (If ff=00, xxxxxx is a 24-bit signed integer|
|44 ... 00 | pushc | S <- null terminated string ... | |
|45 nnnn | pushd [ ... ] | S <- nnnn bytes of data  | At least arrays (0x90..) and tables (0xA0..) can be pushed.|




|**Indexing**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|46 | index | S <- S1[S0] | Both lists and dictionaries can be indexed.|




|**Globals**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|48 xx | global xx | S <- globals[xx] | See [List of Globals](List-of-Globals)|
|49 xx xx xx xx | ??? | Uncertain, might have to do with zone local state... | ... but then apparently the PC's gender is accessed with it.|




|**Arithmetic**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|4A | add | S <- S1 + S0 | |
|4B | sub | S <- S1 - S0 | |
|4C | mul | S <- S1 * S0 | |
|4D | div | S <- S1 / S0 | |
|4E | mod | S <- S1 % S0 | |
|55 | neg | S <- -S0 | |




|**Comparisons**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|4F | lt | S <- S1 < S0 | |
|50 | le | S <- S1 <= S0 | |
|51 | gt | S <- S1 > S0 | |
|52 | ge | S <- S1 >= S0 | |
|53 | ne | S <- S1 != S0 | |
|54 | eq | S <- S1 == S0 | |




|**Bitwise Operations**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|56 | andb | S <- S1 & S0 | |
|57 | orb | S <- S1 | S0 | |
|58 | xorb | S <- S1 ^ S0 | |
|59 | notb | S <- ~S0 | |
|5A | lsh | S <- S0 << S1 | |
|5B | rsh | S <- S0 >> S1 | |




|**Logical Operations**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|5C | and | S <- S1 && S0 | |
|5D | or | S <- S1 or S0 | |
|5E | not | S <- !S0 | |
|5F | len | S <- len(S0) | Works on strings and arrays. Unindexible things return 0. | Does it work on dicts?|




|**Structure Fields**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|60 ?? | Observed in a conditional in 0901 as 60 44|
|61 ?? ??  | Observed in a conditional in 301A|||
|62 ff | field ff | S <- S0.ff | See [Delver Script Structs](Delver-Script-Structs) for the field values.|
|63 cc | Cast to cc | ??? | Exact semantics and cc values unknown; 63 40 appears to cast a prop to a character. Does it promote things (initialize fields)?|
|64 cc | istype | S <- S0 is type cc | Appears in 301A in a conditional. Checks current type, not castability.|




|**Statements**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|82 ll R... 40 | set ll ... end  | Local ll <- R0 | |
|84 L... 40 I... 40 R... 40 | setindex L... at ... to ... end | L0[I0] = R0 | see 1087, writing on a paper|
|86 ff L... 40 R... 40 | setattr | L0.ff <- R0 | See [Delver Script Structs](Delver-Script-Structs) for the field values.|
|87 gg R... 40  | setglobal | global gg <- R0 | Tentative identification.|
|8A V... 40 | print | print V0 | Can display integers, booleans, strings, and objects. objects (arrays etc) are printed as <xxxxyyyy> where xxxx is the resource in which they occur plus 0x8000 and yyyy is the offset in the resource.|




|**Flow Control**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|8C C... 40 aa aa | if | Goto aaaa if C0 | Conditional (actually less common than 8D (tested)|
|8D C... 40 aa aa | if_not | Goto aaaa if not C0 | The basic conditional. (Tested)|
|88 aa aa | goto | Branch unconditionally to aa aa | |




|**System**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|90 promptlist 00 pp pp  | Add a conversation response. pp pp is the offset to the next alternative. | |
|93 S... 40 | close ( ... ) | Seen in 100E, 0816 | Seems to close / finish a gui element.|
|9B ww S... 40 | gui ww ... end | [Scripting GUI Operations](Scripting-GUI-Operations).|
|9D mm S... 40 | call_method_mm(S...) | Calls a method mm of an object | push object first, then arguments|
|9E pp pp S... 40 | call_this pppp (S...) | Call this resource at offset pppp, with S as arguments.|
|9F rr rr S... 40 | call_resource rrrr ... end | Call the function in resource rrrr with the stack S as arguments.|
|A6 T... 40 | ??? | ??? | Seein in 1A21, Rune_of_Pain.[UseAt](UseAt)()|
|A7 T... 40 | del ( ... ) |  Deletes T0. Has been tested with props. | It seems it works on other sorts of things... 1105|
|A8 S... 40 | createprop(short, proptype, byte,byte | Creates props.  | see 0x1878:0x966, Sabinate gives the pc a mushroom.(0x0001,0x010f,0,0)|
|At least the upper bits of the proptype are flags or maybe aspect?. e.g. pelagon giving 4th shard: (1,0x825,0,0) - glowing crystal is 0x025. last two numbers might be the persistence values, first might be the destination.)|||||
|AC S... 40 | randint | S <- randint(min=S1,max=S0) | Generates a random integer in [min, max). e.g. S1=1,S0=7 would be the results from a d6.|
|AD S... 40 | createat | seems to add objects to the world model | [Opcode AD](Opcode-AD) Seen in 301A and elsewhere with a large number of parameters, mostly byte 0, first is byte 0x1C.|
|B9 S... 40 | join_party(S0) | The character joins the party. Must be a real character, not a monster. | It isn't necessary to cast the thing to 0x40, yet this only works on Characters|
|BF S... 40 | changezone | changezone(wipeeffect,zoneport,flags) | flags for camera bump on wipeeffect?|
|flags - 1 party follows, 2 - teleporter effect; wipeeffect - 0 instant, 1 or d box wipe, c wipe down, b up, a right,9 left|||||
|C1 S... 40 | setbit | setbit(object=S1, whichbit=S0) | Sets a bit (e.g. applies a status effet)|
|C2 S... 40 | clearbit | clearbit(object=S1, whichbit=S0) | Clears a bit/flag (e.g. cures poisoning)|
|C4 S... 40 | testbit | S <- testbit(object=S1, whichbit=S0) | e.g. 9 as the second parameter tests for poisoning|
|C5 S... 40 | emit_signal | emit_signal(id) | Raises a signal to which other objects might react. E.g. 1175 Strange Device and 100A, stone door|
|CB S... 40 | ??? | Appears to take two parameters, one word starting with 1, the other an integer. | See 109E, shovel|
|D2 S... 40 | playnote | It takes three integer parameters (instrument, pitch, duration?) and seems to block until the note is finished.|
|D3 S... 40 | playsound | playsound(which=S2, x=S1, y=S0) | Plays a sound; the which parameter is the low byte of the sound resid. | Difference with D7?|
|D6 S... 40 | ??? | ??? | Seen in character scripts e.g. 180D|
|D7 S... 40 | playsound2 | playsound(which=S2, x=S1, y=S0) | Plays a sound; the which parameter is the low byte of the sound resid. | Difference with D3|
|DB S... 40 | haswindow | haswindow(someprop) |  If someprop has a window open, return true and bring the window to the front. Otherwise return false.|
|DC S... 40 | ??? | ???(which) -> truth value | in 1825, checking if the gator boots are done. Also used to track other plot events in many places (dc 41 xx)|
|DD S... 40 | ??? | ???(which,value) | in 1825, set when gator boots given to player and when he starts working on them - probably sets a timer. value seems to be in days.|
|E1 S... 40 | magicaura | magicaura(whom=S1, color=S0) | Makes a prop glow as when casting a spell. Color is a word (0x43 .. .. .. ..), low byte is color.|
|E2 S... 40 | shooteffect | shooteffect(src_x,src_y,dst_x,dst_y,tile_id, ?, ?, optional?) | Coordinates are in level-space not screen-space. 1A22, 1A1D, 1A12|
|F2 S... 40 | add_quest | add_quest(stringtableref) Add item to to-do list. | Works with a 0x3000xxxx+n string table reference, not a string directly.|
|F5 S... 40 | getskill | getskill(possibleSkillHaver, skillID) | Returns the skill object instance for a character, or None if untrailed.|




|**Unknown Statements**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
| 84 A 40 B 40 C 40  |   |  Unknown  |  See 3005 |
| 93 S... 40 |   |   |  See 0816.|




|**Unknown Expressions**|||||
|-|-|-|-|-|
|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
| 6A xx xx  |     | Unknown |  See 0E87|



_Note: This below is out of date_ What is going on with 080E and 1802, with nested functions... 080c Spell: sleep 

```
8D
   9F 0E A1
      30    62 0B
      41 02
      41 04
   40
40 00 98               ; if CastSpell(caster.field0B, spell_level=2, spell_mana_cost=4): ask on whom, else:  end
```

4 is the cost of this spell. its level is 2. 

S0 - top of stack; S1 - item below S0 on stack; S2 - item below S1, etc. P0 - function call parameter 1; P1 - parameter 2; etc. 


|**Opcode** | **DTW-Assigned Mnemonic** | **Explanation** | **Questions**|
|-|-|-|-|
|_Parameters_|||
|3n | push argv[n] | Push call parameter n onto the stack|
|_Immediate data_|||
|40 |   |   |  Is there a register? |
|41 bb | push (bb) | Push byte onto stack|
|43 ww ww ww ww |  push (wwwwwwww) | Push word onto the stack |  Is the word 3 bytes or 4? The field is 4, at any rate|
|44 (chars) 00  |  push "chars"  | Push a null-terminated string onto the stack | |
|_Arithmetic_|||
|4A |  add  |  Pop two operands from the stack, add, and push result onto the stack  |  |
|4B |  sub  |  Pop two operands from the stack, subtract, and push result onto the stack  |  |
|4C |  mul  |  Pop two operands from the stack, multiply, and push result onto the stack  |  |
|_Comparisons_|||
|51 |  gt  |  Greater than  |  Not known if it pushes a truth value onto the stack or sets a flag. (Probably the former, though)|
|_Bitwise Operations_|||
|5A |  shl  |  Left shift  |  |
|_Data Structures_|||
|62 xx | field .xx | Replace the top stack item with the value retrieved from its field xx | |
|_Subroutines_|||
|81 aa bb |   |   |  Always starts functions/methods. aa might be number of args, bb number of local variables?|
|_Local variables_|||
|82 aa |  push &locals[a] | Push reference to local variable onto the stack. | Maybe it is only for storing?|




|8D aa |  push locals[a] | Push local variable onto the stack. | |
|-|-|-|-|



If true, player character is male 

```
  8D
    49 05 00 00 10
  40 01 FF
```

This predicate only occurs as such. It would be interesting to find any other examples of 0x49. The sequence after it is also very puzzling. You would think this would either be a property of the player character or more likely a global variable, but apparently not. 

The only other 49.05 sequence: 

```
  Curing Alaric
82 05
  49 05 01 01 10
  48 05
  62 20
  46
40

```


#### 61 xx yy

30 61 0C 01/00 - none for people and nonpeople. 

30 61 33 00 - prints out the "learned description" of an item, none if it has none. 

Seems to retrieve an item (field xx) which is an array and index it with yy. maybe. Why there is an opcode for this specific thing and why it doesn't seem to work with arbitrarily injected arrays is obscure. 

49 sequences are seen, e.g. 49.03 in the bed (100E) or 49.00 in various places. 


#### load_word_from_res


|49 rr rr ii ii | load_word_from_res r i | ldwr r i | Loads a word from resource r at offset i|
|-|-|-|-|



* - Cannot directly refer to savedgame resources (tried with E000, journal entry) - But it can load data ultimately stored in the saved game (e.g. player gender 49 05 00 00 10) - Can refer to arbitrary data file resources - when seen in the game it seems to refer to Script Data / Static Data in  the scenario file (03xx, 05xx). - Resources with these IDs do not exist in the saved game file and the original versions in the scenario file seem to primarily be placeholders - e.g. the player's gender is in 0500:0010 and is a boolean, but 0500:0010 contains only zeroes. 