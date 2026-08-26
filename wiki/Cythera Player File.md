
Cythera's player files hold information about the dynamic state of the game world, including the situation of the player character and party. These files are a [Delver Archive](Delver-Archive) and can be examined with [Narthex](Narthex), but their examination and modification by players far predates the successful interpretation of [Cythera Data](Cythera-Data). 

Long before the successful interpretation of Delver Archives, saved games (i.e. player files) were edited with methods described as [Cythera Save File Hacking](Cythera-Save-File-Hacking) by players. 


## Resource Fork

* PICT - One resource, contains the preview view of the game shown when opening a saved game. 
* pnot - One short resource, unclear binary data. 
* SCEN - Resource appears to contain a link to the associated scenario file on disk, although given the portability of Cythera saved games between computers, it isn't clear what this really does (perhaps it's simply ignored by Cythera.) 

## Data Fork Contents

* [Player File Subindex   2](Player-File-Subindex---2) - Contains one short binary resource. 
* [Player File Subindex   3](Player-File-Subindex---3) - 0400 contains a list of short strings, 0401 8-byte records, 0404 short binary thing. 
* [Player File Subindex 128](Player-File-Subindex-128) - Contains prop lists (just like [Cythera Data Subindex 128](Cythera-Data-Subindex-128))  
* [Player File Subindex 129](Player-File-Subindex-129) - Probably what areas have been explored already (for the automap), as a packed bitmap. 
* [Player File Subindex 135](Player-File-Subindex-135) - Contains the player's current portrait (so this can be modded without editing Cythera Data, interesting.) 
* [Player File Subindex 223](Player-File-Subindex-223) - Contains journal entries. 
* [Player File Subindex 239](Player-File-Subindex-239) - Most probably persistence data for the scripting system  
* [Player File Subindex 242](Player-File-Subindex-242) - F306 might be a prop list for the first 256 props/ characters?? Probably more persistence data. 