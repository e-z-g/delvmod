
A pattern of related terrain one could place down in one step using the original Delver editor.  

Its use is usually more subtle than seen in the example screenshots. 

Stamps are stored in the [Cythera Data](Cythera-Data) file, resource type [eSTM](Cythera-Data-eSTM), and might provide a clue as to how terrain tiles are identified internally. Stamps are _only_ part of the editor, for convenience in making maps; altering or even deleting them has no effect on the game. 

![](Delver-editor-stamp/stampmap.png) ![](Delver-editor-stamp/stamp1.png) 

Screenshots from Cythera, copyright 1999 Ambrosia Software, inc. 


## Examples

Of the 16 known eSTM resources, 15 are 132 bytes in length and one, ResID 128, is 164 bytes. The first three resources, 128-130, have generic names; the others all have identifiable human-readable names like "Forest Medium 1" or such.  


## Data Format

The eSTM resources known (including the one of odd size) all begin with 0x0008 0x0008, probably the dimensions of the stamp. This takes up 4 bytes, leaving 128. The next 128 bytes appear to be two-byte integers (i.e. shorts), meaning 64 data items. Probably not coincidentally, this corresponds to an 8-by-8 array of short ints, which are probably some kind of terrain tile identifiers. Curiously, in the example eSTMs available to us, none with a most significant byte value other than 0x00 is seen. It may be that none of the higher tile IDs  happen to be used in the eSTM corpus, or there could be some more interesting technical reason. 

eSTM "Forest Medium 1", ID 2558 


| 00 08  |  00 08 |
|-|-|




| 00 4E  |  00 36  |  00 49  |  00 40  |  00 41  |  00 49  |  00 36  |  00 4A |
|-|-|-|-|-|-|-|-|
| 00 46  |  00 4C  |  00 35  |  00 42  |  00 43  |  00 4C  |  00 4A  |  00 46 |
| 00 4A  |  00 47  |  00 4A  |  00 4C  |  00 37  |  00 46  |  00 4A  |  00 49 |
| 00 4B  |  00 4A  |  00 34  |  00 48  |  00 34  |  00 35  |  00 4E  |  00 48 |
| 00 4A  |  00 40  |  00 41  |  00 4A  |  00 49  |  00 47  |  00 49  |  00 49 |
| 00 49  |  00 42  |  00 43  |  00 40  |  00 41  |  00 35  |  00 4A  |  00 47 |
| 00 4D  |  00 47  |  00 4A  |  00 42  |  00 43  |  00 49  |  00 40  |  00 41 |
| 00 37  |  00 4A  |  00 48  |  00 37  |  00 4A  |  00 36  |  00 42  |  00 43 |



Maping these with F004 we get: 


| =shrub  |  tree  |  dead tree  |  grass  |  grass  |  dead tree  |  tree  |  dead tree |
|-|-|-|-|-|-|-|-|
| grass  |  dead tree  |  tree  |  grass  |  grass  |  dead tree  |  dead tree  |  grass |
| dead tree  |  =tree  |  dead tree  |  dead tree  |  tree  |  grass  |  dead tree  |  dead tree |
| dead tree  |  dead tree  |  tree  |  dead tree  |  tree  |  tree  |  shrub  |  dead tree |
| dead tree  |  grass  |  grass  |  dead tree  |  dead tree  |  tree  |  dead tree  |  dead tree |
| dead tree  |  grass  |  grass  |  grass  |  grass  |  tree  |  dead tree  |  tree |
| scrub  |  tree  |  dead tree  |  grass  |  grass  |  dead tree  |  grass  |  grass |
| tree  |  dead tree  |  dead tree  |  tree  | dead tree  |  tree  |  grass  |  grass |



(Note, assuming the names are repeated) 

![](Delver-editor-stamp/stamps2.png) 

![](Delver-editor-stamp/stamps3.png) 
