
This is the version of the Fetch spell that has been modified to operate correctly, hopefully. RIP Fetch Bug, ca. 1997-2016. 

```
; Skill and Spell Objects: Fetch (0x1A28)
; Cythera Community Bugfix Patch Sources, based on:
;   The Annotated Unofficial Cythera Sources (TAUCS 1.0.4)
; Commentator: Bryce Schroeder <bryce.schroeder@gmail.com>
; Fixer: Bryce Schroeder
; Produced as part of the delv project. 
; http://www.ferazelhosting.net/wiki/Cythera

include Delver.Model
include Delver.Main
include Cythera
use System
resource 0x1A28
class Object

; The significance of the ordering is not yet appreciated, but seems to be
; relevant somehow. Perhaps the 'empty' slots are just holding spaces for when
; a class doesn't implement a method.
field_order (0x0695, 0x0008, 0x0002, 0x0036, 0x0009, 0x0036, 0x0696, 0x0696,
             0x0008, 0x0009, 0x000A, 0x000B, 0x0033)
class_field 0x000B none
class_field 0x0695 none
class_field 0x0696 none

; Tells the AI what kind of spell this is (in this case a utility spell,
; which as far as I know the AI doesn't use.
array AIInformation( AISpellTypes.Utility )

; Return the short name of the spell (analogous to the method of items
; that returns the name you see when you mouse over them.)
function Look(Self) (
    return 
        string "Fetch"
    end 
    return 
        byte 0
    end 
)

; This stores the Level and Prerequisite for skills. Fetch has no
; prerequisite.
array AskedAbout( 6 none )

; Print out a more detailed description of the spell.
function Examine(Self) (
    'This spell brings a small distant object to the caster.\n'
    return 
        byte 0
    end 
)

; This code is run when the player (or AI, in principle) attempts to
; cast the spell.
function Use(Self) (
    if_not 
        call_resource RPGUtil.CastSpell
            ; A character is considered a container for skills.
            ; Hence we get the character posessing this instance of
            ; this skill class with this field.
            arg Self
            get_field DObj.container  

            ; The spell level of Fetch
            byte 6 

            ; The mana cost
            byte 24 
        end
    then CastingFailed

    ; If this is an NPC casting, we will skip printing out the prompt
    ; explaining to the user that a target is needed.
    if_not 
        global Globals.IsPlayerTurn
    then CastingSucceeded


    'Cast \''

    ; The console prints out the name of the spell when the skill object
    ; is printed (equivalent to calling the Look method directly.)
    print 
        method Object.Look
            arg Self
        end 
    end 

    '\' on what?\n'

    ; If our casting was successful, we will need to target an item
    ; to fetch. This tells the interface to get one from the user 
    ; or AI. (In the general case; the AI doesn't use Fetch.)
    CastingSucceeded:
    return 
        byte UseReturnCodes.TargetItemRequired
    end 

    ; If the casting failed, then we don't need a target, naturally.
    CastingFailed:
    return 
        byte UseReturnCodes.NothingRequired
    end 
)

; After the user has specified a target for the spell, this code actually
; implements the effect.
function UseOn(Self, Target) (

    ; Display a nifty purple aura around the caster.
    sys MagicAuraEffect
        global Globals.CurrentCharacter

        ; This cast is apparently unnecessary
        cast Types.Prop   
        
        ; This is one of the palette animated colors
        word ColorOfMagic 
    end 


    ; Play the sound effect. Takes the caster position so that it can
    ; properly do stereo sound. Self is the spell instance itself in this
    ; class, so we have to retrieve the caster from a global variable that
    ; holds the character whose turn it is (and ipso facto must be the 
    ; caster since a character can only cast a spell on his or her turn.)
    sys PlaySound
        byte Sounds.Magic5

        global Globals.CurrentCharacter
        get_field DObj.x

        global Globals.CurrentCharacter
        get_field DObj.y
    end 

    ; Check for an object already in the inventory or container.
    if
        arg Target
        get_field DObj.flags
        byte 0x10
        eq
        arg Target
        get_field DObj.flags
        byte 0x08
        bitwise_and
        or
    then AlreadyInInventory

    ; If the object flags are not equal to 0 or 1, fail because of the
    ; object's ostensible size/weight.
    if_not 
        arg Target
        get_field DObj.flags
        byte PropFlags.OnMap
        eq
 
        arg Target
        get_field DObj.flags
        byte PropFlags.OnMapNotStealing
        eq 

        or 
    then TooLargeAndHeavy


    ; We here exclude non-weighable objects.
    if_not
        arg Target
        has_field 0x24
    then TooSticky


    ; At this point we have decided that the object is in fact fetchable.
    ; We have to see if it will in fact fit, though, in the player's 
    ; inventory.
    if_not
        sys GetWeight
            arg Target
            field DObj.aspect_and_proptype
            arg Target
            field DObj.unkn09
        end
        sys WeightCapacity
            global Globals.CurrentCharacter
        end
        le
    then InventoryFull
    


    ; In this branch, we have found that the object will fit in the
    ; player's inventory.
    set_field DObj.flags
        arg Target
    end 
        byte 0x10
    end 

    set_field DObj.x
        arg Target
    end 
        byte 0
    end 

    set_field DObj.y
        arg Target
    end 
        byte 1
    end 

    set_field DObj.container
        arg Target
    end 
        global Globals.CurrentCharacter
    end 

    ; Tell the object it was picked up
    method Object.PutInside
        arg Target
    end

    ; We removed something from the window, so we need to tell
    ; the world view to redraw itself (without the object, in this
    ; case.)
    sys RefreshView 
        ; Significance of the parameter is unknown.
        byte 1 
    end 

    branch Success

    
    ; In this branch the spell is successful but the player's inventory is
    ; too full, so the item lands at their feet instead.
    InventoryFull:
    'The item falls to your feet.\n'
    set_field DObj.x
        arg Target
    end 
        global Globals.CurrentCharacter
        get_field DObj.x
    end 

    set_field DObj.y
        arg Target
    end 
        global Globals.CurrentCharacter
        get_field DObj.y
    end 
    
    branch Success


    TooLargeAndHeavy:
    'It is too large and heavy.\n'
    branch TheEnd

    TooSticky:
    'It doesn\'t seem possible to retrieve that.\n'
    branch TheEnd

    AlreadyInInventory:
    'It won\'t come free.\n'
    branch TheEnd


    Success:
    sys RefreshView 
        byte 1 
    end 

    TheEnd:
    return 
        byte 0
    end 
) 

```
