
Magpie is a patch manager for Cythera, written by Glenn Andreas. It doesn't work on old versions of classic Mac OS on 68K (e.g. OS 7.5.3 on Basilisk II, which runs Cythera itself fine), but will work on OS 9 using Sheepshaver. 

Magpie was apparently intended to be an add-on system for Cythera, but only one patch is known, the so-called [Pumpkin Patch](Pumpkin-Patch) which adds a Halloween / autumn graphical theme to the game. gandreas cryptically referenced a second patch in one post, noting that Magpie has provisions for collision detection, but this second patch is not known. Perhaps it had a very limited release, or was just a Bug Fix patch. 

Analysis of the STR# resources of the Magpie application suggest that patches are divided into one of four kinds: "Bug Fix", "Expansion," "Add On," and "Plug In;" the Pumpkin Patch is an "Add On." Patches also have a rating, which is one of "Official," "Approved," "Unofficial," or "Invalid;" the Pumpkin Patch is "Official."  They also have a version (1.0 in the case of the Pumpkin Patch.) 

As of this writing, detailed analysis of Magpie and its patches has not been carried out.  

Rather than just making a clean backup copy of the unpatched data file, Magpie appears to store information about the changes it's made in a secondary file called "[Cythera Unpatch](Cythera-Unpatch)" in its Patches folder. This is a Delver Archive, albeit without a scenario title in the header. (Narthex can read it.) It contains the original versions of the resources that were replaced by patches. 

Besides the expected alternate versions of the resources to be patched, a Magpie patch has a special resources, FFFF, with patch information. A Cythera Data file patched by magpie acquires this resource, as well as another, FFFE, which is very short. 

See [Patch Working Page](Patch-Working-Page) 
