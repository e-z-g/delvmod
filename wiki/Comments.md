
Stuff gandreas has said. 



```
Top that off with the fact that my time is spent doing that as well as tech support to everybody (and the scripting system isn't simple - how well do you know how to do object-oriented programming (using a combination of generic functions with a limited mix-in architecture) in a multi-threaded environment?) I'm not busy making the game better.
```



```
Tue Nov 5 13:50:23 1996
    Besides voting, got "conditional schedules" working - this allows me to have someone say "Meet me at the graveyard at midnight" and then, and only then, will that person be at the graveyard at midnight. Basically, entire populations can behave differently based on external state. I'm also amazed at the number of people reading this, since not even altavista knows about it... 
```

In Odemia. 



```
Wed Dec 18 14:48:04 1996
    Found another nasty bug in the scripting compiler - if a "for" loop was used twice in the same file but in different routines with different number of local variables, it would overwrite one of those variable or hose the loop. I can now throw attack something from a distance and it correctly knows to throw my spear at it... 
```

Stuff Andrew said (known bugs): 

```
Here are the known bugs we've accumulated for Cythera -- we are working
actively to fix these problems, and I am upset that Cythera was able to
make it out of beta test with these issues still pending, but
unfortunately, it happened.

If you have any other *serious* bugs to report (not typos, etc.) that are
impacting your ability to play or enjoy the game, please let me know.

.....

-- If there's a closed door with an item on the same space, you can't open
the door until you move the item. This becomes a particular problem if the
item is blood.

-- Cythera seems to access the hard drive every step a person takes, if
there is someone else in their party.  As a wild guess, are you calling a
Registration_Tool routine (RT_IsRegistered()?) each frame?  If so, erm,
don't -- it accesses the disk, nothing is cached.  Many people are not
bothering with the game because of this.

-- If you have more than one monitor, dragging items causes them to paint
trails on the screen

-- Cythera doesn't work properly without QT installed, nor does it work
with QT 2.5 installed (it crashes in both cases at different places in the
game)

-- The Cythera application should be given more memory; people are running
out of memory and losing their progress, which needless to say is very
bad.  People are also crashing after opening crates, and getting "Out of
persistant memory storage" errors.

-- There have been a number of scenerio bugs (door blocked by a dagger,
for instance) and typos ("I am a warrior, at least one will be, like
father" from Hector and "and it will envelope you" in the intro, as
examples) reported to the list; I assume you'll track them and fix them.

-- Cythera doesn't work with the Logitech Mousekey -- the game is
completely unplayable, nothing can be dragged.
```
