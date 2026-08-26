
Iterators in the scripting system are implemented as system calls that take a local variable passed by reference as the first parameter. (The syntax is `&Foo` in [RDASM](RDASM); the binary format is `0x10000000|(local_variable_number + 1)` )  


### Iterator Methods

Rather than being separate system calls, each iterator takes an integer argument that tells it what "method" of the iterator is being invoked: 


|**Second Argument** | **Interpretation** | **Arguments**|
|-|-|-|
|0 | Iterator.Begin | Loop variable reference, method ID, other parameters depending on iterator type.|
|1 | Iterator.[IsFinished](IsFinished) | Loop variable reference, method ID|
|2 | Iterator.[GetNextItem](GetNextItem) | Loop variable reference, method ID|



The return value of Iterator.Begin is the first item to be looped over, so [GetNextItem](GetNextItem) should be at the end of the loop. [GetNextItem](GetNextItem) puts the next item into the local variable directly, and does not require an assignment.  


### RangeIterator (0xA0)



```
    loopvar MyLoop ; necessary to allocate extra space for the iterator.
    setl MyLoop
      sys System.RangeIterator
        word &MyLoop
        byte Iterator.Begin  
        byte 0      ; Initial value
        short 300   ; One more than the highest value the loop will reach.
                    ; i.e. 0 <= MyLoop < 300
      end
    end
```


### ArrayIterator (0xA1)

Iterates over the items in an array.  

```
    loopvar MyLoop
    setl MyLoop
      sys System.ArrayIterator
        word &MyLoop
        byte Iterator.Begin
        loc MyArray
      end
    end
```


### PropListIterator (0xC7)

Iterates over all the entities in the proplist, which will include both the global / characters proplist, every prop in the zone, and everything in inventories. 


### ContainerIterator (0xC8)

Iterates over items in a container (e.g. a crate). It can be applied to a character, in which case it will iterate over all his or her items and inventory, as well as skills / spells, which will be interpreted nonsensically as items. 



```
loopvar MyLoop
    setl MyLoop
      sys ContainerIterator
        word &MyLoop
        byte Iterator.Begin
        loc MyContainer
      end
    end
```

 


### RecursiveContainerIterator (0xC9)

As a [ContainerIterator](ContainerIterator), but it descends recursively through the contents of containers within the container. 


### PartyIterator (0xCA)

Iterates through the current party members. The meaning of the third constructor argument is unclear. It's `true` in the whole corpus except for `1827` , `0EA9`, and `0EA2`. 



```
    loopvar MyLoop
    setl MyLoop
      sys PartyIterator
        word &MyLoop
        byte Iterator.Begin
        word false ; ??
      end
    end
```


### LocationIterator (0xCB)

Iterates through all props at a given X,Y location. 


### EquipmentIterator (0xCC)

Iterates through all equipped items of a character. 


### EnemyIterator (0xCE)

Iterates through all enemies a character. Seems to work for all party members, but not for monsters.  


### EffectIterator (0xCF)

Iterates through all characters (and only characters) caught in a recent [ShootEffect](ShootEffect).  


### NearbyIterator (0xD1)

Iterates through all nearby props around a given X,Y location, within a specified distance. The distance is in terms of squares, but it is apparently properly computed, so e.g. a diagonal square is ~1.4 units away, not 1. 
