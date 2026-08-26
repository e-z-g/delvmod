
"[Cythera](Cythera) Data" is the main data file of Cythera. It is a [Delver Archive](Delver-Archive).


## Resource Fork Contents

Many of the resource types in the data file appear to be for the use of the original delver editor, rather than for the use of the game itself, and can even be deleted without apparent consequence.

* [Cythera Data clut](Cythera-Data-clut) - Contains the color palette for Cythera
* [Cythera Data nrct](Cythera-Data-nrct) - Contains
* [Cythera Data sfnt](Cythera-Data-sfnt) - Font related
* [Cythera Data vers](Cythera-Data-vers) - Contains version information (the Cythera 1.0.4 data file is marked as version 1.0.3.)
* [Cythera Data TMPL](Cythera-Data-TMPL) - Contains [ResEdit](ResEdit) templates for editing [TxSt](TxSt) and [TxCl](TxCl) resources
* [Cythera Data STR#](Cythera-Data-STR) - Contains various arrays of strings, e.g. the game credits.
* [Cythera Data RMAP](Cythera-Data-RMAP) - Contains
* [Cythera Data NFNT](Cythera-Data-NFNT) - Contains bitmapped fonts (for the Seldane typeface, apparently)
* [Cythera Data FOND](Cythera-Data-FOND) - Contains font information
* [Cythera Data PORT](Cythera-Data-PORT) - Contains
* [Cythera Data eBRS](Cythera-Data-eBRS) - Contains [Delver editor brush](Delver-editor-brush) for the editor. Appears to be dispensable.
* [Cythera Data eSTM](Cythera-Data-eSTM) - Contains [Delver editor stamp](Delver-editor-stamp) for the editor. Appears to be dispensable.
* [Cythera Data MSta](Cythera-Data-MSta) - Contains what may be mission/quest completion logic templates for the editor
* [Cythera Data LINF](Cythera-Data-LINF) - Contains
* [Cythera Data FILT](Cythera-Data-FILT) - Contains
* [Cythera Data DATA](Cythera-Data-DATA) - Contains data of unknown significance; some resources have intelligible strings.
* [Cythera Data TxSt](Cythera-Data-TxSt) - Contains some stuff that may be related to interface formatting.

## Data Fork (Delver Archive) Contents

Broadly, this file contains most of Cythera's content, such as maps, scripts, sprites, and dialogue.

* [Cythera Data Subindex   0](Cythera-Data-Subindex-0) - List of game actions and classifications? (clrbit, [CanHold](CanHold), etc.)
* [Cythera Data Subindex   1](Cythera-Data-Subindex-1) - Encrypted Lists of strings for scripts (character names, class names, ring inscriptions, gravestones)
* [Cythera Data Subindex   2](Cythera-Data-Subindex-2) - Contains unknown
* [Cythera Data Subindex   3](Cythera-Data-Subindex-3) - Contains AI [scripts](AI-Script-Type)
* [Cythera Data Subindex   4](Cythera-Data-Subindex-4) - Encrypted Integer constants for scripts?
* [Cythera Data Subindex   7](Cythera-Data-Subindex-7) - Contains shared [dialogue](Cythera-Dialogue).
* [Cythera Data Subindex   8](Cythera-Data-Subindex-8) - Scripts of the [81 ... 40 Script Type](81-...-40-Script-Type)
* [Cythera Data Subindex   9](Cythera-Data-Subindex-9) - Scripts of the [81 ... 40 Script Type](81-...-40-Script-Type), e.g. drinking water at fountain
* [Cythera Data Subindex  10](Cythera-Data-Subindex-10) - Contains just one very short [81 ... 40 Script Type](81-...-40-Script-Type) resource, 0B00
* [Cythera Data Subindex  11](Cythera-Data-Subindex-11) - Scripts of the [81 ... 40 Script Type](81-...-40-Script-Type), including e.g. innkeeper popup dialogue
* [Cythera Data Subindex  12](Cythera-Data-Subindex-12) - Scripts of the [81 ... 40 Script Type](81-...-40-Script-Type)
* [Cythera Data Subindex  13](Cythera-Data-Subindex-13) - Very many scripts of the [81 ... 40 Script Type](81-...-40-Script-Type), e.g. using water on things, unlocking doors, combat results
* [Cythera Data Subindex  14](Cythera-Data-Subindex-14) - Quite short scripts of the [81 ... 40 Script Type](81-...-40-Script-Type), without intelligible strings
* [Cythera Data Subindex  15](Cythera-Data-Subindex-15) - Contains dialogue trees, multiple scripts of the [81 ... 40 Script Type](81-...-40-Script-Type) although the file does not begin with 0x81
* [Cythera Data Subindex  16](Cythera-Data-Subindex-16) - Contains objects, and possibly associated data/scripts with intelligible strings
* [Cythera Data Subindex  19](Cythera-Data-Subindex-19) - Contains short binary data with names of regions ("Odemia", "Omen's Test" and "Below Cademia" in the same resource, "Mountains")
* [Cythera Data Subindex  20](Cythera-Data-Subindex-20) - Very similar to subindex 19, but but only three resources ("Cave", e.g.)
* [Cythera Data Subindex  23](Cythera-Data-Subindex-23) - More character dialogue scripts for individual characters.
* [Cythera Data Subindex  24](Cythera-Data-Subindex-24) - Encrypted binary data of unknown significance.
* [Cythera Data Subindex  25](Cythera-Data-Subindex-25) - Descriptions, and possibly scripts, for spells, skills, and sorts of actions (e.g. pooling cash.)
* [Cythera Data Subindex  26](Cythera-Data-Subindex-26) - Contains Room descriptions, and possibly scripts.
* [Cythera Data Subindex  27](Cythera-Data-Subindex-27) - Contains room descriptions, like 26.
* [Cythera Data Subindex  29](Cythera-Data-Subindex-29) - One resource, 1E20,  40 bytes, encrypted. Unknown purpose.
* [Cythera Data Subindex  47](Cythera-Data-Subindex-47) - Classic scripts of the [81 ... 40 Script Type](81-...-40-Script-Type), which seem to relate to actions on characters.
* [Cythera Data Subindex 127](Cythera-Data-Subindex-127) - Contains maps (and roofs; each resource is paired with a subindex 128 resource)
* [Cythera Data Subindex 128](Cythera-Data-Subindex-128) - Contains props (each resource paired with a subindex 127 resource)
* [Cythera Data Subindex 131](Cythera-Data-Subindex-131) - Landscapes, as [compressed graphics](Delver-Sprite-Graphics)
* [Cythera Data Subindex 135](Cythera-Data-Subindex-135) - Character portraits, as [compressed graphics](Delver-Sprite-Graphics)
* [Cythera Data Subindex 137](Cythera-Data-Subindex-137) - Contains spell icons (simple, clut-indexed graphics)
* [Cythera Data Subindex 141](Cythera-Data-Subindex-141) - Contains [compressed graphics](Delver-Sprite-Graphics) for the props and tiles.
* [Cythera Data Subindex 142](Cythera-Data-Subindex-142) - General graphics (e.g. signs, drawers, the background texture.)
* [Cythera Data Subindex 143](Cythera-Data-Subindex-143) - Contains music.
* [Cythera Data Subindex 144](Cythera-Data-Subindex-144) - Contains sounds ([asnd Format](asnd-Format))
* [Cythera Data Subindex 239](Cythera-Data-Subindex-239) - Contains binary resources of tremendously varying lengths (16 bytes to 131kb)

## Narthex Output



```
List of valid subindices:
Subindex   0: found     1 resource
Subindex   1: found    20 resources
Subindex   2: found     2 resources
Subindex   3: found    14 resources
Subindex   4: found     3 resources
Subindex   7: found    22 resources
Subindex   8: found    19 resources
Subindex   9: found     8 resources
Subindex  10: found     1 resource
Subindex  11: found    30 resources
Subindex  12: found    10 resources
Subindex  13: found    66 resources
Subindex  14: found    22 resources
Subindex  15: found   180 resources
Subindex  16: found    88 resources
Subindex  19: found    42 resources
Subindex  20: found     3 resources
Subindex  23: found   121 resources
Subindex  24: found    29 resources
Subindex  25: found    87 resources
Subindex  26: found   111 resources
Subindex  27: found    38 resources
Subindex  29: found     1 resource
Subindex  47: found    40 resources
Subindex 127: found    42 resources
Subindex 128: found    40 resources
Subindex 131: found    18 resources
Subindex 135: found   142 resources
Subindex 137: found    62 resources
Subindex 141: found   160 resources
Subindex 142: found    59 resources
Subindex 143: found    11 resources
Subindex 144: found    46 resources
Subindex 239: found    20 resources
```
