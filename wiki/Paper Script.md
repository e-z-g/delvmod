
1086, paper, object  

Disassembly: 



```
object DObj
  .Look: [0x00000001]

  .Examine: function(Self)
     callself DObj.Use ; Op9D
       arg Self
     end

     return
       byte 0
     end

  .Use: function(Self) (Local1, Local2) 
    ifn
      arg Self
      field Prop.D1
      byte 0
      eq
    then Label0071

    set Local1
      word None
    end
   
    ifn
      arg Self
      field Prop.Field11
    then Label003B

    set Local1
      arg Self
      field Prop.Field12
      word 0x00000102
      index
    end

    Label003B:
    ifn
      local Local1
      word None
      ne
    then Label0061

    call 0x0E64
      arg Self
      local Local1
      byte 0x21
      byte 0x03
      byte 0x26
      byte 0x2C
      word 0x000000B6
      word 0x000000B8
    end

    goto Label006E

    Label0061:
    "It is blank.\n"

    Label006E:
    goto Label00F4

    Label0071:
    ifn 
      arg Self
      field Prop.D1
      word 0x000000FF
      eq
    then Label00A9
   
    ifn
      opDB
        arg Self
      end
    then Label0089

    return
      byte 0
    end

    Label0089:
      set Local2
        op9B 0x04
          arg Self
          arg Self
          field Prop.D2
          byte 0x32
          byte 0x32
          byte 1
          byte 1
        end
      end

      print
        word 0x3000:0x0221
        arg Self
        field Prop.D2
        add              ;;!!!
      end
      
      goto Label00F4

      Label00A9:
      ifn
        arg Self
        field Prop.Aspect
        byte 0x02
        lt
      then Label00D6
      
      call 0x0E64
        arg Self
        
        word 0x3000:0x0219
        arg Self
        field Prop.D1
        add
        byte 0x21
        byte 0x03
        byte 0x26
        byte 0x2C
        word 0x000000B6
        word 0x000000B8
      end
      
      goto Label00F4

      Label00D6:
      call 0x0E65
        arg Self
        word 0x3000:0x0219
        arg Self
        field Prop.D1
        add
        byte 0x11
        byte 0x27
        byte 0x34
        word 0x000000BC
        word 0x00000095
      end
 
      Label00F4:
      return
        byte 0
      end
        
  empty 0x000E
  empty 0x0024
  empty 0x0026
  empty 0x0027
```


|Field | Value|
|-|-|
|000E | nil|
|0024 | 0x1086:0x0002|
|DObj.Use | 0x1086:0x0013|
|0026 | nil|
|0027 | nil|
|DOBj.Examine | 0x1086:0x0008|
|000D | nil|





```
class Paper(DObj):
    Look = [1]

    def Examine(self):
        self.Use()

    def Use(self):
        if self.d1 != 0: goto L71
        local1 = None
        if not self.field11: goto L3B 
        local1 = self.field12[0x102]

        L3B:
        if local1 == None: goto L61
    
        call_resource(0x0E64, (self, local1, 33, 3, 38, 44, 0x000000B6, 0x000000B8))
        goto L6E

        L61:
        print "It is blank.\n"

        goto L00F4

        L71:
        if self.d1 != 0xFF: goto LA9

        if not opDB(self): goto L89

        return

        L89:
        local2 = op9B(0x04, (self, self.d2, 50, 50, 1, 1))

        print ref(0x3000, 0x0221) + self.D2

        goto LF4
  
        LA9:
        if self.aspect >= 2: goto LD6
 
        call_resource(0x0E64, (self, resource(0x0219) + self.d1, 33, 3, 38, 44, 0x000000B6, 0x000000B8))

        goto LF4

        LD6:
        call_resource(0x0E65, (self, resource(,0x0219) + self.d1, 17, 39, 52, 0x000000BC, 0x00000095))

        LF4:
        return
```
