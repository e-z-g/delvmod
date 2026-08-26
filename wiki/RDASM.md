
Installer VISE was used to package Cythera into a self-extracting installer.  



```
Pairs of bytes are swapped in the archive and encoded with a substitution cipher of some sort. At least all the URLs seem to use the same cypher. It is not clear yet if any other files do.
cy pt asc
30 6D m
33 5D ]
35 5B [
3B 52 R *
3E 0A \n *
42 76 v ?
44 3D = *
4F 57 W
5E 72 r
64 49 I
6D 68 h +
76 6F o
7F 41 A
8B 4C L *
93 53 S
9B 2E . ?
9C 69 i
9F 2F /
A9 3A :
B0 0D \r *
B2 64 d
BC 62 b
BF 63 c
C9 75 u
D8 70 p 
DA 6E n
E0 65 e
E9 55 U *
EA 74 t +
F6 61 a

```

BA C7 4D C7 79 C2 6D EA EA D8 A9 9F 9F 20 20 20 9B 7F 30 BC 5E 76 07  ?  ?  ?  ?  ?  ?  h  t  t  p  :  /  /  w  w  w  .  A  m  b  r  o  s 9C F6 93 4F 9B BF 76 30 9F B0 D8 C7 C7 i  a  S  W  .  c  o  m  /  \r p  ?  ? 

BA C7  B6 C7  A7 C2  35 64  DA EA  E0 5E  DA E0  EA 93  6D 76  5E EA ?  ?   ?  ?   ?  ?   [  I   n  t   e  r   n  e   t  S   h  o   r  t BF C9  EA 33  B0 3E  E9 3B  8B 44  6D EA  EA D8  A9 9F  9F 20  20 20 c  u   t  ]   \r \n  U  R   L  =   h  t   t  p   :  /   /  w   w  w 9B B2  E0 1F  42 E0  5E 9B  BF 76  30 9F  B0 3E  C7 C7 .  d   e  l   v  e   r  .   c  o   m  /   \r \n  ?  ? 



```
Data fork:
+0x00, magic number 'SVCT'
+0x24-0x28, address of table of entries, 0x0067D500 in case of cythera installer

Entry format:
4 Character signature
    Seen: 'PACK' (a combination of files constituting an install item?), 
          'FVCT' (a file),   
          'DVCT' (a directory)
           

'FVCT' entry:
'FVCT' signature
uint32 = 0
uint32 = 8 # flags?
uint32 = 1
uint32[6] = 0
uint32 = 1
char[4] = mac file type code
char[4] = mac creator code

01 00 
00 44 01 31 
00 00 
B2 A0 34 89 
B2 A0 34 89 
00 00 00 20 <-- could be compressed length (or maybe coincidence)
00 00 00 17 
00 00 00 00 
00 00 00 00 
48 EE 7A 92 
00 00 00 0C 
00 00 B3 F6 
00 02 00 01 

00 67 D4 E0 <-- offset?
00 00 00 

00 00 00 00 

00 03 22 00 

00 00 02 00 

00 00 00 15 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 8E A0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 43 79 74 68 65 72 61 20 57 65 62 20 53 69 74 65 20 28 4E 53 29




If that's its offset, here is the data there:
C7        BA        C7        AA        C2        08        EA        6D        D8        EA        9F        A9        20       
1100.0111 1011.1010 1100.0111 1010.1010 1100.0010 0000.1000 1110.1010 0110.1101 1101.1000 1110.1010 1001.1111 1010.1001 0010.0000
9F        20        20        B2        9B        1F        E0        E0        42        9B        5E        76        BF 
1001.1111 0010.0000 0010.0000 1011.0010 1001.1011 0001.1111 1110.0000 1110.0000 0100.0010 1001.1011 0101.1110 0111.0110 1011.1111
9F        30        44        B0        C7        C7
1001.1111 0011.0000 0100.0100 1011.0000 1100.0111 1100.0111

Plaintext - cythera's website
68        74        74        70        3A        2F        2F        77        77        77        2E        64        65 
0110.1000 0111.0100 0111.0100 0111.0000 0011.1010 0010.1111 0010.1111 0111.0111 0111.0111 0111.0111 0010.1110 0110.0100 0110.0101
6C        76        65        72        2E        63        6F        6D        2F        0D
0110.1100 0111.0110 0110.0101 0111.0010 0010.1110 0110.0011 0110.1111 0110.1101 0010.1111 0000.1101 

Ambrosia website NS data 00 67 D4 84 (termination unknown)
C7        BA        C7        4D        C2        79        EA        6D        D8        EA        9F        A9        20 
1100.0111 1011.1010 1100.0111 0100.1101 1100.0010 0111.1001 1110.1010 0110.1101 1101.1000 1110.1010 1001.1111 1010.1001 0010.0000
9F        20        20        7F        9B        BC        30        76        5E        9C        07        93        F6 
1001.1111 0010.0000 0010.0000 0111.1111 1001.1011 1011.1100 0011.0000 0111.0110 0101.1110 1001.1100 0000.0111 1001.0011 1111.0110
9B        4F        76        BF        9F        30        D8        B0        C7        C7       C7         BA        C7
1001.1011 0100.1111 0111.0110 1011.1111 1001.1111 0011.0000 1101.1000 1011.0000 1100.0111 1100.0111 1100.0111 1011.1010 1100.0111

Plaintext asw:
68        74       74        70        3A        2F        2F        77        77        77        2E        41        6D
0110.1000 0111.0100 0111.0100 0111.0000 0011.1010 0010.1111 0010.1111 0111.0111 0111.0111 0111.0111 0010.1110 0100.0001 0110.1101
62        72        6F        73        69        61        53        57        2E        63        6F        6D        2F  
0110.0010 0111.0010 0110.1111 0111.0011 0110.1001 0110.0001 0101.0011 0101.0111 0010.1110 0110.0011 0110.1111 0110.1101 0010.1111
0D
0000.1101

len:11011/27
(terminating - running into CVCT - 20 bytes long)


InputSprocket CH - first FVCT
compresse dlength? 7714
offset 0x0000002C
no inteligible strings seen even early - so not lzw...

```

Having another go. 

```
46 56 43 54  FVCT signature
00 00 00 00 
00 00 00 08 
00 00 00 01 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00
00 00 sometimes not 0, unknown 
00 01 often 1. unknown 
55 52 4C 20 mac type code 
4D 4F 53 53 mac creator code
01 00 seen 0500 as well 
00 44 01 31    seen -1 as well
00 00 
B2 A0 34 89 high entropy block. 
B2 A0 34 89 often the same number twice, but not always. B23235BD occurs in disparate contexts 

00 00 00 20 compressed length?
00 00 00 17 uncompressed length of data fork alone(definitely)

00 00 00 00 likely resource fork compressed length
00 00 00 00 definitely uncompressed length of resource fork alone

48 EE 7A 92 high entropy block

00 00 00 0C value 2 also seen

00 00 B3 F6 valuex b3f5, b3f6, b3f4 and b3f3 occur sequentially in four files, but 0xb3fb precedes them


00 02 00 01 
00 67 D4 E0 data fork offset in file (verified with sequential files - matches lengths)

00 00 00 00 not apparently the resource fork offset, oddly enough - probably it just follows the data fork immediately? should check with sequential resforkiferous files.
00 00 00 00 

03 22 00 00 00 02 00 00 00 00 15 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 8E A0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 43 79 74 68 65 72 61 20 57 65 62 20 53 69 74 65 20 28 4E 53 29

```

Oh look, the manual has a struct (different version of installer vise though) IVISE8.4UsersGuide.pdf 



```
struct ArcFileType {
Str32 af_Name; // File Name
Str32 af_Internal1; // Internal Use Only
unsigned long af_CreateDate; // Modificaton Date of File
unsigned long af_ModDate; // Modificaton Date of File
long af_DirID; // Directory ID
long af_Internal2; // Internal Use Only
long af_Internal3; // Internal Use Only
short af_Internal4; // Internal Use Only
short af_vRefNum; // Volume Reference Number
long af_CompDataFork; // Size of compressed data fork
long af_CompResFork; // Size of compressed resource fork
long af_unCompDataFork; // Size of uncompressed data fork
long af_unCompResFork; // Size of un compressed resource fork
long af_SegNumber; // Segment Number file is in
long af_Internal5; // Internal Use Only
long af_Internal6; // Internal Use Only
long af_Internal7; // Internal Use Only
unsigned long af_CRC; // Checksum
FInfo af_FInfo; // FileInfo
long af_Flags; // special location flags and replace flags
long af_ExtractFlags[2]; // gestalt calls bit flags (Gestalts to
call before installing this file)
long af_Internal8; // Internal Use Only
Handle af_ActionName; // Handle to name Action Item name
unsigned long af_CodePreActionFlags; // external code to call doing the
action of an Action Item - after the search
unsigned long af_CodeBeforeFlags; // external code to call before installing
flags
unsigned long af_CodeAfterFlags; // external code to call after installing
flags
short af_FatBinaryFlags; // when to install fat binary (see FAT
BINARY FLAGS above)
unsigned short af_UniqueID; // a unique number used by the installer
unsigned short af_MergeIntoID; // UniqueID of file to merge into
unsigned short af_InstallIfID; // Install this file if Install Action
item/fails succeeds
unsigned long af_Version; // 4 bytes 1st part, 2nd & 3rd parts, development
stage, prerelease version
unsigned char af_InstallWhen; // Install if Succeeds or Fails
unsigned char af_Directory; // File is a directory (if nonZero)
unsigned char af_Internal9; // Internal Use Only
unsigned char af_Internal10; // Internal Use Only
unsigned char af_InstallDisk; // disk the uncomp. file is supposed to be
on 0 = compressed
unsigned char af_Locked; // file - locked - from ioFlAttrib
unsigned long af_LanguageBits[2]; // PopMenu Value for "Language" Country
Code (1...37)
unsigned long af_RegionBits[2]; // PopMenu Value for "Region" Country Code
(1...62)
unsigned char af_Internal11; // Internal Use Only
long af_PackageFlags[kMaxPackFlags]; // package flags
long af_DirectiveFlags[kNumDirectiveLongs]; // Build directive
flags
unsigned long af_PathID; // Which folder is it in
unsigned char af_FileGroup; // File Group for Web Installer purposes
long af_LongNameIndex; // Internal Use Only
unsigned char af_InstallToDomain; // FindFolder() Domain constant used for
OSX
long af_UnixPrivBits; // Internal UNIX flags; rwx rwx rwx &
symbolic link
long af_UnixUserBits; // Internal UNIX flags; set user to
wheel, root, etc.
};
typedef struct ArcFileType ArcFileType;
typedef ArcFileType *ArcFilePtr;
```

That struct isn't directly applicable (the name format for example is different) to the binary data on disk, and clearly the field order is different. But the fields are probably basically the same. It identifies a checksum as CRC, as an unsigned long.   It is known that mutating the installer causes per-file checksums to fail (with no incorrect expanded output being produced to disk - will have to pull it out of memory presumably to do mutation experiments). Or can the checksum be disabled? They would probably want that feature for testing.  

--- data --- 

Cythera web site IE 

```
Compressed
C7 BA C7 B6 C2 A7 64 35 EA DA 5E E0 E0 DA 93 EA 76 6D EA 5E C9 BF 33 EA 3E B0 3B E9 44 8B EA 6D D8 EA 9F A9 20 9F 20 20 B2 9B 1F E0 E0 42 9B 5E 76 BF 9F 30 3E B0 C7 C7

Plain
5B 49 6E 74 65 72 6E 65 74 53 68 6F 72 74 63 75 74 5D 0D 0A 55 52 4C 3D 68 74 74 70 3A 2F 2F 77 77 77 2E 64 65 6C 76 65 72 2E 63 6F 6D 2F 0D 0A
```

Cythera web site NS 

```
Compressed
C7 BA C7 AA C2 08 EA 6D D8 EA 9F A9 20 9F 20 20 B2 9B 1F E0 E0 42 9B 5E 76 BF 9F 30 44 B0 C7 C7

Plaintext
68 74 74 70 3A 2F 2F 77 77 77 2E 64 65 6C 76 65 72 2E 63 6F 6D 2F 0D
```

Ambrosia website NS 

```
Compressed
C7 BA C7 4D C2 79 EA 6D D8 EA 9F A9 20 9F 20 20 7F 9B BC 30 76 5E 9C 07 93 F6 9B 4F 76 BF 9F 30 D8 B0 C7 C7

Plaintext
68 74 74 70 3A 2F 2F 77 77 77 2E 41 6D 62 72 6F 73 69 61 53 57 2E 63 6F 6D 2F 0D
```

Ambrosia website IE 

```
Compressed
C7 BA C7 61 C2 C1 64 35 EA DA 5E E0 E0 DA 93 EA 76 6D EA 5E C9 BF 33 EA 3E B0 3B E9 44 8B EA 6D D8 EA 9F A9 20 9F 20 20 F6 9B BC 30 76 5E 9C 07 07 F6 9B 20 76 BF 9F 30 3E B0 C7 C7

Plaintext
5B 49 6E 74 65 72 6E 65 74 53 68 6F 72 74 63 75 74 5D 0D 0A 55 52 4C 3D 68 74 74 70 3A 2F 2F 77 77 77 2E 61 6D 62 72 6F 73 69 61 73 77 2E 63 6F 6D 2F 0D 0A
```

Decoding based on the struct in the manual 

```
Having another go. Netscape http://www.delver.com/\r
{{{
46 56 43 54  FVCT signature
00 00 00 00 
00 00 00 08 
00 00 00 01 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00
00 00 sometimes not 0, unknown 
00 01 often 1. unknown 
55 52 4C 20 mac type code 
4D 4F 53 53 mac creator code
01 00 seen 0500 as well 
00 44 01 31    seen -1 as well
00 00 
B2 A0 34 89 high entropy block. 
B2 A0 34 89 often the same number twice, but not always. B23235BD occurs in disparate contexts 

00 00 00 20 compressed length?
00 00 00 17 uncompressed length of data fork alone(definitely)

00 00 00 00 likely resource fork compressed length
00 00 00 00 definitely uncompressed length of resource fork alone

48 EE 7A 92 high entropy block - this is a crc-32, same as python's binascii.crc32, of uncompressed data fork (+res fork? needs to be checked)

00 00 00 0C value 2 also seen

00 00 B3 F6 valuex b3f5, b3f6, b3f4 and b3f3 occur sequentially in four files, but 0xb3fb precedes them


00 02 00 01 
00 67 D4 E0 data fork offset in file (verified with sequential files - matches lengths)

00 00 00 00 not apparently the resource fork offset, oddly enough - probably it just follows the data fork immediately? should check with sequential resforkiferous files.
00 00 00 00 

03 22 00 00 00 02 00 00 00 00 15 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 8E A0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 43 79 74 68 65 72 61 20 57 65 62 20 53 69 74 65 20 28 4E 53 29
```
