


```
 ---- SUBINDEX 4 ---- 
Index 0, ID 0500 Length: 20 bytes

Index 1, ID 0501 Length: 276 bytes
  This contains the initial stats and skills for starting characters. (Note that the strings in 0205/0206 are purely cosmetic
  and in fact contain errors.) 0501 contains an array of arrays, one array for each character archetype; idx 0, 1, and 2 are for
  initial Body, Reflex and Mind respectively. There is one subsequent integer in the array for each skill aptitude. The integer's
  lower ten bits are added to 1A00 to get the resource ID of the skill object; the upper bits of the integer are shifted right 10
  to get the number of starting aptitude levels. Why this complicated arrangement was favored over simply having two
  integers for each skill aptitude (one for the skill's ID, one for the number of levels) gandreas only knows.

Index 64, ID 0540 Length: 4 bytes
```
