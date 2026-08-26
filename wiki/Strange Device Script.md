
1175, strange device 



```
class StrangeDevice(DObj):

   Field27 = None # sic

   Field2037 = None

   # 0x0002
   AskedAbout = ["Fascinating.  Clearly of Seldane construction, but for what purpose?, 
                 [People.Timon]
                ]

   # 0x0057
   Field24 = [0x0000004]

   # 0x005D
   Field27 = [0x0000008]

   def function_0063(self, arg1, arg2): # 4 locals [sic]
       local0 = self.separate_data[0x100]
       local1 = OpA0(word 0x10000002, 0, 0, 8)
       while not OpA0(word 0x10000002, 1):
           if arg1[local1] == local0[local1]:
               return 0
           local1 = OpA0(word 0x10000002, 2)
       #0x00AD
       play_sound(0x2C, self.x, self.y) # opening sound
       OpC5(arg2)
       return 0

   def function_00BE(self, arg1): # 5 locals
       local0 = self.separate_data[0x100]
       local1 = self.separate_data[0x101]
       local2 = [5, 3, 4, 5, 6, None, None, None]
       local3 = [3, 4, 7, 6, 7, None, None, None]


       while arg1 != None:
           local0[arg1] = 1 - local0[arg1]
           local4 = local1[arg1]
           local4.field37 = local0[arg1] + 0x35

           if not local0[arg1]:
               arg1 = local2[arg1] # mutable arguments.
               break
           else:
               arg1 = local3[arg1]

       function_0063(self, [1,0,1,0,0,1,0,1], 0x84)
       function_0063(self, [0,0,0,0,0,0,0,0], 0x85)
       function_0063(self, [1,1,1,1,1,1,1,1], 0x86)
       return 0

   def function_0F1B(self, arg1):
       function_00BE(self, 0) # 9E call this resource
       return 0

   def function_0209(self, arg1):
       function_00BE(self, 1)
       return 0

   def function_0217(self, arg1):
       function_00BE(self, 2)
       return 0
       

       
   # 0x0225
   def Use(self): 
       # Not disassembled yet
       # interesting highlight:
       local3.field39 = 0x1174:0x01FB # or 0x0209, or 0x219
       local3 = Op9B_0A(window?, 0x37, 0x38, 0, 0x19, 0x0a)
       # this variable local3 is repeatedly recycled.

   # 0x03CA
   def Examine(self): 
       "You see a round disk, with what appear to be three buttons and eight holes.\n"
       return 0
   



   


   
```
