
1105, Tome 



```
#object DObj

; 0x0047-0x009C
.Examine: function (self) {
  "It is a tome that teaches the spell '"
  set_local theSpell (
    opAD (
      push_byte 0x1C
      push_byte 0x00
      push_byte 0x00
      push_byte 0x00
      push_argument self
      get_field Prop.Data1
      push_byte 0x00
      push_byte 0x00
    )
  )

  set_local theSpell (
    push_local theSpell
    cast 0x50
  )

  print (
    call_method DObj.Look( ; 9D02
      push_local theSpell
    )
  )

  "'.\n"

  call_method DObj.Examine( ; 9D08
    push_local theSpell
  )

  delete (
    push_local theSpell
  )

  return (
    push_byte 0x00
  )  
}

; 0x009D-
.Use: function (self) {
  set_local castingSkill (
    call_resource 0x0EAC (  ; See also Stealing Script
      push_global gPlayerCharacter
      push_short 0x00C3     ; 1AC3 is the casting skill.
    )
  )
  if_not (
    push_local castingSkill
    logical_not
  ) then HAS_CASTING_SKILL

  "You have not even learned the fundamentals of magic "
  "- attempting to learn a spell is beyond you.\n"

  return ( 
    push_word None
  )


  HAS_CASTING_SKILL:
  if_not (
    get_skill (
      push_global gPlayerCharacter
      push_argument self
      get_field Prop.Data1
      
    )
  ) then DOES_NOT_KNOW_ALREADY 
  
  "You already know that spell.\n"

  goto SKIP_TO_END

  DOES_NOT_KNOW_ALREADY:
  set_local castingSkill (
    opAD ( ; creating an object with fields??
      push_byte 0x1C
      push_byte 0x00
      push_byte 0x00
      push_byte 0x00
      push_argument self
      get_field Prop.Data1
      push_byte 0x00
      push_byte 0x00
    )
  )

  set_local castingSkill (
    push_argument self
    cast 0x50
  )

  set_local local1 (
    push_global gPlayerCharacter
    cast Character
  )

  if_not (
    call_method 0x1A ( ; Object_50.Method_1A
      push_local castingSkill
      push_local local1
    )
  ) then FAILED_TO_LEARN

  set_attribute Object_50.Field_0B (
    push_local castingSkill 
  ) to (
    push_global gPlayerCharacter
  )

  set_local local2 (
    push_byte 0x00
  )
  set_local local3 (
    opA0 (; nb not table
      push_word 0x1:0000004
      push_byte 0x00
      push_byte 0x00
      push_word 0x0000080
    ) 
  )

  OP8C_LABEL:
  op8C (
    opA0 (
      push_word 0x1:0000004
      push_byte 0x01
    )
  ) then LEARNED_SPELL
  
  if_not (
    get_skill (
      push_local local1
      push_local local3
    ) 
  ) then SKIP_INCREMENT
  
  set_local local2 (
    push_local local2
    push_byte 0x01
    add
  )

  SKIP_INCREMENT:

  set_local local3 (
    opA0 (
      push_word 0x1:0000004
      push_byte 0x02
    )
  )

  goto OP8C_LABEL
  
  LEARNED_SPELL:
  "You now know the spell '"
  print (
    call_method DObj.Look (
      push_local castingSkill
    )
  )
  "', giving you "
  print (
    push_local local2
  )
  " of "
  print (
    call_resource 0x0EB5 ( 
      push_local local1
    )
  )
  " spells possible.\nTo cast it, select it from the character's"
  " skill list.\n"
  goto SKIP_TO_END

  FAILED_TO_LEARN:
  "You fail to learn '"
  print (
    call_method DObj.Look (
      push_local local2
    )
  )
  "'.\n"
  delete (
    castingSkill
  )

  SKIP_TO_END:
  return (
    push_byte 0x00
  )
}

.Field0015: None

.Field0027: None

.Field0032: None

; 0x0002-0x0046
.AskedAbout: array {
  "Many a spell has been learned from a tome like that."
  array {
    0x000004A
  }
}

.Field0D6D: None
```
