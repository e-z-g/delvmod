
This is an example script that comes with delv. 

```
include Delver.Main   // The system calls and globals are defined here.
resource 0x3039       // Change this if you paste it in somewhere else.
define globalToLookAt (Globals.CurrentZone)

function Dug(self) (
    'The value of the global '
    print
        byte globalToLookAt
    end
    ' is '
    print
        global globalToLookAt
    end
    '!\n'
    return
        byte 0
    end
)
```
