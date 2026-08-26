
_This is out of date. Go here [RDASM](RDASM)_ 

rdasm2 is an assembly language for the [Delver Virtual Machine](Delver-Virtual-Machine) 


#### Syntax

In common with other assembly languages, the general format is to have an opcode on every line, optionally followed by arguments, e.g: 

```
push-string "Ouch! That hurts!"
push-byte 0x20
close 
```


#### Comments

Any text on a line after a pound sign (#) is ignored as a comment. 


#### Literals

Integers can be written in hex, prefixed with 0x in C style (e.g. 0x20 = 32), or in decimal (e.g. -40).  


#### Symbols

Symbols are substituted with values known at assembly-time. Pseudo-opcodes can define symbols: 

```
define CONSTANT 42
```

Symbols can also come into being as labels: 

```
mylabel:
  push-string "test"
```
