
The scripting language used by Delver is known to us directly from only a single example of a subroutine written in it, the [GainExp Fragment](GainExp-Fragment), and the statement by gandreas that it was "like Python." 

Indirectly, we have many examples of _compiled_ Delver Scripts, in [Cythera Data](Cythera-Data), where they were first identified as the [81 ... 40 Script Type](81-...-40-Script-Type). It has been possible to decypher these compiled scripts independently of what was known about the Delver Script Language by careful analysis of their context and known functions. (E.g. figuring out how props and scripts were associated, and how method calls like "[UseOn](UseOn)" were dispatched to particular fragments of code; experiments with altering the code, and so on.) 

[redelv](redelv) can assemble [rdasm](rdasm) (and disassemble compiled code to it), but this assembly language is an invention of the redelv project - as far as is known, there was no analog of rdasm in the original [DelvEd](DelvEd) (although conjecturally, it might well have had some kind of symbolic debugging facility for scripts.) 
