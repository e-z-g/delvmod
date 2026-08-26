
100E, bed. 



```
class Bed(DObj):  
    Field22 = None
    Field00 = None 
    def Use(self):
        local0 = 0 
        if global(0x12) != 2:
            local0 = 4

        LABEL019:
    if self.data1:
        if self.data1 == 0xFF:
            "It looks like somebody else is staying here - perhaps another bed...\n"
            return 0

        if self.data1 != Op49(0x03010016):
            "You need to pay the inkeeper first.\n"
            return 0

        local0 = Op49(0x03010012)[Op49(0x03010016)]

    bedX = self.x
    bedY = self.y  
 
    if bed.aspect == 3:
        bedY -= 1
    else:
        bedX -= 1

    local3 = OpCB(word 0x10000004, 0, bedX, bedY)

    labelF2:
    while not OpCB(word 0x10000004, 1): 
        if local3 and (Character)local3 != gCurrent:
            "Somebody is already asleep there!\n"
            return 0
        local3 = OpCB(word 0x10000004, 2))
        ; 144

    window = gui.Window(0x12c, 0x140)
    prompt = gui.Label(window, "Sleep how long?", 0,0,0x12c, 0x20)
    dawnbtn = gui.Button(window, "Until Dawn/d", 0,0x28, 0x12c, 0x20)
    morningbtn=gui.Button(window, "Until Morning/o",0,0x50,0x12c,0x20)
    #  ...&c,     0x9b11:
    hoursbox = gui.Spinner(window, 0x96, 0xF0, 0x96,0x20) #d
    hoursbox.field3E = 1
    hoursbox.field3F = 12
    hoursbox.field37 = 1
    hoursbtn = gui.Button(window, "Hours", #etc...)
    cancelbtn = gui.Button(window, "Cancel/c\x1B", #etc...)
    
    # 0x0290
    - assign string based on button pressed to local11, e.g. "noon"

    ## 039d - 85 03 01 00 16    41 00    40
    ## 0x3a5 - 9F 0E93  - sleeping script? 
    
    
```
