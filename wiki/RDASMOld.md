
RDASM ([ReDelv](ReDelv) ASseMbly language) is an assembly language which delv can assemble into bytecode for the Delver virtual machine. It can thus be used to write scripting code for Delver-based games. It is believed that the original language used to write scripts for Cythera was a python-like language, as seen in the [GainExp Fragment](GainExp-Fragment). It is possible, though not likely, that this language was compiled into an intermediate assembly language, but if so, it is completely lost to us. The RDASM language is thus a creation of the delv project, not a part of Delver. 


## Modes

RDASM can operate in two modes, `object` and `direct`. In Direct mode, the output is a single entity of some sort (usually a `function`, but also e.g. an `array` or `table`). In Object mode, the output is, unsurprisingly, an object, which contains a dispatch table at the end and a pointer to the table's position at the beginning. Which mode is appropriate to use depends on what resource type the assembled code is going to be placed into. The `hints` module of `delv` knows which objects go where for [Cythera](Cythera). 


### Direct Mode

In direct mode, code is output according to its order in the source file. There is no header. Direct mode is specified with the keyword `direct` before any coding source lines, though as direct mode is the default, its usage is optional. 


### Class Mode

In class mode, the first two bytes of the output are the offset to a dispatch table containing an index of the object's fields, which is generated automatically from the contents of the source file. The assembled source is placed after the offset. Finally, the dispatch table is written out. Class mode is specified with the keyword `class` before any coding source lines. It takes a single parameter, the name of a definition that will be used for associating method/field names with keys. 


## Top-Level Structures

Top-level structures are ones that can be encountered in direct mode, or inside an immediate data operation. 


### Array



```
array (
  42
  "Foo"
  array(1 2 3)
  -19 -3
  "Bar"
)

```

Items in an array can be words, strings, or other arrays or tables. 


### Table



```
table (
   42:"bob"
   4:true
   78:array(5 6)
   0xabcd:table(4:3 6:None)
)
```


### String



```
"This is a null-terminated string."
```


### Function



```
function (arg1 arg2 argN) (
   set_local mylocal (
     push_byte 1
     push_argument argN
     add
   )
   return (
     push_byte 0
   )
)
```


## Classes



```
class DObj  ; puts the assembler into class mode
.Look: function (self) (
  return (
    push_string "You see a hamster."
  )
)
```


## Definitions, Includes and Comments

These are non-code-generating items. 


### Comments

Comments proceed from a semicolon `;` to the end of the line. 


### Includes



```
include 'cythera'
```

By default, the search path is delv's headers folder, which will be who-knows-where in your python installation. 


### Definitions

Definitions occur in header files mainly, though you can put them anywhere before they are used. These are simply constants or a family of constants with a symbolic name. There are two forms - one that will make a bunch of constants that can be accessed as [DefName](DefName).Foo as in the first example below, which can also be referred to by the `object` mode keyword. The other is for a single constant, as in the second example below. 

```
define DObj (
  Look: 0x0002
  Examine: 0x0008
  Use: 0x0009
  UseOn: 0x000A
  UseAt: 0x000B
  Talk: 0x000C
)

define gKarma 0x0C
```


## Literals



```
"This is a null-terminated string (i.e. a CString)"
'This is a sequence of characters with no termination.'
{DEADBEEF} ; This is a sequence of binary data with no termination.
           ; There may be spaces or '.' between bytes, e.g. {DEAD.BEEF} or {DE AD BE EF}

0 -3 +42   ; These are decimal integers
0x2A       ; This is a hex integer
0b00101010 ; This is a binary integer

<5000FFFF>      ; This is a Delver word literal. The digits are hex.
0x1337:0x32     ; Resource 0x1337, offset 0x32 - Assembles to <93370032>
0x1337[3]       ; Resource 0x1337, index 3 (only applicable to resources containing indexable items.)
                ; Assembles to <30031337>
true false None ; These are atoms
$0x0C           ; Assembles to <2000000C> (future)
&0x0C           ; Assembles to <1000000C> (future)

0x0006@0x40                 ; Assembles to <40400006>
Characters.Hector@Character ; Assembles to <40400006>, if you include 'cythera'



```


## Labels and Symbols

Valid first characters for symbols are a-z, A-Z, and _. Subsequent characters can also include the digits 0-9 and the `-` character. 

Labels are defined by following a symbol with a colon and placing it in the program text. A label beginning with a `.` will be local to the function in which it is defined. 


## Opcodes

Inside functions, opcodes occur. Broadly these can be divided into two categories, statements and others. Statements start with bytes (probably) 0x80 or higher, others are less. Only statements can occur at the 'top level' of a function, i.e. outside of a statement. Other opcodes only occur inside statements. If their (<0x80) values were to occur outside a statement, they would be interpreted as literal text and streamed to the console or conversation dialogue box (depending on the circumstances.) 

What exactly constitutes being 'inside' a statement depends on the statement. For example, the print statement has the format `8A ... 40`, and what's between the 8A and the 40 is "inside." Some other statements may have multiple consecutive insides, separated by 40, for example set_index has three, `84 ... 40 ... 40 ... 40`, corresponding to the array, the index, and the value to set it to. Other statements taking multiple parameters have only a single inside, and take more items from the evaluation stack than just the top. It is unclear why they are not all implemented in this way; there does not seem to be any good reason to have multiple stacks in a statement, but that's the way it is. 

In RDASM, each evaluation stack is represented by a set of parenthesis, thus we have e.g. 

```
; myArray[10] += 1;
set_index (push_local myArray) (push_byte 10) (
  push_local myArray
  push_byte 10
  index
  push_byte 1
  add
  )

```

Some opcodes contain immediate values as part of their binary format. For example, opcode ``push_byte xx`` pushes a byte onto the evaluation stack, and its binary format is `41 xx` where `xx` is the byte. These integers may immediately follow the opcode name, or may occur after the last evaluation stack is closed, e.g. `if_not (push_local var1) SKIP` 

The list [Delver Script Opcodes](Delver-Script-Opcodes) contains opcodes reverse engineered (or at least identified) before this version of RDASM was designed. [RDASM Opcodes](RDASM-Opcodes) contains the mnemonics used by RDASM. Most mnemonics have a long form and a short form; the long form is intended to be readable, the short form is easy to type. 
