
Just the business end (.[UseOn](UseOn)) of the water-filled distiller. .Use returns 0x8001 to get the target. 

CONTAINS ERRORS. 

```
object DObj
  .UseOn: function (self, target) (local1)
    if
      arg self
      field Prop.Data1    ; First persistence data byte
      byte 1
      eq
    then label569

    if
      arg target
      field Prop.Field5  
      word 0x00001825 ; not sure what this is. res 1825 is the gator boots smith.
      eq
    then label548

    setattr Prop.Data1
      arg self
    to
      byte 0
    end

    setattr Prop.PropType
      arg self
    to
      short Props.Distiller_Empty ; empty distiller 0x00E9
    end

    setattr Prop.Data1
      arg target
    to
      byte 1
     end

     call 0x0E8B
       global 0x05
       byte 0x32
     end

     "You seem to hear a faint, muted scream, "
     "and suddenly the crystal seems different.\n"

     sys_E8   ; Conversation mode?
     end

     sys_A4   ; Add conversation participant?
       short 0x0001 
       byte 0x02
     end

     sys_A4   ; Add conversation participant?
       short 0x007E
       byte 0
     end
 
     "An anxious vision of Omen suddenly "
     "appears*"No!!!! You've ruined it all!!!"
     ; ... A long block of text is omitted here. ...
     "somehow you doubt this is the last of him...*"

    sys_E9  ; End conversation mode?
    end
 
    goto label566
    
    label548:
    "Hm, nothing seemed to happen."
    goto label655
    
    label569:
    set local1
      global 0x05 ; the pc at least sometimes
      op63 ;; 63 40 -- cast?
      end
    end

    if 
      local local1
      field 0x1E ;; interesting - mana, must be
      byte 10
      lt
    then label5D1
    
    "You concentrate, but end up feeling drained, accomplishing nothing.\n"

    setattr 0x1E
      local local1
    to
      byte 0
    end

    setattr Prop.PropType
      arg Self
    to
      short 0x00E9 ; empty distiller
    end

    return
      byte 0
    end

    label5D1:
    setattr 0x1E
      local Local1
    to
      local Local1
      field 0x1E
      byte 10
      sub
    end

    setattr Prop.PropType
      arg Self
    to
      short 0x00E9
    end

    if
      arg Target
      field 0x09 ; quantity for stackables?
      byte 1
      le
    then label5FB

    delete
      arg Target
    end
    
    goto label606

    label5FB:
    setattr 0x09
      arg Target
    to
      arg Target
      field 0x09
      byte 1
      sub
    end

    call 0x0E8B
      local Local1
      byte 1
    end
    
    sysAD
      byte 1

      arg Self
      field Prop.X
      byte 1
      add

      arg Self
      field Prop.Y

      arg Target
      op61 ; offs=61b

      arg Self

      local Local1

      short 0x001F

      byte 0 

      byte 0
    end

    sysE6
      byte 1
    end

    "It worked!\n"

    goto label655
   
    label637:
    "Hm, nothing seemed to happen.\n"
    return
      byte 0
    end

    label659

```
