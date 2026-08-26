
0EAC, little mechanics script called to check for Thievery (but not the binary skill Awareness.) 

```
def f0EAC(skillHaver, skillID):
    skillval = getskill(skillHaver, skillID)
    if not skillval: 
        return 0
    if not (skillval.field03 & 0x10)
        return skillval.field03 
    return 0
    
```

300F, stealing/"borrowing" Awareness/Stealing script. 

```
def Steal(arg0):
  x0 = gUnknown_10.field20 # odd since global 0x10 prints as an integer...

  if op60_24(x0):
      return None

  thieveryLevel = call_resource(0x0EAC, (gPlayerCharacter, Skills.Thievery))   # 0x1AD6 is "Thievery"

  hasAwareness = getskill(gPlayerCharacter, Skills.Awareness) # 0x1ACD is "Awareness"

  if not (hasAwareness or thieveryLevel): 
      return True
  
  myWindow = gui_window(260, 130)

  if thieveryLevel:
      gui_text(myWindow, "You sense that somebody is watching you 'borrow' that...",
               50,10,200,64)
  else:
      gui_text(myWindow, "That doesn't seem to belong to you...",
               50,10,200,64)

  gui_10(myWindow, arg0, 10, 10)

  if thieveryLevel:
      takeButton = gui_button(myWindow, "Steal/s", 10, 90, 96, 32)
  else:
      takeButton = gui_button(myWindow, "Take/s",  10, 90, 96, 32)

  leaveButton = gui_button(myWindow, "Leave/l/\x1B", 154, 90, 96, 32)

  x6 = True

  while 1:
      x7 = myWindow.field37
      if x7 == takeButton: 
          x6 = True
          break
      if x7 == leaveButton:
          x6 = False
          break

  op93(myWindow)  # close

  if not x6:
      return x6

  if not thieveryLevel:
      return x6

   while (thieveryLevel > 0):
       thieveryLevel -= 1
       if random(0,6) != 3:
           continue
       x8 = ["Your shoe's untied...", "Is that Alaric?", None]
       Globals.PlayerCharacter.talkBalloon = x8[random(0, len(x8))]
       return None

  

   x8 = ["Look over there!", "Is that Elvis?", "Don't mind me..."]
   Globals.PlayerCharacter.talkBalloon = x8[random(0,len(x8))] # field26, text balloon
   return True

   
      
  
```



```
function (a0) (x0, x1, x2, x3, x4, x5, x6,x7,x8) 
  set x0
    global 0x10 ; odd, since this prints as an integer
    field 0x20
  end

  ifn 
    local x0
    op60 0x24
  then L018

  return 
    word None
  end

  L018:
  set x1
    call 0x0EAC
      global Globals.PlayerCharacter
      short 0x00D6
    end
  end

  set x2
    opF5
      global Globals.PlayerCharacter
      short 0x00CD
    end
  end

  ifn
    local x2
    local x1
    or
  then L23C

  set x3
    gui_window 
      word 0x000104
      word 0x000082
    end
  end

  ifn
    local x1
  then L096

  gui_text
    local x3
    string "You sense that somebody is watching you 'borrow' that..."
    byte 0x32
    byte 0x0A
    word 0x00000C8
    byte 0x40
  end
  
  goto L0CC
  
  L096:
  gui_text
    local x3
    string "That doesn't seem to belong to you..."
    byte 0x32
    byte 0x0A
    word 0x00000C8
    byte 0x40
  end

  L0CC:
  gui_10
    local x3
    arg a0
    byte 0x0A
    byte 0x0A
  end

  ifn
    local x1
  then L0F5

  set x4
    gui_button
      local x3
      string "Steal/s"
      byte 0x0A
      byte 0x5A
      byte 0x60
      byte 0x20
    end
  end

  goto L10C

  L0F5:
  set x4
    gui_button
      local x3
      string "Take/s"
      byte 0x0A
      byte 0x5A
      byte 0x60
      byte 0x20
    end
  end
  
  L10C:
  set x5
    gui_button
      local x3
      string "Leave/l/\x1B"
      word 0x000009A
      byte 0x5A
      byte 0x60
      byte 0x20
    end
  end

  set x6
    word true
  end

  ifn 
    byte 1  ; <-- !!!
  then L164
  
  ; Dead code, or how buttons work?
  set x7
    local x3
    field 0x37
  end

  ifn
    local x7
    local x4
    eq
  then L14F

  set x6
    word true
  end
 
  goto L164

  L14F:
  ifn
    local x7
    local x5
    eq
  then  L161

  set x6
    word false
  end

  goto L164
 
  L161:
  goto L131 ; Event loop?

  L164:  ; dead code would end
  op93
    local x3
  end

  ifn
    local x6
  then L239

  ifn
    local x1
  then L239

  L171:
  ifn 
    local x1
    byte 0
    gt
  then L1DF

  set x1
    local x1
    byte 1
    sub
  end

  ifn
    randint
      byte 0
      byte 6
    end
    byte 3
    eq
  then L1DC

  set x8
    data ["Your shoe's untied...", "Is that Alaric?", void]
  end

  setattr 0x26
    global Globals.PlayerCharacter
  to
    local x8
    randint
      byte 0
      local x8
      len
    end
    index
  end

  return
    word None
  end
 
  L1DC: 
  goto L171 ; loopback

  L1DF:
  set x8
    data ["Look over there!", "Is that Elvis?", "Don't mind me..."]
  end

  setattr 0x26
    global Globals.PlayerCharacter
  to
    local x8
    randint 
      byte 0
      local x8
      len
    end
    index
  end

  return
    word true
  end

  L239:
  return
    local x6
  end

  L23C:
  return
    word true
  end

  return
    byte 0
  end
```
