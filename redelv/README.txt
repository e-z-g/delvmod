WHAT IS redelv?

The program 'redelv' is a third-party role playing game scenario editor system
interoperable with the Delver Engine by Glenn Andreas. Besides modifying the 
scenario file of a Delver-based game (e.g. "Cythera Data"), it can create and 
apply patches and perform other manipulations of Delver Archives.

redelv is based on the python module delv, which was itself prepared based on
the DelvTechWiki's technical documentation project, which can be found here:
http://www.ferazelhosting.net/wiki/

REQUIREMENTS / PYTHON VERSION

redelv requires Python 2.7 and PyGTK (GTK+ 2). PyGTK was never ported to
Python 3 and is not available on Apple Silicon (arm64) Macs, so redelv does
not currently run there. Porting it would mean migrating the GUI to
PyGObject/GTK+ 3, which is a substantial rewrite -- gtk.ItemFactory, used to
build every menu bar in redelv, was removed outright in GTK+ 3.

The underlying delv module itself does run on Python 3 and on Apple Silicon;
only this GUI front end is affected.

INSTALLING
pip install .

HOW TO USE IT
Run the command 'redelv' from your command line after installing.
It's a GUI program, so you just mess with it until you figure it out. 
Make backups.

The suggested workflow is to use redelv on a copy of "Cythera Data" that is
on a virtual disk shared with a Mac Emulator (e.g. BasiliskII or SheepShaver).
After making your desired mods, you can use redelv to make a patch that will
modify an unmodified copy of "Cythera Data" to match your modified one.



LICENSE
Free software under the GPL3. (As required by using delv, which is GPL3,
not LGPL3.) The developers of delv politely ask you not to use delv to create
versions of the "Cythera Data" file modified to bypass the shareware 
restrictions, a request that also applies to redelv.





