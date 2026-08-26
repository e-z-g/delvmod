
Warning: This is out of date. The actual header file is on github. 

Header file for RDASM. 



```
; Copyright 2016 Bryce Schroeder, www.bryce.pw, bryce.schroeder@gmail.com
; Wiki: http://www.ferazelhosting.net/wiki/delv
; 
;    This program is free software: you can redistribute it and/or modify
;    it under the terms of the GNU General Public License as published by
;    the Free Software Foundation, either version 3 of the License, or
;    (at your option) any later version.
;
;    This program is distributed in the hope that it will be useful,
;    but WITHOUT ANY WARRANTY; without even the implied warranty of
;    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;    GNU General Public License for more details.
;
;    You should have received a copy of the GNU General Public License
;    along with this program.  If not, see <http://www.gnu.org/licenses/>.
;
; This header file defines data structures and constants used by 
; Cythera 1.0.4. They are not expected to work with any other first-party
; Delver scenario (or version), as constants and even opcodes could in
; theory change under DelvEd. (ReDelv does not have this problem of 
; gratuitous constant-reassignment, and new first-party anythings seem
; extremely unlikely at this point.)
;
; Note that this file is GPL licensed; all scripts produced which include it
; are also required to be GPL licensed - if you distribute their compiled 
; form, you must also make the source code available.


class DObj      ; Delver Object
  ; string DObj.Look(self)
  ; A method which returns a string containing a short description of the
  ; object, i.e. what one would see when looking at it. This overrides the
  ; default of the tile name when mousing over things in the game.
  .Look         0x0002

  ; void DObj.Examine(self)
  ; A method, which should print out a more detailed description of the
  ; object. It returns nothing (n.b. unlike .Look which returns a string -
  ; it is not unusual for Examine to call Look in the case of objects which
  ; encompass many types of things, e.g. potions or scrolls.)
  .Examine      0x0008
  
  ; int DObj.Use(self)
  ; A method, triggered when the user attempts to use an object. For some
  ; sorts of objects, e.g. a spell not requiring a target, the use method
  ; effects the result of using the object. More commonly though, it prints
  ; some explanatory prompt ("Pour water on what?"). In that case, a mask
  ; value must be returned to identify what input Delver should get from the
  ; user:
  ;   (Document Use return values here) FIXME
  .Use          0x0009

  ; void DObj.UseOn(self, target)
  ; A method, which should effect the use of this object on another. Note
  ; that in the case of e.g. casting a spell or using a skill, "self" is the
  ; skill object itself, not the caster/user. The object for the user is 
  ; instead typically gotten from Globals.Current. UseOn returns nothing.
  .UseOn        0x000A

  ; void DObj.UseAt(self, x, y)
  ; A method, which effects the use of this object at a location in the
  ; current level. As with UseOn, self is the skill object, not the user.
  ; UseAt returns nothing.
  .UseAt        0x000B


  ; Seems to be called on e.g. goats and chickens, which do supplementary
  ; things not covered by the AI scripts, e.g. making noises. (cluck-cluck!)
  ; It is probably called every turn on the object's turn. An experiment is
  ; needed to determine what kinds of objects receive this event -- if it is
  ; called for non-character objects it would be a way to bypass the technical
  ; difficulties in creating summoning spells under Delver.
  .Method20     0x0020


  ; list DObj.AskAbout
  ; A field, containing a list of two items. The first item of the list is 
  ; a string which contains what a character knowledgeable about the subject 
  ; would say. The second item is a list of the NPCs who know about the item
  ; when asked about it. E.g. a magic item would be something like:
  ; ["This is infused with strange goat magics.", [People.Timon]]
  .AskAbout     0x0033 


enum People             ; People in Cythera.
  .x                   0
  .Hero                1
  .Alaric              2
  .Magpie              3
  .Hadrian             4
  .Emesa               5
  .Hector              6
  .LKH_Guard           7
  .Cademia_Guard       8
  .Ruins_Guard         9
  .Myus               10
  .Naxos              11
  .Darius             12
  .Pelagon            13
  .Deiphobus          14
  .Kosha_Guard        15
  .Atreus             16
  .Ennomus            17
  .Ariethous          18
  .Laodice            19
  .Thuria             20
  .Malis              21
  .Cybele             22
  .Amphidamas         23
  .Eurybates          24
  .Rhesus             25
  .Lycurgus           26
  .Erechtheus         27
  .Thamyris           28
  .Atymnius           29
  .Milcom             30
  .Sardis             31
  .Ake                32
  .Neoptolemus        33
  .Meleager           34
  .Hebe               35
  .Antenor            36
  .Alastor            37
  .Aeneas             38
  .Eioneus            39
  .Parium             40
  .Crito              41
  .Apis               42
  .Dares              45
  .Diomede            46
  .Thetis             48
  .Bias               49
  .Philinus           50
  .Opheltius          51
  .Ascalon            52
  .Ariadne            53
  .Odemia_Guard       54
  .Tlepolemus         55
  .Eteocles           56
  .Laomedon           57
  .Ilus               58
  .Autonous           59
  .Propontis          60
  .Mantinea           61
  .Halos              62
  .Catamarca_Guard    63
  .Oeneus             64
  .Periphas           65
  .Theano             66
  .Hypsenor           67
  .Thoas              68
  .Dymas              69
  .Sacas              70
  .Metopes            71
  .Berossus           72
  .Itanos             73
  .Timon              74
  .Prusa              75
  .Bryaxis            76
  .Anisa              77
  .Pheres             78
  .Charax             79
  .Lindus             80
  .Selinus            81
  .Palaestra          82
  .Tros               83
  .Pnyx_Guard         84
  .Alcestris          85
  .Asius              86
  .Paris              87
  .Helen              88
  .Niobe              89
  .Larisa             90
  .Joppa              91
  .Eudoxus            92
  .Eumelus            93
  .Antiphus           94
  .Polydamas          95
  .Peirithous         96
  .Aethon             97
  .Dryas              98
  .Gate_Guard        100
  .Thersites         101
  .Glaucus           102
  .Borus             103
  .Briseis           104
  .Pelops            105
  .Alcmena           106
  .Asteropaeus       107
  .Stentor           108
  .Demodocus         109
  .Thrasymedes       110
  .Protesilaus       111
  .Menelaus          112
  .Lycaon            113
  .Peleus            114
  .Peisander         115
  .Danae             116
  .Semele            117
  .Alcyone           118
  .Clytemnestra      119
  .Sabinate          120
  .Jhiaxus           121
  .Unhayt            122
  .Seqedher          123
  .Uset              124
  .Ignae             125
  .Omen              126
  .UrSylph           127
  .Fountain          189
  .Door              190

enum Spells             ; Spells in Cythera. ResID = N | 0x1A00
  .Directed_Nexus       0
  .Vision_of_the_Night  1
  .Minor_Embrightenment 2
  .Detect_Concealment   3
  .Detect_Traps         4
  .Remote_Manipulation  5
  .Death_Strike         6
  .Acertainment         7
  .Alleviation          8
  .Lesser_Healing       9
  .Healing              10
  .Greater_Healing      11
  .Embrightenment       12
  .Soporiferousness     13 ; Where did he get this word...
  .Terrorisation        14
  .Derangement          15
  .Major_Embrightenment 16
  .Nutrient             17
  .Mystic_Arrow         18
  .Awaken               19
  .Detect_Rune          20
  .Resist_Blows         21
  .Rune_of_Warding      22
  .Rune_of_Flame        23
  .Dispel_Rune          24
  .Rally                25
  .Rune_of_Blocking     26
  .Mage_Lock            27
  .Awaken_All           28
  .Lightning            29
  .Cure                 30
  .Resist_Fire          31
  .Open                 32
  .Rune_of_Pain         33
  .Fireball             34
  .Paralyze             35
  .Shake_Down           36
  .Daylight             37
  .Mass_Terrorisation   38
  .Charm                39
  .Fetch                40 ; Oh, the memories
  .Mass_Cure            41
  .Farsight             42
  .Replicate            43
  .Mass_Confusion       44
  .Tremor               45
  .Restoration          46
  .Resurrection         47
  .Remove_Mage_Lock     48


enum Globals          ; Global variables, accessible with the 0x48 xx opcode.
  .Current            0x09  ; Current character prop (whose turn it is?)
```
