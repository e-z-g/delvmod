
Brushes are a feature of the original Delver editor that allowed one to set down things like rivers and walls without manually specifying each tile to be used. They are only part of the editor and not part of the game; the eBRS resources in the [Cythera Data](Cythera-Data) file can even be deleted without apparent consequence. There are 25 eBRS resources in the file, all of which have human-readable names like "Adobe Wall, Grass" or "Seldane Walls". Incidentally, the presence of variations like "Adobe Wall, Grass", "Adobe Wall, Dirt", "Adobe Wall, Wood" and "Adobe Wall, Brick" suggest that the choice of wall is intermingled with its choice of ground type, at least at the level of the map. Are they intermingled at the level of graphics? It remains to be seen.  

As of this writing, it seems more likely that tiles can be composed, e.g. tree + grass or adobe wall + dirt. Where the values seen in the editor brushes are mapped to definitions of tiles remains to be determined - the values seen in the brushes don't seem to be found in the suspected maps. 


## Data Format

They are all 32-byte resources, appearing to contain 16 2-byte integers with the most significant byte equal to zero, similar to [Delver editor stamp](Delver-editor-stamp). The integers probably identify terrain tiles, and the editor knows their joining rules. Unfortunately, it is at least theoretically possible that the values seen in the editor brush are not global constants across all maps. 

![](Delver-editor-brush/eBRS.png) 
