
_B:_ This page is a commentary on gandreas' document about the Delver Engine's internals, titled "Delving into Details." Some typographical errors have been corrected. Formatting is mine. Unattributed text is Glenn's. 


## Introduction

The Delver engine provided a fairly rich world model, and was designed to be the last "tile based" RPG that I'd ever want to write. In many ways, it was modelled after Ultima 6, both in terms of its capabilities (though it exceeded those) as well as the the "look and feel" of the world it could produce. The engine also had performance constraints (it needed to run on 68K machines, and run in about 10-12 meg of memory) 

_B:_ The visual resemblance between the 1990 game _Ultima VI_ and Cythera is strikingly obvious, including details such as the florid red dirt and choice in graphical perspective. The resemblance to the tile-based _Ultima_ games runs deeper than the appearance - many capabilities of the Delver engine are clearly designed to support an _Ultima_-like RPG, and Cythera is designed to showcase these capabilities. (The town of Odemia particularly stands out as a sort of Delver-Engine "sampler," illustrating the engine's capabilities with NPC schedules and interactivity.) 

_B:_ Glenn started writing Cythera in September of 1995. (It was not picked up by Ambrosia until later in its development.) At the time, Apple's computer line was already dominated by PowerPCs, although a substantial installed base of 680x0 based Macs existed. The decision to target these computers would clearly prove problematical for the development of Delver, and, by extension, Cythera - directly in terms of the time spent preparing a 68k version, and indirectly in terms of the optimization choices the decision engendered.  


## Concepts

There are a number of different areas in the engine, but the two major ones are the renderer and the object system. There is also a scheduler, and a planning system, as well as a file & memory system (which won't be discussed). 

_B:_ The file system is [well-understood.](Delver-Archive) 


## Renderer

The most visible thing, of course, is the renderer. It is the thing responsible for drawing what you see in the map view. There are two basic components that works with - "ground tiles", and props - both of which are composed of 32x32 pixel tiles. Ground tiles form the grid that the world lives on. Props are everything else - from doors to food to monsters. 

The ground tiles were stored in a grid (map), and the props were a list, and these two things together formed a "level" in the game. The map was considered static data, and never changed (and so was kept in the scenario data), while the prop list was considered dynamic, and was then kept in the player saved game data. 
### Tiles

Tiles, in general, are normally drawn as a single 32x32 icons, with some associated properties (such as "blocks movement", "blocks vision", "generates light", the name of the tile). Tiles can also be "multi-part" (which is only used for props) - for example, a horizontal door is composed of two tiles stuck together to form a single larger 64x32 tile. Multi-part tiles can be as large as 64x64 (things such as trees are done with this). There were around 8192 tiles (?) 

There is also a special "composite" tile (used only for the ground tiles) that is actually made by "slicing & dicing" existing tiles into smaller, 8x8 tiles, and gluing them back together. This allow us to make a large variation on ground tiles to help hide their grid like nature 
### Ground titles

Ground tiles also could have a prop "glued" to them (these were termed "faux props" because they were not persistent like other props). This was introduced later in the game, which is unfortunately, because if they were used more it would allow for more general "static" props. A good example of faux props were the mountains and forests - the mountains were entirely faux props (since they extended up beyond their own tile), and forests composed of trees (originally, these were different tiles that just looked more like a standard forest in a tile based game). 

Ground tiles were then all stored in a fixed array (which was the size of the current level). Every square in the map needed some sort of ground tile - even if it was the "transparent" one that allowed you to see the black void that is underneath every single level. 
### Props

Props, on the other hand, are stored in a list. Each prop had a location on the underlying grid formed by the ground tiles, as well as a object ID & aspect. The object ID was used to map to which specific tile. The aspect would then be added to that tile ID to tell the renderer what tile to draw (and if that tile included the various multi-part bits, the resulting object would span multiple tiles). 

The object ID would also associate a tile with the scripting object system (which will be discussed later). Props also had several additional fields used for storing persistent data with that prop - two single byte values ("d1", "d2", which could be treated as a 16 bit value "d3") a reference to another prop, and a general storage reference (which was kept in the persistent memory storage - this kept things that didn't fit in 2 byte data, such as the on screen window location for an open container). This general storage reference mechanism could have been used more heavily, but fortunately wasn't (since the persistent memory system had some "issues"). 


### Reshaper

One key feature of the renderer was the way it handled line of sight. If you were on the wrong side of a wall, you couldn't see stuff on the other side - which is no big trick. The interesting thing is that if that wall had another wall perpendicular to it that you couldn't see (forming a "T" where you were north of it) if you just drew the wall, at that junction you'd see part of the wall on the other side. Instead, the renderer would "reshape" the wall to appear as a single straight line (also removing props that would hang on that other side of the wall while it was at it). All tiles used for walls has special "shape" bits associated with them (so the renderer would know if the wall extended in various directions, among other uses), and there was also a "reshaping" table which would be used to remap a "t" shaped wall into a straight one if the bottom part wasn't visible. 

Combined with the reshaper was the line of sight routines. These were actually quite simple - a flood fill was performed from the current character, spilling out until blocked by a tile that doesn't allow vision (one of the flags on a tile) or the edge of the field of view (which was +/- 15 tiles away, so the flood fill could be done on a series of long words to form a bit mask). There were also special "window" bits on tiles which would work like "blocks LOS" bits unless they were immediately adjacent to the player (and so you could see through a window into the next area if you were next to it, otherwise you couldn't). The "remove props that you can't see on the other side of the wall" turned out to be a major problem to get correct (especially getting ladder placed on narrow walls in some of the caverns to work correctly). 

One could also do a series of "ray casting" to produce what is actually visible, but that normally produced a series of stair-step diagonals when you come to a corner (which is ugly) and there are other issues, especially in large fields of view when looking down a narrow hall, where part of the hall would block what is next to it (incorrectly). 

The way that LOS was handled proved to be quite satifying. 
### The "hood"

Since there could potentially be a large number of props on a level (consider the outside world, which is all one big level), having to go through all of them when drawing the view resulted in a whole lot of things never being drawn - each and every frame. 

As a result, an intermediate cache was created, to contain just the props found in the "neighborhood" of the player. This "hood" also contained all the faux-props that were associated with ground tiles that occured in the hood (and so faux-props were never actually part of the prop list associated with the level). 

The hood was reconstructed every time the player passed a certain larger underlying grid system. An alternate scheme of breaking the level down into "chunks" and having prop lists associated with their underlying chunk was also considered, but would be more useful in a large, continuous, single scale type of game. 
### Sorting it out

One important aspect of the renderer, besides determining what might be seen via LOS (and reshaping the tiles accordingly) was to keep the props sorted. They were sorted in esssentially two ways. One was the X/Y coordinate of the prop, so multi-tiled props that were "anchored" south/east of other multi-tiled props were drawn after those to the north/west (so two adjacent large wine vats would overlay correctly). It was possible to come up with situations where three items could overlap each other in a circular fashion, but this never came up in practice. 

The other way that things were sorted was by layer. Tiles had various bits associated with them that indicated what "layer" it was in (there were about half a dozen of them - floor, shadows/rugs, small/low items, large item, flying objects, high layer). The renderer would draw things from the bottom up, sorted as above. This allowed a rug to sit on top of the floor, with a key on top of it, underneath a flower pot. Or a vase to sit on top of a table. 
### Other effects

There were several other special things that the renderer did - one important one was handling lighting. There would be a light map created based on several factors - the general ambient light (which would change from day to night), the player spot light (which allowed for different intensity lights that the player would have), and individual light producing objects (which included glowing lava, candles, torches, and the like - since this was based on tile flags, both general props as well as ground tiles could produce light). Lights would also flicker - the "light map" produced by various light sources had several variations that would randomly be picked from. 

These were all combined to produce a grid of light (which was finer than the tile grid, but not to the pixel level). After rendering the scene, the renderer would post-process this by applying a darkening filter based on the light level of the light grid to all the pixels in that grid, producing the final lighting effect. 

There were other post-process effects that could be applied in a similar manner, such as producing a "grayscale" view (which, combined with turning off LOS could produce a nice "x-ray vision" effect). 

The engine relied on a trick called "palette animation" for a number of simple effects (such as the lava, or waves in the water) where colors for certain indices were iterated through - provides a simple way to do pulsing magic, lava, or waves, but not much beyond that. The renderer, however, also had tile based animation - certain tiles were automatically substituted for other tiles at render time (based on a the time, so it was synchronized). This is how flags, for example, would flutter. 

There was one additional effect that was done - the pixel distortion effect. This was used to mimick leaves blowing in the breeze, or to add some complexity to the waves. This had to be applied to tiles as they were being plotted (again, a tile flag would say if it was distorted or not). As it was being plotted random pixels would be distorted a pixel one way or the other. A little touch, but added a lot of effect. 
## Object System

The object system is built on top of the prop list discussed above, with a scripting engine interfaced to it. It handles almost everything that isn't done by the renderer (or specific to the UI handling - windows, dragging, mouse movement, etc...). 

One important concept is that not all props can/will be drawn - and not all props exist "on" the map. The prop list is used not only for those props drawn by the render, but also inventory management - there are flags that indicate where this prop is (if it is a normal "on map" prop or something else). If an item is taken by the player, this flag is set to "in character inventory" and the location changed to reflect what character is holding it. If that item is then worn/wielded, the flag is changed to "used by character" (and then window that shows the character knows that this item is worn on the head, for example). 

Other possible values for this flag include "inside another item" (in which case it points to object it is contained within). Props can be "hidden" (simply not drawn, but otherwise treated like any other prop) - this is how traps work (they are hidden, but when you step on them, boom). 

And then there are "eggs". There are a number of different kinds of eggs, but basically, these are used to cause something dynamic to happen. The most common sort of egg is used for "random monsters". Monster hatching eggs can be set to go off during the day, night, and with a random chance, or only once. There are then a bunch of monsters that are "inside" this egg (just like a chest can contain items, eggs contain monsters). This is the only way for a monster to be created (if you were to try to make one as a prop, it would be just that - a prop that doesn't do anything). 

There are also eggs that produce sound (for example, sea shore waves crashing), eggs that cause special triggers (something happens when you approach an area), and similar things to handle "room descriptions" (where a given rectangle is a "room" object that gets a message sent to the object system when the character enters/leaves, which is how a description can be done when the player enters an area). 
### Monsters

As mentioned above, monsters are created from eggs. All monsters have general abilities/stats associated with them, and also an "age" which causes these values to be scaled (ranging from 50% to 200%). Besides these stats, there are flags (such as "immune to heat", "regnerates", etc...) an object associated with it (so we know what prop to create), and a "general behavior". This general behavior is important - it determine who will attack what (and what the player would get into trouble for attacking). There are four basic values: 

         * Good - player attacking this causes repurcusions, will attack evil on sight. Evil - the opposite of good - will attack good on sight. Neutral - will not attack anything unless given a good reason, and will simlarly not be the target of attack (most townspeople are neutral). Attacking them, like attacking a good character, causes repurcusions (they yell for help, for exampe). Chaotic - most wild animals are this - they don't attack unless attacked first, and will often just run away, but you can attack them.  
Monsters are also associated with the underlying object system - when a monster is created, it can be sent a number of messages, including "it's your turn to do something, so do something already". Part of this is based on the "general behavior" mentioned above, but beyond that the monster object is able to decide what kind of attack to take (spell or physical combat, etc...). 
### Characters

Characters are essentially props that get time to do stuff and have extra state associated with them. The main player is a very special character - it is controlled by the player. Every individual in the game is a character - they (usually) have a portrait (so you can talk to them, or see them in a window), stats associated with them, and a whole lot of scripting code & properties as well. 

Characters are also props, or else they wouldn't show up in the game view. All characters are props, but not all props are character. In fact, only the first 256 props are characters (there are 256 possible characters). Even if there aren't all 256 characters (actually 255, since character 0 is a special "none" character/prop) on the current level, the first 256 entries in the prop list are for the characters (as a result, the save game doesn't save the these character props with the level, but separately - they are essentially "global" props). 

Oh, and all of the stuff above about "monster objects" is also misleading. While there _are_ monster objects, they are actually "temporary" characters (and so have all the stats, state, and the like that any other character might have), and that's what makes them tick (and it actually is a character that is created when an egg is hatched). All characters then have a monster template associated with them (so yes, there are "hero" monsters). So, the render draws tiles. What tile to draw is based on the prop's object ID (which gives a tile number) and aspect (which is added to that number). Props 0-255 also have character data associated with them. That character data includes a reference to the monster data. That monster data includes an object ID, though the prop associated with a character might actually have a different object ID (and thus different tile). When an egg containing a monster is hatched, the monster data is used to create the character entry and its equivalent prop, which includes what object ID to use. So all characters are also props, not all props are characters, props (and thus characters) have an (item) object associated with them, and characters also have a monster (object) associated with (which in turn have objects associated with them), but monsters are not objects and neither are props - got that? 
### User Interaction

Pretty much all of the user interaction would end up boiling down to the scripting system. When the player tried to use an item, take something, attack, cast a spell, use a skill - all of them would be handled in the scripting system. Originally, these things were to be handled in the engine itself, but that limited the flexibility (and since code needed to be written to handle these things anyway, might as well write it at the layer that allowed the most "bang for the buck"). 

Other than a few major UI items (the map view, "control bar" at the bottom of the screen & associated to-do/journal windows, character windows) the rest of the UI was run by the scripting system. This included custom shaped window, which might contain "inventory lists" or they might have "buttons" that could be pressed, allowing anything from a sack to a musical instrument. 

Even the conversations and other modal dialogs were handled by the scripting system. The conversation was obviously provided in a "fixed" format (and the list of available conversation words was handled by the engine), but other modal dialogs was all done in the scripting layer. This allowed simple things like asking a question with multiple choice (like how long to sleep) to more complex things like the shopping interface (complete with haggling). 

The real flexibily shined in the use of objects. When somebody would try to use an item, the scripting system would determine if this was something that could just be used "as it" (such as openning a door or container) or if it needed a secondary thing (such as what to use it on - be it a location, another item, or both). Ultimately one of three different scripting methods for the object would be executed ("Use", "[UseOn](UseOn)", or "[UseAt](UseAt)"). Since everything at that point was done in the scripting layer, a wide variety of effects could be achieved, including baking bread. Roughly, you'd use the sack of flour at a location, which would produce a pile of flour there. You'd use a source of water (there could be several) on that pile of flour, which would then convert the flour into a pile of dough. You'd use the rolling pin on the dough which made a raw piece of bread (assuming you had a cooking skill), which you'd then use on the stove, which would change that to bread. 
## Schedules

One key part of the Delver engine is the use of schedules to have different characters do different things at different times. There are actually two layers of schedules - one is the "larger" time based schedule, and then there is also a "smaller" action based task list. 

The time based schedule is used to determine where that character will be when. It includes the ability to specify random information (to add some variety) as well as look at special global variables (which are shared with the scripting system), so people can change where they are based on different key events in the game. Besides being at a specific location at a specific time, they were then given a "task" to perform. Simple things would be to just stand (or sit) there, or randomly roam about, but those proved to be of limited usefulness. 

As a result, there was then the concept of a task list. A good example would be a blacksmith - they would go between different parts of the shop to perform their tasks. For example, they would get wood from the woodpile, work at the forge, take something from the forge and dunk it in a tank of water, etc... Another example would be a waitress who goes between tables and the kitchen getting an order. 

These tasks were actually handled in the scripting system, and there was a list of pending tasks to be performed (with a special signal that would be handled in the scripting system when it happened). This would allow somebody to "flag down" a waitress and order food. That food order would result in several tasks being queued up - first coming over and taking that order, then going to the kitchen to get the food, and then returning with it and giving it to the player. Afterwards, they would return to their (semi-random) series of tasks. 

Schedules added a lot of depth and interest to the game - making it feel like the NPCs had a life of their own. When the task list was added on top of that, they actually felt like they did something with that life instead of just sit around or wander aimlessly. 
## Conculsions

There was a lot of power and flexibility that eventually ended up in the Delver engine, due to the ubiquitous use of the scripting system to handle behavior of both the in-game items, as well as the UI. The rendering system was capable, but in the end would suffer due to the large granularity of the underlying grid system (which was a side effect of the original design of a "tile based game"). Also, the flat, 2D nature of the world limiting as well (though that did allow for a simple "layer" system for objects that mostly worked well). 

If done again from scratch, many of the concepts would be kept exactly as is, but the world would be upgraded to have at least a concept of "height" (if not a true 3D structure), and the granularity of the world would be refined. It's unclear exactly what else would be added to the renderer (I suppose this would depend on the availability of resources for such an undertaking). 

I don't know if I'd want to "re-invent" another scripting system or use some off the shelf solution such as Python or Lua. Obviously the scripting system used here had a very good "impedence match" with the rest of the game (since they were co-evolved - the scripting system was re-written from scratch several times). On the other hand, using an existing system would save a great deal of time. 

The scheduling system would be a mixed bag - it did a lot, but was often very difficult to use. Some of those problems, however, were intrinsic in the basic nature of the task list - if you ever try to coordinate tasks between multiple characters, you can easily get deadlocked (which is why there wasn't a whole lot of that) 

Certianly I'm quite happy with the ability of the Delver engine to produce a rich environment, populated by people who have their own "lives", and the dynamic nature of the world was quite satisfying. 
