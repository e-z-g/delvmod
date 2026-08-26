
A problem in decyphering the Delver scripting system is how strings are stored. 

Often, it's something like this 

```
0x44 "A null-terminated string"      <- push a cstring onto the stack
```

And all is good. 

But then we have this... 

```
3039:                             
    81 01 00                       New subroutine with one parameter and no local variables                
    You can't dig here! 0A         This prints a string to the console
    8B 41 00 40                    Return nothing (or possibly 0, but more likely nothing)
```

There are three bytes before the string begins, all of which is completely accounted for. The 0x0A is just a linefeed, leaving open the question of termination (perhaps any nonprinting character terminates it) but WHAT MARKS THE BEGINNING?  Why doesn't the VM execute Y (0x59) as an opcode? Granted, we don't know for sure that 0x59 is a valid opcode (0x5A is _left shift_, so it could be right shift or something) but many opcodes are perfectly valid ascii printing characters, e.g. 0x4A is the _add_ opcode, and the ASCII letter 'J'.  

This does not leave any nice possibilities that I have thought of so far: 

   * 'Y' is a special case. (And at least ' ' is also handled this way, if so.) 
   * The VM sees the local stack is empty and infers that it can't be an opcode 
   * The default is string-to-output, not code or even string-to-stack (although perhaps it is string-to-stack and the caller is printing it.) 
It also appears that many things besides 0x00 can terminate a string, including at least 8x series opcodes - perhaps any nonprinting character. This falls more into the expected range of weird optimizations, though. 


## Mutations



```
3039:                             
    81 01 00                                       
    44 You can't dig here! 0A        
    8B 41 00 40                   

Output:
DYou can't dig here!
```



```
3039:                             
    81 01 00                                       
    44 You can't dig here! 0A Foo 0A      
    8B 41 00 40 

Output:
You can't dig here!
Foo
```



```
81 01 00 "You can't dig here! 00 Squirrels 0A 8B 41 00 40

Output:
You can't dig here!Squirrels
```



```
81 01 00 "You can't dig here! 00 Squirrels 00 8B 41 00 40

Output:
You can't dig here!Squirrels
```

Substituting 00 for 0A results in no linefeed. Omitting it entirely has the same result. 

Putting an address right after 81 01 00 resulted in it being printed. 8D seems to be the if-statement. 

```
8D (code leaving truth value on top of stack) 40 ADDR ; Branch to addr if true. 
```

0 is false and 1 is true, at least. 



```
88 ADDR
```

Branch unconditionally to addr. Parser will be in stringmode when it gets there. N.B. no termination (0x40) required. 



```
82 nn 40
```

Local variable assignment 
