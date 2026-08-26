
Contains short binary data with names of regions ("Odemia", "Omen's Test" and "Below Cademia" in the same resource, "Mountains") All encrypted, mostly quite short, although their length varies. 

They may be some sort of script that runs when entering a new zone. 

These resources refer to maps (i.e. resources of [Cythera Data Subindex 127](Cythera-Data-Subindex-127)) not by their full resource ID, as we might hope, but by either their index, i.e. the order the occur in the data file, or the LSB of their resource ID - we are at the moment unable to disambiguate between the two situations because it happens that all the Cythera maps are given consecutive resource IDs. The references appear to occur after the script (i.e. at the part pointed to by the offset at the very beginning of the resource) and are preceeded by 0x94. Some have two references. 



```
 ---- SUBINDEX 19 ---- 
                                          Associated map
Index 0, ID 1400 Length: 51 bytes         Map 8000
Index 1, ID 1401 Length: 218 bytes        Cythera 8001 (very long - rects with ambient noise?? check for them)
Index 2, ID 1402 Length: 136 bytes        Odemia 8002
Index 3, ID 1403 Length: 69 bytes         Land King Hall 8003
Index 4, ID 1404 Length: 64 bytes         Abandoned Farmhouse 8004
Index 5, ID 1405 Length: 54 bytes         Cellar 8005
Index 6, ID 1406 Length: 58 bytes         Catamarca 8006
Index 7, ID 1407 Length: 59 bytes         Underground 8007
Index 8, ID 1408 Length: 86 bytes         Cademia 8008
Index 9, ID 1409 Length: 59 bytes         Underground 8009 (Ayrit)
Index 10, ID 140A Length: 54 bytes        Ruins 800A
Index 11, ID 140B Length: 50 bytes        Ruins 800B
Index 12, ID 140C Length: 49 bytes        Pnyx
Index 13, ID 140D Length: 54 bytes        Kosha 800D
Index 14, ID 140E Length: 49 bytes        Pnyx 800E (upper story)
Index 15, ID 140F Length: 63 bytes        Iron Mine 800F
Index 16, ID 1410 Length: 61 bytes        Volcano 8010
Index 17, ID 1411 Length: 88 bytes        Charax House / Small House 8011
Index 18, ID 1412 Length: 53 bytes        Vineyard 8012
Index 19, ID 1413 Length: 67 bytes        Hall of Truth 8013
Index 20, ID 1414 Length: 53 bytes        Vineyard 8014 (southland)
Index 21, ID 1415 Length: 60 bytes        Sewers 8015
Index 22, ID 1416 Length: 49 bytes        Farm 8016
Index 23, ID 1417 Length: 89 bytes        Kosha Grotto 8017
Index 24, ID 1418 Length: 56 bytes        Mining Camp 8018
Index 25, ID 1419 Length: 292 bytes       Tomb 8019
Index 26, ID 141A Length: 64 bytes        Temple 801A
Index 27, ID 141B Length: 62 bytes        Cove 801B
Index 28, ID 141C Length: 67 bytes        Below Cademia 801C
Index 29, ID 141D Length: 102 bytes       Ruined City 801D
Index 30, ID 141E Length: 65 bytes        Ruined City 801E
Index 31, ID 141F Length: 61 bytes        Stronghold 801F
Index 32, ID 1420 Length: 61 bytes        Encampment 8020
Index 33, ID 1421 Length: 58 bytes        Dungeon 8021
Index 34, ID 1422 Length: 56 bytes        Caves 8022 (harpy)
Index 35, ID 1423 Length: 50 bytes        Caves 8023
Index 36, ID 1424 Length: 146 bytes       Stronghold 8024 (Tavara's disappearing fortress, including disappearing message)
Index 37, ID 1425 Length: 52 bytes        Cythera 8025 (Empty field - disappearing fortress)
Index 38, ID 1426 Length: 142 bytes       Bridge 8026 (unusually long)
Index 39, ID 1427 Length: 54 bytes        Mountains (Tree of life) 8027
Index 40, ID 1428 Length: 149 bytes       Below Cademia, Omen's Test (three 94xx references) 8028
Index 41, ID 1429 Length: 54 bytes        Mountains (actually Harpy cave, but it's called Mountains in the game too) 8029

```
