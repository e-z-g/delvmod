
Disassembly of the script 3000, tentatively identified as the default `__init__` method. Is there any proof that 40 is Character and not Monster? Maybe 48 = Character and 40 = Monster. 

Code injection has shown that this script is called when a monster is hatched from an egg. It is not called when some new objects (e.g. a potion) are created, but it was seen to be called when seedpods were created in the swamp. 

The istype clause is triggered when asps are created - the value of local0 is printed as "something (48/14)" For a seedpod, it is not triggered. For ruffians, local0 is "something (48/1)" 

3000 does not seem to be called for the equipment of the ruffians. It is called on obsidian. It does not appear to be called when the game starts, nor for Alaric giving the amulet. 

a tentacle : something (48/1f) 

It is called on chickens in Odemia ("something (48/1d)"), and as I entered, on a person sleeping (None), a guard (something (48/7), and interestingly, one in which the argument was 'something (48/7)' and the value of local0 was 64. 

The significance of the second part of the 48/whatever is not known for sure, but a goat is 48/16 and the goat is the 22nd (0x16) entry in the F008 table of monster stats. This pattern also holds for a ratlizard (48/18). So perhaps 48 is monster? 



```
function (arg0) {
  if (istype(arg0, 0x48)) {
    local0 = cast_48(arg0)
    if (local0) {
      call_method_00(local0, local0, arg0)
    }
  }
  return 0;
}
```
