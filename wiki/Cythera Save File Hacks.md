
Sources of documentation obtained by editing save files: 

[To boldly go where no Cytherean has gone before](http://www.ambrosiasw.com/forums/index.php?showtopic=114332&st=0&p=1778525&#entry1778525) 


### Notes from BreadWorldMercy453



```
This is my instruction page for changing your sprite (& therefore, your special attributes) using Pandora's Box. I still have next to no idea how to use HexEdit. Pandora's Box is available for download off Cythera's addons page.
1) Make two save-game files, one with a male character and one with a female character. Open the male game.
2) With the game open, toggle to Pandora's Box. Search for the value 32 in Cythera under 'short's.
3) Toggle back to Cythera and open the female game (don't quit the program, it needs to stay open or Pandora's Box will lose the search)
4) Toggle to Pandora's Box and search for short values that changed to 33. If there is more than one, switch back and forth between male and female characters until you narrow it down to one.
5) When you've isolated the location, change the value to whichever sprite number you'd like to be.

Monster sprite number list (in alphabetical order... kind of):
Flying bird: 89
Ruffian: 47
Chicken: 228
Child: 79
Small crab: 349
Titan: 204 (be careful with that one, because of its awkward size it's easy to get stuck in stuff)
Demon: 295
Beggar: 50
Fighter: 116
Firesprite: 290 (296 is also a firesprite but it is not animated)
Fool: 35
Gator: 84 (front half only :()
Ghost: 289! (293 is also a ghost but it is not animated)
Zombie: 288
Slug: 208
Goat: 90 (goats physically can't go through their fences)
Guard: 46 and 229
Harpy: 291
Hero: 32
Heroine: 33
Hunter: 117
Hydra: 278 is one tile of its tentacles and 279 is the center tile
LandKing: 34
Giant crab: 91
Land jellyfish: 207
Lich: 297
Magess: 81
Mage: 80
Man in blue clothing: 82
Workman: 211
Noblewoman: 44
Nobleman: 45
Gecko: 348
Woman in grey clothing: 49
Man in grey clothing: 48
Polyp: 277
Wolflizard: 93
Ratlizard: 92
Scylla: 206 (head only)
Female Seldane: 86
Male Seldane: 85
Head Seldane (purple clothing): 87
Skeleton: 287
Ooze: 115
Asp: 88
Tentacle: 205
Golem: 294
Unicorn: 225 (front half only :()
Woman in purple clothing: 83
Sylph: 292

When choosing what you'd like to be, you can check out each monster's attributes on the Monster Stats page. There are many other interesting and occasionally useful sprites that you can be, but I did not write all of them down. You can even find some sprites that do not appear in the game ^_^ But the vast majority of the values are boring little bits of walls or shadows or such.

I'm sure this can be done with HexEdit too, but I have no idea how, and I bet it's considerably harder than my way. 
```


### Notes from Bryce



```
hex
10      oboloi in inventory
01      not in inventory?
ff      nothing/unused

16 byte record
byte 3 - Y position, apparently. leads one to suspect that
        bytes 0-2 might be zone or position related.
byte 0 - ff - nothing.
byte 4:5 - object type
        05 41   Green crystal orb
        05 42   lit bomb.
                byte 6 - fuse length. (01 = nasty suprise...)
        05 44   Mounted gator head.
        05 45   Sword dummy
        05 46   Broken sword
        05 47   Dice (behaved like a scale)
        17 82 - shrub.
        18 9A   A pitcher that behaves like a lyre.
        18 89 - 6 oboloi pile
        18 88 - 4 oboloi, but they don't stack with normal ones
        18 87 - a skirt, but it behaves like an inkwell
        18 86 - strange device
                (but gives a message: "It is blank." when you use it.)
        18 85 - sulfur
                (does not exhibit butter phenomina of seed pods.)
        18 84 - seed pod 
                NOTE - this object apparently contains a pointer to a script
                or something as I ended up with a seed pod that could be used
                to butter bread. unfortunatly it is not clear where the pointer
                is. (tested poking 10 into each of the 00 bytes and no change.)

                It would seem that objects with scripts have some additional 
                game state somewhere and turning oboloi into an object that
                should rightfully have scripts causes random collosions.
                (Note - it seems possible that the structure for these
                extended objects is 32 bytes but preliminary experiments
                may contradict this: turned crystal ball into dice. It behaved
                like a scale, not a crystal ball.
        18 83 - stairs (non-functional)
        18 82 - oboloi
        18 81 - vat
        18 01 - encampment (4 buildings make a town)
        18 02 - stairs down
        18 03 - top of a door.
        18 04 - archway
        24 51 - female mage
        24 50 - male mage
byte 14: involves position.

In the case of stacking objects, byte 7 is the quantity.

In the case of certain objects (such as the seed pod, 0x1884) the use of
byte 7 is unclear. 

In the case of portal objects (e.g. stairs or towns), byte 7 determines
where you go. some Valid places:
        01: LKH Summoning triangle (logical!)
        02: Outside LKH
        03: inside LKH
        04: inside Odemia
        05: outside Odemia
        06: outside abandoned farmhouse ( kidnapper's hideout)
        07: inside abandoned farmouse
        08: cellar of abandoned farmhouse
        09: next to ladder going into cellar (see the pattern here?)
        0a: outside catamarcia
        0b: inside catamarcia?
        0c: next to ladder going into catamarcia underground spring
        0e: next to ladder going into catamarcia underground store-cave
        10: to a point in the south of catamarcia, next to the ocean.
                just north of this there is actually a secret passage that
                also goes into the catamarcia underground spring.
        12: outside cademia
        14: next to the cave hole in LKH north store-cave.
        16: outside UrSlyph's prison
        18: in the east of the cave that leads to Maayti.
        1A: ditto, but the west entrance
        1C: timon's seldane ruins
        1D: Outside swamp ruins
        1E: Inside swamp ruins
        1F: outside Pnyx.
        20: inside pnyx
        22: inside Kosha
        26: beside east stairs on Pnyx bottom floor.
        28: beside east stairs on Pnyx top floor
        2f: 'nowhere' underneith pnyx.
        40: deep inside land's end volcano
        50: outside Borus's vineyard
        60: inside mining camp
        70: in cademia, next to the ladder going to the golem door puzzle thing
        80: deep inside harpy cave
        90: Cademia side of the bridge where Demodocus often hangs out
        a0: by rock outcropping of harpy cave chasm
        b0: Under Pnyx (the room with the fountain)
        c0: nothing
        d0: nothing
        
000008ED: 0B (11) -> 0F (15)
000008F4: D7 (215) -> ED (237)
000039F2: FF (255) -> 10 (16)
000039F4: 03 (3) -> 00 (0)
000039F5: 41 (65) -> 01 (1)
000039F6: 4C (76) -> 18 (24)
000039F7: CC (204) -> 82 (130)
000039F8: 31 (49) -> 00 (0)
000039F9: 00 (0) -> 1B (27)
00003AF2: 10 (16) -> 20 (32)
00003AF3: 00 (0) -> 0C (12)
00003AF4: 00 (0) -> 60 (96)
00003AF5: 01 (1) -> 3A (58)
00003AF6: 1C (28) -> 18 (24)
00003AF9: 3A (58) -> 1F (31)

01
cb:
000008ED: 0B (11) -> 1E (30)
000008F4: D7 (215) -> F9 (249)
00003FD2: 10 (16) -> 20 (32)
00003FD3: 00 (0) -> 0C (12)
00003FD4: 00 (0) -> 60 (96)
00003FD5: 01 (1) -> 39 (57)


clearing unexplored on mainland
0003C1F8: 1F (31) -> 9F (159)
0003C218: 1F (31) -> 9F (159)
0003C238: 1F (31) -> 9F (159)
0003C258: 1F (31) -> 9F (159)
0003C278: 1F (31) -> 9F (159)
0003C298: 1F (31) -> 9F (159)
0003C2B8: 1F (31) -> 9F (159)
0003C2D8: 1F (31) -> 9F (159)
0003C2F8: 1F (31) -> 9F (159)
0003C318: 1F (31) -> 9F (159)
0003C338: 1F (31) -> 9F (159)
0003C358: 1F (31) -> 9F (159)
0003C378: 1F (31) -> 9F (159)
The cytherian mainland is apparently 8*64 = 512 tiles across



appear to be 16-byte object records around 48e60, but starting at B
rather than 2. Also there are (similarly alligned) object records around
48e8e. although these records clearly involve characters,
changing the object type here  isn't persistant. So clearly something else
(possibly an associated script) is controlling it. The pointers to these
scripts must be elsewhere... they are not apparently in the object record.

prusa moving:
00044B3E: 77 (119) -> 78 (120)
00044B3F: 20 (32) -> 24 (36)
00044B4D: 01 (1) -> 02 (2)
00044B53: 17 (23) -> 16 (22)

00048E8E: 77 (119) -> 78 (120)
00048E8F: 20 (32) -> 24 (36)
00048E91: 30 (48) -> 20 (32)
04

meleager joins
000008ED: 0A (10) -> 0B (11)
000008F4: BF (191) -> DC (220)
0000092E: 03 (3) -> 00 (0)
000445DD: 04 (4) -> 00 (0)
000445E1: 83 (131) -> C3 (195)
000445EB: 00 (0) -> 02 (2)
000445EF: 8F (143) -> 01 (1)
000445F1: 06 (6) -> 07 (7)
00048BBD: 04 (4) -> 00 (0)
00048BBF: 20 (32) -> 10 (16)

variables related to the hero/ine are located around 92e
```


### Selax's expanded zone list

One fairly obvious observation is that these zones are denesely packed, not corresponding to any resource IDs.  They are probably indices into a table including a zone ID and coordinates. Zone IDs are thought to be two-byte integers (i.e. short), but it is not known if the Zone ID is the same as the Resource ID containing data describing that zone. 



```
01: LKH Summoning triangle (logical!)
02: Outside LKH
03: inside LKH
04: inside Odemia
05: outside Odemia
06: outside abandoned farmhouse ( kidnapper's hideout)
07: inside abandoned farmouse
08: cellar of abandoned farmhouse
09: next to ladder going into cellar (see the pattern here?)
0a: outside catamarcia
0b: inside catamarcia?
0c: next to ladder going into catamarcia underground spring
0e: next to ladder going into catamarcia underground store-cave
0f: in catamarca underground
10: to a point in the south of catamarcia, next to the ocean.
        just north of this there is actually a secret passage that
        also goes into the catamarcia underground spring.
11. Under Catamarca (Crolna chamber-next to tight passage)
12: outside cademia
13: Cademia entrance
14: next to the cave hole in LKH north store-cave.
15: Inside entrance to LKH cave system
16: outside UrSlyph's prison
17: tight passage exit on path
18: in the east of the cave that leads to Maayti.
19: just in front of tight passage
1A: ditto, but the west entrance
1B: in front of Timon ruins
1C: timon's seldane ruins
1D: Outside swamp ruins
1E: Inside swamp ruins
1F: outside Pnyx.
20: inside pnyx
21: outside Kosha
22: inside Kosha
23: outside Pnyx stairwell
24: outside Pnyx stairs
25: outside Pnyx stairs
26: beside east stairs on Pnyx bottom floor.
27: outside Pnyx stairs
28: beside east stairs on Pnyx top floor
29: outside Pnyx stairs
2a: outside Pnyx stairs
2b: Under Pnyx (Diones office)
2c: Pnyx library
2d: Under Pnyx (In wall?)
2e: Under Pnyx
2f: 'nowhere' underneith pnyx.
30: Seldane city
31: Outside Seldane entrance
32: Iron mine entrance
33: Entrance to above mine
34: Iron mine (ladder dead end)
35: Iron mine (outside ladder)
36: Iron mine (ladder to upper left of entrance)
37: Iron mine (exit from above ladder)
38: Iron mine (exit from ladder to hole)
39: Iron mine (entrance to ladder to hole)
3A: Iron mine (ladder to dead end on right)
3B: Iron mine (ladder dead end)
3C: Iron mine (next to hole)
3D: Iron mine (jhiaxus)
3E: In front of LKH volcano entrance
3F: LKH Volcano entrance
40: deep inside land's end volcano
41: LKH Volcano
42: LKH Volcano
43: LKH Volcano
44: LKH Volcano
45: LKH Volcano (dead end)
46: LKH Volcano
47: LKH Volcano
48: LKH Volcano
49: LKH Volcano (jinrai's chamber?)
4A: Outside Charax's house
4B: In Charax's house
4C: Outside Northern vineyard
4D: In Vineyard
4E: entrance to hall of truth
4F: Maayti entrance
50: outside Borus's vineyard
51: Inside Borus's vineyard
52: Next to trapdoor in Halos's house
53: Sewers next to ladder to door
54: Sewers (dryas)
55: ratcatcher's home
56: Next to sewers trap door
57: Next to ladder at sewers entrance
58: Sewer exit near ladder entrance
59: Sewer exit at Judge's house
5A: Sewers (next to bridge)
5B: Sewers (dryas hiding)
5C: Outside farm
5D: Inside farm
5E: Secret room in Comana
5F: Kosha grotto
60: inside mining camp
61: Next to mine entrance
62: Tyrant's tomb
63:  Sundial to tomb
64: Entrance to Scylla temple
65: scylla temple
66: Crypts entrance
67: Entrance to cave system in mountains
68: Inside cave system
69: Moss entrance to cave
6A: Outside Cove
6B: Inside Cove
6C: Outside hole to north of Cove entrance
6D: Inside hole
6E: Next to hole entrance in Timon entrance
6F: Machaon workshop
70: in cademia, next to the ladder going to the golem door puzzle thing
71: Abydos entrance
72: Next to Abydos
73: Next to ladder in far northwest abydos
74: Inside ladder entrance in abydos
75: below abydos
76: Next to ladder south of abydos entrance
77: First stronghold entrance
78: Next to First Stronghold
79: Outside Ruffian Encampment
7A: Ruffian Encampment
7B: Bottom of dungeon stairs in First Stronghold
7C: First Stronghold stairs to down
7D: Far east of Stronghold dungeon
7E: Outside hole to mountains
7F: Harpy cave?
80: deep inside harpy cave
81: Below north hole in harpy cave
82: Outside First Stronhold ladder exit
83: Second Stronghold (disappearing)
84: Outside Second Stronghold
85: Cavern system (Eioneus)
86: Outside entrance to Eioneus's cave system
87: Outside hole to bottom right of Eioneus bridge
88: Inside hole in cave system
89: Outside another hole in the caves
8A: Caves (Eioneus?)
8B: Endpoint of rope in Eioneus's cave
8C: Caves (next to rope down)
8D: Strange empty Cythera map (Second Stronghold?)
8E: East end of bridge
8F: Entrance to bridge
90: Cademia side of the bridge where Demodocus often hangs out
91: East bridge entrance
92: Mountains (Strange map-Tree of Life?)
93: West of Cythera mountains (north of mine)
94: Omen's test entrance
95: Omen's test
96: LKH (Quarters-Omen teleports)
97: Omen's Test (Bomb room)
98: Omen's Test
99: Omen's Test
9A: Omen's Test
9B: Omen's Test (lever in maze)
9C: Omen's Test
9D: Omen's Test
9E: Omen's Test
9F: Mountains
A0: by rock outcropping of harpy cave chasm [Mountains]
A1: Sewers (lyre room stair)
A2: Fur cloak room
A3: Crypts
A4: Crypts
A5: Crypts
A6: Crypts
A7: Crypts
A8: Crypts
A9: Crypts
AA: Crypts
AB: Crypts
AC: Crypts
AD: Crypts
AE: Crypts
AF: Crypts
B0: Crypts (diones office) [Under Pnyx (the room with the fountain)]
B1: LKH (Seldane teleport point)
B2: Stone (Seldane east point)
B3: Swamp Ruins (south point)
B4: Timon Ruins (west point)
B5: Underground sewer chamber
B6: Entrance to chamber
B7: End of Omen's test
B8: Entrance to end of test
B9: Cademia (outside trapdoor to Omen)
BA: Omen's Test
BB: Cove
BC: Cove
BD: Ur-sylph's prison
BE: outside Ur-sylph's prison
BF-FF: Nothing map (Presumably)
```
