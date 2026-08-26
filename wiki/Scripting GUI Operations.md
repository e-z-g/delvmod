
Mere conjecture - 93 S... 40 might wait on response from the window. Nope, calling it causes the window to close right away. Maybe that's because I didn't have a window with working buttons, though. 

Mostly explicit-event-loop based like classic Mac OS, but callbacks seem to be possible as well, see for example 1175, Strange Device - the buttons may function this way, with widget field39 being the callback. 

hypothesis: the four ints are probably x,y,w,h. If there is no parent, then you just have w,h. 


|**Binary format** | **Mnemonic** | **Parameters**|
|-|-|-|
|9B 04 | gui create | parent, graphic, int?, int?, int?, int?|



Makes a new window. graphic - in 8Fxx series. Returns a "System Object" (probably the window.) A zoom box from the parent prop will be created when the window opens, and a woosh sound. 

Examples: 1086 for maps, wanted posters 

in 0EA9 (selling stuff): gui_create (0x0000015E, 0x0000012C) (no parent!) 

1098 (lute): gui_create(self, 0x12, 1, 0x18, 0x5A, 0x34) 109A (lyre): gui_create(self, 0x14, 0x61, 0x48, 0x55, 0x000000A7) 

0x8F12 is the panpipes but it's probably a coincidence. None of those bytes correspond to any other musical instrument and the instruments are not consecutive. 

1111 (map of cythera) - gui_create(self, 0x13, 0x32, 0x32, 1,1) 0x8F13 is the map of cythera. This seems to be the no-frills version of the call. 

10C5 (poster- make oboloi fast etc?) - gui_create(self, self.d2, 0x32, 0x32, 1, 1) 

117A (automap) - gui_create(self, 0x06, 0x28, 0x28, 0x7D, 0x000000A5) 0x8F06 is the automap background. 


|**Binary format** | **Mnemonic** | **Parameters**|
|-|-|-|
|9B 06 | gui text | parent, caption, int?, int?, int?, int?|



in inkwell: (window, "What do you want to write?", 0x14, 0x14, 0x0000012C, 0x20) in 0E64 (called by paper): (window, messagetext, 0, 0, arg, arg) 


|**Binary format** | **Mnemonic** | **Parameters**|
|-|-|-|
|9B 08 | gui button | parent, caption, int?, int?, int?, int?|



in inkwell: (window, "Write it", 0x0000010E, 0x000000A8, 0x46, 0x20) 

in 300F (stealing warnings from awareness or being observed while stealing): gui_button(local3, "Steal/s",      0x0a, 0x5a, 0x60, 0x20)  (s is the keyboard shortcut.) gui_button(local3, "Leave/l/\x1B", 0x9a, 0x5a, 0x60, 0x20)  (l is the keyboard shortcut.) gui_button(local3, "Take/s",       0x0a, 0x5a, 0x60, 0x20)   


|**Binary format** | **Mnemonic** | **Parameters**|
|-|-|-|
|9B 0F | |



Seen in 1098 (lute) with arg list (window, 0,0,0x5a,0x34, 0x19, [0x0000000f, 0x0000000c, 0x00000009, 0x00000006, 0x00000003]) (probably the notes made by the instrument passed in an array) 

lyre (window, 0,0,0x55,0x000000A7, 0x2f, [0x12, 0x0f, 0x0c, 0x09, 0x06, 0x03]) 

two in  panpipes (1099)-  

* (window, 0,0,0x000000a0,0x61,0x4c,[0xf,0xc,0x9,0x7,0x3]) (window, 0,0,0x000000a0,0x61,0x4c,[0xf,0xc,0x9,0x6,0x3]) 

|**Binary format** | **Mnemonic** | **Parameters**|
|-|-|-|
|9B 11 | gui spinner | parent,x, y,w,h|



Field3E, 3F set min and max integer values. field37 contains the value (set to set the default.) 


|**Binary format** | **Mnemonic** | **Parameters**|
|-|-|-|
|9B 14 | gui textbox | parent, default_content, x,y,w,h|



in inkwell: (window, "Write Something", 0x14, 0x3C, 0x0000012C, 0x60) 

Returns the textbox, its field 0x37 contains the text. 

--these last four parameters, man... addresses? If they are they aren't for the resource or relative to function beginning or that +3...-- Coordinates? 

![](Scripting-GUI-Operations/sleep.png) _Example of Cythera's gui, showing text, buttons, 
