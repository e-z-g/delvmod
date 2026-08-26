
This is a list of opcodes used by [RDASM](RDASM). 


## Opcodes by code

The opcodes are here numerically ordered by the first byte, with missing entries for as-yet unknown or incompletely known opcodes. 


|Binary format | RDASM Name | Mnemonic | Short Description / notes|
|-|-|-|-|
|ii (0 <= i <= 2F) | local i | loc i | Push a local variable onto the evaluation stack.|
|3i | argument i | arg i | Push a function argument onto the evaluation stack.|
|40 | end | -- | Close an evaluation stack.|
|40 ff ff | then f | Close a stack with an address.|
|41 ii | load_byte ii | byte i | Push an immediate signed byte onto the evaluation stack.|
|42 ii ii | load_short iiii | short i | Push an immediate signed short onto the evaluation stack.|
|43 ww ww ww ww | load_word w | word w  | Push an immediate word onto the evaluation stack.|
|44 ...  | load_cstring "s" | string "s" | Push a null-terminated string onto the evaluation stack.|
|45 ll ll ... | load_data ... | data ... | Push data object onto the stack, of length l bytes.|
|46 | index | idx | Index arrays and tables.|
|47 aa aa | load_word LABEL | ldw LABEL | Load a word from the local address space of the code being executed.|
|48 ii | global i | glo i | Push a global variable onto the evaluation stack.|
|49 rr rr ii ii | load_word_from_res r i | ldwr r i | Loads a word from resource r at offset i|
|4A | add | add | The usual arithmetic operation.|
|4B | subtract | sub | The usual arithmetic operation.|
|4C | multiply | mul | The usual arithmetic operation.|
|4D | divide | div | The usual arithmetic operation.|
|4E | modulus | mod | The usual arithmetic operation.|
|4F | less_than | lt | The usual inequality.|
|50 | less_than_or_equal | le | The usual inequality.|
|51 | greater_than | gt | The usual inequality.|
|52 | greater_than_or_equal | ge | The usual inequality.|
|53 | not_equal | ne | The usual inequality.|
|54 | equal | eq | The usual equality.|
|55 | negative | neg | Unitary minus arithmetic operation.|
|56 | bitwise_and | andb | Bitwise arithmetic operation.|
|57 | bitwise_or | orb | Bitwise arithmetic operation.|
|58 | bitwise_xor | xorb | Bitwise exclusive or operation.|
|59 | bitwise_not | notb | Bitwise invert operation.|
|5A | left_shift | lsh | Left shift bitwise operation.|
|5B | right_shift | rsh | Right shift bitwise operation.|
|5C | logical_and | and | Boolean operation.|
|5D | logical_or | or | Boolean operation.|
|5E | logical_not | not | Boolean operation.|
|5F | get_length | len | length of object on top of stack.|
|60 xx | has_field x | has x | true if the object has the field specified, 0 otherwise. (How does it work with inheritance?)|
|61 xx xx | class_variable x y | cvar x y | Retrieve class variable x (limited to one byte) and put its `i`th indexed item on the stack, the class variable being assumed to be an array.|
|62 ff | get_field f | field f | Get a field of a structure.|
|63 cc | cast_to c | cast c | Cast an object to a type `c`.|
|64 cc | is_type c | type c | Checks type of an object.|
|65 | unobserved_65 | ub65 | _Unobserved_, has been looked for fairly extensively|
|66 | unobserved_66 | ub66 | Not found.|
|67 | unobserved_67 | ub67 | Looked for not extensively.|
|68 | unobserved_68 | ub68 | _Unobserved_|
|69 | unobserved_69 | ub69 | _Unobserved_|
|6A | unobserved_6A | ub6A | _Unobserved_|
|6B | unobserved_69 | ub69 | _Unobserved_|
|6C | unobserved_6C | ub6C | _Unobserved_|
|6D | unobserved_6D | ub6D | _Unobserved_|
|6E | unobserved_6E | ub6E | _Unobserved_|
|6F | unobserved_6F | ub6F | _Unobserved_|
|70 | unobserved_70 | ub70 | _Unobserved_|
|71 | unobserved_71 | ub71 | _Unobserved_|
|72 | unobserved_72 | ub72 | _Unobserved_|
|73 | unobserved_73 | ub73 | _Unobserved_|
|74 | unobserved_74 | ub74 | _Unobserved_|
|75 | unobserved_75 | ub75 | _Unobserved_|
|76 | unobserved_76 | ub76 | _Unobserved_|
|77 | unobserved_77 | ub77 | _Unobserved_|
|78 | unobserved_78 | ub78 | _Unobserved_|
|79 | unobserved_79 | ub79 | _Unobserved_|
|7A | unobserved_7A | ub7A | _Unobserved_|
|7B | unobserved_7B | ub7B | _Unobserved_|
|7C | unobserved_7C | ub7C | _Unobserved_|
|7D | unobserved_7D | ub7D | _Unobserved_|
|7E | unobserved_7E | ub7E | _Unobserved_|
|7F | unobserved_7F | ub7F | _Unobserved_|
|80 | unobserved_80 | ub80 | _Unobserved_|
|81 pp ll | function (arg0 ... argp) (local0 ... locall) (...) | fun (arg0...argp) (local0...locall) (...) | Starts a function/method context.|
|82 vv ... 40 | set_local v (...) | setl v (...) | Set a variable.|
|83 aa aa ... 40 | write_word LABEL (...) | wrw LABEL (...) | Writes a word into the local code/object space (!!). (It will be reset when the game is reloaded.) |
|84 L... 40 I... 40 R... 40 | set_index (L...) (I...) (R...) | seti (L...) (I...) (R...) | Set an item of an array L at index I to new value R.|
|85 rr rr ii ii ... 40  | write_word_to_resource r i (....) | wrwr r i (...) | Writes a word(?) to resource r at index i. For classes at least this does not persist between saves, but neither is it overwritten when reloading from a saved game...|
|86 ff L... 40 R... 40 | set_field f (L...) (R...) | setf f (L...) (R...) | Set L.f = R.|
|87 gg ... 40 | set_global g (...) | setg g (...) | Set a global variable.|
|88 aa aa | unconditional_branch a | branch a | Go to the local address `a` unconditionally.|
|89 ... 40 nn nn [...] | unknown_89 (...) (LABEL1 LABEL2 ... LABELn) | un89  (...) (LABEL1 LABEL2 ... LABELn) | Seen in 0E95 and Oe96. some kind of dispatch?|
|8A ... 40 | print (...) | print (...) | Print text out to the console or conversation box, depending on context.|
|8B ... 40 | return (...) | ret (...) | Return a value.|
|8C ... 40 aa aa |  branch_if (...) LABEL  |  if (...) LABEL | Conditional branch. (Usually for loops.)|
|8D ... 40 aa aa |  branch_if_not (...) LABEL  |  if_not (...) LABEL |  Negative-conditional branch. (Usual for if statements.)|
|8E | unknown_8E | un8E | Seen in `187C`, `1864` and may others without any parameters. It may begin a conversation.|
|8F | unknown_8F | un8F | Seen in 1862, 1822, 1821 etc. May display a text prompt box.|
|90 cstring pp pp | conversation_prompt "foo,bar" (...) | prompt "foo,bar" (...)|
|91 | unobserved_91 | ub91 | _Unobserved_|
|92 xx ... 40 | unknown_92 x (...) | un92 x (...) | Occurs in 1801 (saved by amulet) and 1CC3 (omen returns player to LKH) with x=0 and None as the only parameter.|
|93 ... 40 | gui_close (...) | gclose | Close a window.|
|94 | unobserved_94 | ub94 | _Unobserved_|
|95 | unobserved_95 | ub95 | _Unobserved_|
|96 | unobserved_96 | ub96 | _Unobserved_|
|97 | unobserved_97 | ub97 | _Unobserved_|
|98 | unobserved_98 | ub98 | _Unobserved_|
|99 | unobserved_99 | ub99 | _Unobserved_|
|9A | unobserved_9A | ub9A | _Unobserved_|
|9B ww ... 40 | gui w (...) | gui w (...) | GUI operation W|
|9C rr rr ... 40 ... 40  | call_index r (i...) (p...) | cidx p | Calls a resource r+i with parameters p.|
|9D mm ... 40 | call_method m (...) | method m (...) | Call a method of the object at the bottom of the stack with the arguments on top|
|9E pp pp ... 40 | call_subroutine p (...) | csub p (...) | Call a subroutine in the same file.|
|9F rr rr ... 40 | call_resource r (...) | res r (...) | Call a function in a resource.|
|A0 | unknown_A0 | unA0 | Seen in `10C1` 'bell' with a word and a byte parameter, or one word and three byte parameters|
|A1 | unobserved_A1 | ubA1 | _Unobserved_, looked for 40searched|
|A2 ... 40 | unknown_A2 (...) | unA2 (...) | Seen in 1801 with a string parameter, seems to quit the game|
|A3 ... 40 | unknown_A3 (...) | unA3 (...) | Seen in 1025 Crolna, unA3(0x28)|
|A4 | unknown_A4 (...) | unA4 (...) | See [Distiller Script](Distiller-Script). (short,byte)|
|A5 | unobserved_A5 | ubA5 | _Unobserved_ Looked for, not found|
|A6 ... 40 | unknown_A6 (...) | unA6 (...) | Seen in `1A21`|
|A7 ... 40 | delete (...) | del (...) | Deletes an object.|
|A8 ... 40 | create_prop (...) | createprop (...) | createprop(short,proptype,byte?,byte?)|
|A9 | unobserved_A9 | ubA9 | _Unobserved_ Looked for, not found|
|AA | unobserved_AA | ubAA | _Unobserved_ Looked for, not found|
|AB ... 40 | unknown_AB (...) | unAB (...) | Several parameters. Seen in Thersites, 1865, and many other locations in dialogue|
|AC ... 40 | random_integer (...) | rand (...) | rand(min,max) (value in `[min,max)` )|
|AD ... 40 | create_at (...) | create (...) | See in 301A. Also used in making skill objects so maybe "at" is a bad name.|
|AE ... 40 | unknown_AE (...) | unAE (...) | Seen in 1865, 2 parameters, (word, byte.) In 1CC3, testing for if the player found Omen's reward.|
|AF | unobserved_AF | ubAF | _Unobserved_ Looked for, not found|
|B0 | unobserved_B0 | ubB0 | _Unobserved_ 40searched|
|B1 ... 40 | unknown_B1 | unB1 | seen with 4 parameters in 1825 starting gator boots, & 1832|
|B2 | unobserved_B2 | ubB2 | _Unobserved_|
|B3 | unobserved_B3 | ubB3 | _Unobserved_|
|B4 | unobserved_B4 | ubB4 | _Unobserved_|
|B5 | unobserved_B5 | ubB5 | _Unobserved_|
|B6 | unobserved_B6 | ubB6 | _Unobserved_|
|B7 | unobserved_B7 | ubB7 | _Unobserved_|
|B8 ... 40 | get_weight (...) | weight (...) | Gets the weight in 'grains' of an object. parameters(aspect-proptype, 1)|
|B9 ... 40 | join_party (...) | join (...) | Cause a character to join the party.|
|BA | unobserved_B8 | ubB8 | _Unobserved_|
|BB | unobserved_BB | ubBB | _Unobserved_|
|BC | unobserved_BC | ubBC | _Unobserved_|
|BD | unobserved_BD | ubBD | _Unobserved_|
|BE | unobserved_BE | ubBE | _Unobserved_|
|BF ... 40 | change_zone (...) | zone (...) | Change zone (wipeeffect,zoneport, flags)|
|C0 | unobserved_C0 | ubC0 | _Unobserved_|
|C1 ... 40 | set_bit (...) | set (...) | setbit(object,whichbit)|
|C2 ... 40 | clear_bit (...) | clear (...) | clearbit(object,whichbit)|
|C3 ... 40 | unknown_C3 (...) | unC3 (...) | In 1A07, Ascertainment, (48 09, 0x1d, 0x1f4)|
|C4 ... 40 | test_bit (...) | test (...) | testbit(object,whichbit)|
|C5 ... 40 | emit_signal (...) | emit (...) | emit(id)|
|C6 | unobserved_C6 | ubC6 | _Unobserved_|
|C7 | unobserved_C7 | ubC7 | _Unobserved_|
|C8 | unobserved_C8 | ubC8 | _Unobserved_|
|C9 | unknown_C9 | unC9 | Seen in 0D01, how much money has the player|
|CA | unobserved_CA | ubCA | _Unobserved_|
|CB ... 40 | unknown_CB | unCB | two parameters. 109E|
|CC ... 40 | unknown_CC (...) | unCC (...) | Seen in 0987, two parameters <10000002>, 1|
|CD | unobserved_CD | ubCD | _Unobserved_|
|CE | unobserved_CE | ubCE | _Unobserved_|
|CF | unobserved_CF | ubCF | _Unobserved_|
|D0 | unobserved_D0 | ubD0 | _Unobserved_|
|D1 | unobserved_D1 | ubD1 | _Unobserved_|
|D2 ... 40 | play_note (...) | note (...) | note(instrument, pitch, duration?)|
|D3 ... 40 | play_sound (...) | snd (...) | sound(which,x,y)|
|D4 | unobserved_D4 | ubD4 | _Unobserved_ Looked for.|
|D5 | unobserved_D5 | ubD5 | _Unobserved_ Looked for.|
|D6 ... 40 | unknown_D6 | unD6 | Observed in 180D, 140C|
|D7 ... 40 | play_sound2 (...) | snd2 (...) | Difference with D3 unknown. Random variations?|
|D8 ... 40 | set_ambient_lighting (...) | lighting (...) | Takes a byte parameter, negative is dark, positive is light.|
|D9 | unknown_D9 | unD9 | seen in zone scripts, single byte parameter - maybe play music?|
|DA ... 40 | set_title (...) | title (...) | Sets the title of the main view window. Usually in zone scripts.|
|DB ... 40 | has_window (...) | hwind (...) | Has the prop a window?|
|DC ... 40 | check_state (...) | check (...) | 1825, tracking plot events.|
|DD ... 40 | set_state (...) | state (...) | Setting plot state.|
|DE | unobserved_DE | ubDE | _Unobserved_|
|DF | unobserved_DF | ubDF | _Unobserved_|
|E0 | unobserved_E0 | ubE0 | _Unobserved_|
|E1 ... 40 | magic_aura (...) | aura (...) | whom,color|
|E2 ... 40 | shoot_effect (...) | shoot (...) | src_x,src_y,dst_x,dst_y,tile_id, ?, ?, optional?|
|E3 ... 40 | unknown_E3 | unE3 | Door script, bashing down door (self.x,self.y,0x1B2)|
|E4 | unobserved_E4 | ubE4 | _Unobserved_|
|E5 | unobserved_E5 | ubE5 | _Unobserved_|
|E6 | unobserved_E6 | ubE6 | _Unobserved_|
|E7 ... 40 | unknown_E7 (...) | unE7 (...) | Seen in 1801, bad end, single byte parameter. Seen in 113F Brazier with (1). (flash of light?)|
|E8 40 | unknown_E8 () | unE8 () | See [Distiller Script](Distiller-Script)|
|E9 40 | unknown_E9 () | unE9 () | See [Distiller Script](Distiller-Script)|
|EA 40 | unknown_EA () | unEA () | In 1832.|
|EB 40 | unknown_EB () | unEB () | 1802 magpie tour|
|EC 40 | unknown_EC () | unEC () | in 1801|
|ED 40 | unknown_ED () | unED () | Seen in 1801 - bad ending|
|EE ... 40 | unknown_EE (...) | unEE (...) | Seen in 1801. Seems to take an indexed resource (3iiirrrr) as parameter|
|EF | unobserved_EF | ubEF | _Unobserved_|
|F0 ... 40 | unknown_F0 (...) | unF0 (...) | 1afe, 5 integer parameters|
|F1 ... 40 | unknown_F1 (...) | unF1 | 1802, magpie plays tourguide, 1afe, regroup action|
|F2 ... 40 | add_quest (...) | quest (...) | Works with a 0x3000xxxx+n string table reference, not a string directly.|
|F3 ... 40 | unknown_F3 (...) | unF3 (...) | 1825 starting gator boots, 1025 crolna, other places|
|F4 ... 40 | add_keyword (...) | keyword (...) | Add a keyword to the suggested prompts the player can click. takes a string._Untested_|
|F5 ... 40 | get_skill (...) | skill (...) | skillhaver,skillID|
|F6 ... 40 | unknown_F6 (...) | unF6 (...) | two parameters, 1141 crystal ball|
|F7 | unobserved_F7 | ubF7 | _Unobserved_ 40check|
|F8 | unobserved_F8 | ubF8 | _Unobserved_ 40check|
|F9 | unobserved_F9 | ubF9 | _Unobserved_ 40check|
|FA | unobserved_FA | ubFA | _Unobserved_ 40check|
|FB | unobserved_FB | ubFB | _Unobserved_ 40check|
|FC ... 40 | unknown_FC (...) | unFC (...) | 1cc3, Omen gives automap  (true)|
|FD ... 40 | unknown_FD | unFD | _140a and other outdoor? location scripts. one byte parameter_|
|FE | unobserved_FE | ubFE | _Unobserved_ 40check|
|FF | unobserved_FF | ubFF | _Unobserved_ 40check|




## Opcodes by function

The opcodes are listed here by their category, and only relatively well-characterized opcodes are listed. 


#### load_word_from_res


|49 rr rr ii ii | load_word_from_res r i | ldwr r i | Loads a word from resource r at offset i|
|-|-|-|-|



* - Cannot directly refer to savedgame resources (tried with E000, journal entry) - But it can load data ultimately stored in the saved game (e.g. player gender 49 05 00 00 10) - Can refer to arbitrary data file resources - when seen in the game it seems to refer to Script Data / Static Data in  the scenario file (03xx, 05xx).  - Resources with these IDs do not exist in the saved game file and the original versions in the scenario file seem to primarily be placeholders - e.g. the player's gender is in 0500:0010 and is a boolean, but 0500:0010 contains only zeroes. 