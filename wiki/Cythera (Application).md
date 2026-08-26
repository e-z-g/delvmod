
These give the names of tiles/objects. The Value associated with each one is the index of the highest tile with that name in the tiles (8Exx resources), e.g. in resource 8E00 we have Nothing at position 0, grass at position 1, swamp at positions 2,3 and 4, a shrub at position 5, and two tiles of swamp that have faux props (bushes, as it happens) at index 6 and 7. 8-15 are water. How this pattern matches to the F004 values is fairly clear on examination of the table below. 


|_Index_| | **Value** | **String**|
|-|-|-|-|
|0 | 0000 | 0000 | Nothing|
|1 | 0001 | 0001 | grass|
|2 | 0002 | 0004 | swamp|
|3 | 0003 | 0005 | shrub|
|4 | 0004 | 0007 | bush|
|5 | 0005 | 000F | water|
|6 | 0006 | 002F | shore|
|7 | 0007 | 0033 | tree|
|8 | 0008 | 003F | grass|
|9 | 0009 | 0047 | tree|
|10 | 000A | 0048 | dead tree|
|11 | 000B | 004D | scrub|
|12 | 000C | 004E | shrub|
|13 | 000D | 005F | earth|
|14 | 000E | 006B | embankment|
|15 | 000F | 006F | earth|
|16 | 0010 | 007C | mountain|
|17 | 0011 | 008B | snowcaps|
|18 | 0012 | 00BB | wall|
|19 | 0013 | 00BC | field|
|20 | 0014 | 00BF | crops|
|21 | 0015 | 00C3 | arrow slit|
|22 | 0016 | 00C5 | window|
|23 | 0017 | 00C7 | crenellation|
|24 | 0018 | 00CD | window|
|25 | 0019 | 00CE | |
|26 | 001A | 00CF | abyss|
|27 | 001B | 00D2 | floor|
|28 | 001C | 00D3 | sand|
|29 | 001D | 00D8 | floor|
|30 | 001E | 00D9 | wet earth|
|31 | 001F | 00DA | puddle|
|32 | 0020 | 00DB | pool|
|33 | 0021 | 00DC | floor|
|34 | 0022 | 00DF | lava|
|35 | 0023 | 00E5 | limestone wall|
|36 | 0024 | 00EF | pyramid|
|37 | 0025 | 00FB | earthen wall|
|38 | 0026 | 00FE | ethereal void|
|39 | 0027 | 00FF | |
|40 | 0028 | 0103 | farmlands|
|41 | 0029 | 0107 | ruins|
|42 | 002A | 010B | floor|
|43 | 002B | 010D | brick wall|
|44 | 002C | 010F | wall|
|45 | 002D | 0113 | brick wall|
|46 | 002E | 0116 | pattern|
|47 | 002F | 011E | large city|
|48 | 0030 | 011F | stronghold|
|49 | 0031 | 0120 | encampment|
|50 | 0032 | 0121 | small city|
|51 | 0033 | 0122 | farmhouse|
|52 | 0034 | 012F | roof|
|53 | 0035 | 0137 | rubble|
|54 | 0036 | 013B | rubble|
|55 | 0037 | 013E | ivy|
|56 | 0038 | 013F | scratch|
|57 | 0039 | 0141 | cattails|
|58 | 003A | 0142 | brick wall|
|59 | 003B | 0143 | brick wall|
|60 | 003C | 0144 | brick wall|
|61 | 003D | 0145 | brick wall|
|62 | 003E | 0147 | limestone wall|
|63 | 003F | 014F | crumbled roof|
|64 | 0040 | 0153 | crenellation|
|65 | 0041 | 015D | tent roof|
|66 | 0042 | 01C9 | pyramid|
|67 | 0043 | 01FB | slate roof|
|68 | 0044 | 0200 | mace|
|69 | 0045 | 0201 | dagger|
|70 | 0046 | 0202 | club|
|71 | 0047 | 0203 | axe|
|72 | 0048 | 0205 | sword|
|73 | 0049 | 0206 | spear|
|74 | 004A | 0207 | hatchet|
|75 | 004B | 0208 | flail|
|76 | 004C | 0209 | sword|
|77 | 004D | 020A | diamond|
|78 | 004E | 020B | bow|
|79 | 004F | 020C | sling|
|80 | 0050 | 020E | sling stone\s|
|81 | 0051 | 0214 | sling stone\s|
|82 | 0052 | 0215 | strange rod|
|83 | 0053 | 0216 | cuirass|
|84 | 0054 | 0217 | metal breast plate|
|85 | 0055 | 0218 | buckler|
|86 | 0056 | 0219 | light shield|
|87 | 0057 | 021A | round shield|
|88 | 0058 | 021B | full shield|
|89 | 0059 | 021C | leather helmet|
|90 | 005A | 021D | helmet|
|91 | 005B | 021E | full helmet|
|92 | 005C | 021F | grimoire|
|93 | 005D | 0220 | scroll|
|94 | 005E | 0224 | ring|
|95 | 005F | 0225 | [LandKing](LandKing) Amulet|
|96 | 0060 | 0226 | black disk|
|97 | 0061 | 0227 | tome|
|98 | 0062 | 022F | potion|
|99 | 0063 | 0230 | unlit torch\es|
|100 | 0064 | 0231 | lit torch\es|
|101 | 0065 | 0232 | spent torch\es|
|102 | 0066 | 0234 | key|
|103 | 0067 | 0236 | key|
|104 | 0068 | 0238 | half disk|
|105 | 0069 | 023F | glowing crystal|
|106 | 006A | 0245 | book|
|107 | 006B | 0246 | flatbread|
|108 | 006C | 0247 | bread|
|109 | 006D | 0248 | cheese|
|110 | 006E | 0249 | grapes|
|111 | 006F | 024A | pomegranate|
|112 | 0070 | 024B | meatpie|
|113 | 0071 | 024C | kabobs|
|114 | 0072 | 024D | fowl|
|115 | 0073 | 024E | meat|
|116 | 0074 | 024F | fish|
|117 | 0075 | 0250 | meat|
|118 | 0076 | 0251 | sausage|
|119 | 0077 | 0252 | steak|
|120 | 0078 | 0253 | butter|
|121 | 0079 | 0255 | meat|
|122 | 007A | 0256 | mushroom steak|
|123 | 007B | 0257 | dried jellyfish|
|124 | 007C | 0258 | dried fruit|
|125 | 007D | 0259 | seedpod|
|126 | 007E | 025A | sulfur|
|127 | 007F | 025B | obsidian|
|128 | 0080 | 025C | spider web|
|129 | 0081 | 025D | peppermint|
|130 | 0082 | 025E | ruby|
|131 | 0083 | 025F | bean|
|132 | 0084 | 0263 | paper|
|133 | 0085 | 0264 | inkwell|
|134 | 0086 | 0265 | map|
|135 | 0087 | 0266 | strange device|
|136 | 0088 | 0267 | map|
|137 | 0089 | 0268 | tunic|
|138 | 008A | 0269 | kilt|
|139 | 008B | 026A | skirt|
|140 | 008C | 026B | dress|
|141 | 008D | 026C | pants|
|142 | 008E | 026D | long dress|
|143 | 008F | 026E | dress|
|144 | 0090 | 026F | dress|
|145 | 0091 | 0270 | tunic|
|146 | 0092 | 0272 | dress|
|147 | 0093 | 0273 | cape|
|148 | 0094 | 0274 | cape|
|149 | 0095 | 0275 | cloak|
|150 | 0096 | 0276 | sandals|
|151 | 0097 | 0277 | boots|
|152 | 0098 | 027F | obol\s/oi|
|153 | 0099 | 0281 | glowing crystal|
|154 | 009A | 0282 | sack|
|155 | 009B | 0283 | pouch|
|156 | 009C | 0287 | chest|
|157 | 009D | 028B | coffer|
|158 | 009E | 028D | lamp|
|159 | 009F | 0290 | candle|
|160 | 00A0 | 0293 | candleabra|
|161 | 00A1 | 0296 | candlestand|
|162 | 00A2 | 0299 | candles|
|163 | 00A3 | 029A | fishing pole|
|164 | 00A4 | 029B | fishing net|
|165 | 00A5 | 029C | lobster trap|
|166 | 00A6 | 029D | lockpick|
|167 | 00A7 | 029F | strange staff|
|168 | 00A8 | 02A0 | eartheart mushroom|
|169 | 00A9 | 02A1 | egg|
|170 | 00AA | 02A2 | gator boots|
|171 | 00AB | 02A3 | piece of kelp|
|172 | 00AC | 02A7 | seaweed|
|173 | 00AD | 02AF | wheelbarrow|
|174 | 00AE | 02B3 | loom|
|175 | 00AF | 02B4 | spinning wheel|
|176 | 00B0 | 02B7 | thread|
|177 | 00B1 | 02BA | cloth|
|178 | 00B2 | 02BB | bale of flax|
|179 | 00B3 | 02BC | plow|
|180 | 00B4 | 02BD | lute|
|181 | 00B5 | 02BE | panpipes|
|182 | 00B6 | 02BF | lyre|
|183 | 00B7 | 02C0 | scythe|
|184 | 00B8 | 02C1 | rake|
|185 | 00B9 | 02C2 | pitchfork|
|186 | 00BA | 02C3 | shovel|
|187 | 00BB | 02C4 | hoe|
|188 | 00BC | 02C6 | pitcher|
|189 | 00BD | 02C7 | pan|
|190 | 00BE | 02C8 | pot|
|191 | 00BF | 02C9 | skillet|
|192 | 00C0 | 02CA | mystic helmet|
|193 | 00C1 | 02CB | mystic armor|
|194 | 00C2 | 02CC | mystic spear|
|195 | 00C3 | 02CD | sign holder|
|196 | 00C4 | 02CE | pail|
|197 | 00C5 | 02CF | pail of water|
|198 | 00C6 | 02D0 | pail of milk|
|199 | 00C7 | 02D1 | rolling pin|
|200 | 00C8 | 02D2 | basket|
|201 | 00C9 | 02D3 | laddle|
|202 | 00CA | 02D4 | large spoon|
|203 | 00CB | 02D5 | bowl|
|204 | 00CC | 02D6 | bowl|
|205 | 00CD | 02D7 | bag of flour|
|206 | 00CE | 02D8 | flour|
|207 | 00CF | 02DA | dough|
|208 | 00D0 | 02DB | spatula|
|209 | 00D1 | 02DC | cleaver|
|210 | 00D2 | 02DD | churn|
|211 | 00D3 | 02DE | odd helmet|
|212 | 00D4 | 02DF | unguent|
|213 | 00D5 | 02E0 | anvil|
|214 | 00D6 | 02E1 | tongs|
|215 | 00D7 | 02E2 | bellows|
|216 | 00D8 | 02E3 | bellows|
|217 | 00D9 | 02EB | firepit|
|218 | 00DA | 02EC | water trough|
|219 | 00DB | 02ED | wood|
|220 | 00DC | 02EE | blacksmith hammer|
|221 | 00DD | 02EF | miner's pick|
|222 | 00DE | 02F3 | urn|
|223 | 00DF | 02F7 | vat|
|224 | 00E0 | 02FB | empty vat|
|225 | 00E1 | 02FE | floor|
|226 | 00E2 | 02FF | stirrup jar|
|227 | 00E3 | 0301 | crate|
|228 | 00E4 | 0305 | chair|
|229 | 00E5 | 0306 | end table|
|230 | 00E6 | 0308 | desk|
|231 | 00E7 | 030C | dresser|
|232 | 00E8 | 030D | throne|
|233 | 00E9 | 030F | person sleeping|
|234 | 00EA | 0313 | bed|
|235 | 00EB | 0317 | palette|
|236 | 00EC | 031B | chair|
|237 | 00ED | 031C | post|
|238 | 00EE | 031F | rope|
|239 | 00EF | 0321 | rug|
|240 | 00F0 | 032C | carpet|
|241 | 00F1 | 032D | plaque|
|242 | 00F2 | 032F | chair|
|243 | 00F3 | 033B | bookshelf|
|244 | 00F4 | 033C | lit wall torch|
|245 | 00F5 | 033D | unlit wall torch|
|246 | 00F6 | 033E | mirror|
|247 | 00F7 | 033F | mirror|
|248 | 00F8 | 0340 | broken mirror|
|249 | 00F9 | 0341 | plate|
|250 | 00FA | 0342 | dinner knife|
|251 | 00FB | 0343 | spoon|
|252 | 00FC | 0344 | fork|
|253 | 00FD | 0345 | pewter mug|
|254 | 00FE | 0346 | glass|
|255 | 00FF | 034A | debris|
|256 | 0100 | 034C | stepping stone|
|257 | 0101 | 034E | flowers|
|258 | 0102 | 034F | plant|
|259 | 0103 | 0358 | table|
|260 | 0104 | 035C | shadow|
|261 | 0105 | 0369 | table|
|262 | 0106 | 036D | conjurer's triangle|
|263 | 0107 | 0373 | passthrough|
|264 | 0108 | 0374 | tableleg|
|265 | 0109 | 0375 | tableleg|
|266 | 010A | 037B | ruined floor|
|267 | 010B | 037F | table|
|268 | 010C | 0382 | ladder|
|269 | 010D | 0385 | floor|
|270 | 010E | 0389 | fountain|
|271 | 010F | 038D | pool|
|272 | 0110 | 0391 | stove|
|273 | 0111 | 0395 | pillar|
|274 | 0112 | 0399 | rubble|
|275 | 0113 | 039B | hole|
|276 | 0114 | 039D | waterfall|
|277 | 0115 | 039F | stalagmites|
|278 | 0116 | 03A4 | trapdoor|
|279 | 0117 | 03A8 | ruins|
|280 | 0118 | 03A9 | altar|
|281 | 0119 | 03AA | standing stone|
|282 | 011A | 03AC | campfire|
|283 | 011B | 03AD | tombstone|
|284 | 011C | 03B0 | tombstone|
|285 | 011D | 03B1 | grave|
|286 | 011E | 03B2 | open grave|
|287 | 011F | 03B7 | cobwebs|
|288 | 0120 | 03C1 | well|
|289 | 0121 | 03C2 | pedestal|
|290 | 0122 | 03C5 | trellis|
|291 | 0123 | 03C8 | trellis|
|292 | 0124 | 03CA | pole|
|293 | 0125 | 03CC | lever|
|294 | 0126 | 03D5 | sundial|
|295 | 0127 | 03D9 | spit|
|296 | 0128 | 03DF | distiller|
|297 | 0129 | 03E2 | mushrooms|
|298 | 012A | 03EF | mushroom|
|299 | 012B | 03F1 | mineshaft|
|300 | 012C | 03F3 | mineshaft|
|301 | 012D | 03F7 | cave|
|302 | 012E | 03FB | sewer|
|303 | 012F | 03FD | pipe|
|304 | 0130 | 0401 | arch|
|305 | 0131 | 0407 | stairs|
|306 | 0132 | 040B | steps|
|307 | 0133 | 040D | crossbeams|
|308 | 0134 | 040F | mousehole|
|309 | 0135 | 041F | oak door|
|310 | 0136 | 042F | windowed door|
|311 | 0137 | 043F | metal door|
|312 | 0138 | 0443 | doorway|
|313 | 0139 | 0447 | archway|
|314 | 013A | 044B | doorway|
|315 | 013B | 044F | archway|
|316 | 013C | 0457 | stone door|
|317 | 013D | 045B | adobe arch|
|318 | 013E | 045F | secret door|
|319 | 013F | 0463 | portcullis|
|320 | 0140 | 0467 | secret passage|
|321 | 0141 | 046F | wooden door|
|322 | 0142 | 0477 | curtain|
|323 | 0143 | 047B | stone doorway|
|324 | 0144 | 0481 | limestone wall|
|325 | 0145 | 0482 | tight passage|
|326 | 0146 | 0484 | wall shelf|
|327 | 0147 | 0486 | bell stand|
|328 | 0148 | 0487 | liquid|
|329 | 0149 | 048F | bell|
|330 | 014A | 049F | flag|
|331 | 014B | 04AF | sign|
|332 | 014C | 04B1 | poster|
|333 | 014D | 04B7 | fence|
|334 | 014E | 04B8 | haystack|
|335 | 014F | 04BB | haystack|
|336 | 0150 | 04C7 | steps|
|337 | 0151 | 04CB | rock|
|338 | 0152 | 04CF | boulder|
|339 | 0153 | 04D3 | rockpile|
|340 | 0154 | 04DF | grafitti|
|341 | 0155 | 04EF | statue|
|342 | 0156 | 04F3 | fireplace|
|343 | 0157 | 04F7 | force wall|
|344 | 0158 | 04F8 | ground|
|345 | 0159 | 04F9 | chaos|
|346 | 015A | 04FB | button|
|347 | 015B | 04FF | secret passage|
|348 | 015C | 0507 | asp|
|349 | 015D | 050B | bird|
|350 | 015E | 050F | chicken|
|351 | 015F | 0517 | goat|
|352 | 0160 | 051F | crab|
|353 | 0161 | 0527 | ratlizard|
|354 | 0162 | 052F | wolflizard|
|355 | 0163 | 054F | titan|
|356 | 0164 | 0553 | crack|
|357 | 0165 | 055F | skeleton|
|358 | 0166 | 056F | ooze|
|359 | 0167 | 0573 | tentacle|
|360 | 0168 | 057B | sea monster|
|361 | 0169 | 057F | land jellyfish|
|362 | 016A | 0587 | giant slug|
|363 | 016B | 058F | sleeping seldane|
|364 | 016C | 059B | small city|
|365 | 016D | 059F | pyramid|
|366 | 016E | 05AF | large city|
|367 | 016F | 05B7 | harpy|
|368 | 0170 | 05BF | ghost|
|369 | 0171 | 05CF | corpse|
|370 | 0172 | 05D7 | demon|
|371 | 0173 | 05DF | golem|
|372 | 0174 | 05F7 | corpse|
|373 | 0175 | 05FB | bones|
|374 | 0176 | 05FF | blood|
|375 | 0177 | 060F | guard|
|376 | 0178 | 061F | ruffian|
|377 | 0179 | 062F | nobleman|
|378 | 017A | 063F | noblewoman|
|379 | 017B | 064F | man|
|380 | 017C | 065F | woman|
|381 | 017D | 066F | beggar|
|382 | 017E | 067F | child|
|383 | 017F | 068F | mage|
|384 | 0180 | 069F | magess|
|385 | 0181 | 06AF | man|
|386 | 0182 | 06BF | woman|
|387 | 0183 | 06CF | seldane|
|388 | 0184 | 06DF | seldane|
|389 | 0185 | 06EF | seldane|
|390 | 0186 | 06FF | fighter|
|391 | 0187 | 0707 | skeleton|
|392 | 0188 | 070F | undead|
|393 | 0189 | 071F | king|
|394 | 018A | 072F | fool|
|395 | 018B | 073F | hero|
|396 | 018C | 074F | heroine|
|397 | 018D | 075F | hunter|
|398 | 018E | 076F | workman|
|399 | 018F | 077F | Strange Device|
|400 | 0190 | 079F | hydra|
|401 | 0191 | 07A7 | shore|
|402 | 0192 | 07A8 | loose dirt|
|403 | 0193 | 07A9 | open hole|
|404 | 0194 | 07AA | fumerole|
|405 | 0195 | 07AB | Rune of Warding|
|406 | 0196 | 07AC | Rune of Flame|
|407 | 0197 | 07AD | Rune of Pain|
|408 | 0198 | 07AE | Rune of Blocking|
|409 | 0199 | 07AF | spikes|
|410 | 019A | 07BF | unicorn|
|411 | 019B | 07CF | gator|
|412 | 019C | 07D7 | polyp|
|413 | 019D | 07DF | firespirit|
|414 | 019E | 07EF | fresco|
|415 | 019F | 07FF | lich|
|416 | 01A0 | 0803 | hourglass|
|417 | 01A1 | 0805 | open shutters|
|418 | 01A2 | 0807 | closed shutters|
|419 | 01A3 | 0808 | open drapes|
|420 | 01A4 | 0809 | closed drapes|
|421 | 01A5 | 080A | gavel|
|422 | 01A6 | 080B | hand mirror|
|423 | 01A7 | 080C | broken hand mirror|
|424 | 01A8 | 080D | mortar and pestle|
|425 | 01A9 | 080E | decorative axe|
|426 | 01AA | 080F | rock|
|427 | 01AB | 0813 | archery target|
|428 | 01AC | 0814 | brazier|
|429 | 01AD | 0815 | lit brazier|
|430 | 01AE | 0816 | bomb|
|431 | 01AF | 0817 | lit bomb|
|432 | 01B0 | 081F | lamp post|
|433 | 01B1 | 0825 | footprints|
|434 | 01B2 | 0826 | wall|
|435 | 01B3 | 0827 | rope|
|436 | 01B4 | 082B | mounted head|
|437 | 01B5 | 082D | sword dummy|
|438 | 01B6 | 082E | scale|
|439 | 01B7 | 082F | dice|
|440 | 01B8 | 0830 | broken sword|
|441 | 01B9 | 0831 | broken sword|
|442 | 01BA | 0832 | broken axe|
|443 | 01BB | 0833 | broken bow|
|444 | 01BC | 0834 | broken shield|
|445 | 01BD | 0845 | bridge|
|446 | 01BE | 0848 | bridge|
|447 | 01BF | 0849 | crack|
|448 | 01C0 | 084A | crevice|
|449 | 01C1 | 084C | abyss|
|450 | 01C2 | 084D | crevice|
|451 | 01C3 | 084E | crack|
|452 | 01C4 | 0853 | abyss|
|453 | 01C5 | 0854 | loose rock|
|454 | 01C6 | 085C | rope bridge|
|455 | 01C7 | 085D | rock outcropping|
|456 | 01C8 | 085E | rope down|
|457 | 01C9 | 085F | rope up|
|458 | 01CA | 0863 | easel|
|459 | 01CB | 0864 | palette|
|460 | 01CC | 0865 | paintbrush|
|461 | 01CD | 0869 | moss|
|462 | 01CE | 086F | water pool|
|463 | 01CF | 0870 | incense burner|
|464 | 01D0 | 0874 | burning incense|
|465 | 01D1 | 0875 | wall hanging|
|466 | 01D2 | 0876 | poison trap|
|467 | 01D3 | 0877 | blast trap|
|468 | 01D4 | 0879 | pillar|
|469 | 01D5 | 087A | portal|
|470 | 01D6 | 087B | bust|
|471 | 01D7 | 087F | petroglyphs|
|472 | 01D8 | 0880 | fur cloak|
|473 | 01D9 | 0881 | belt|
|474 | 01DA | 0882 | gauntlets|
|475 | 01DB | 0886 | crystal ball|
|476 | 01DC | 0887 | boards|
|477 | 01DD | 088B | staff|
|478 | 01DE | 0891 | painting|
|479 | 01DF | 0893 | gong|
|480 | 01E0 | 0897 | crab|
|481 | 01E1 | 089B | gecko|
|482 | 01E2 | 089F | sylph|
|483 | 01E3 | 08CD | wall|
|484 | 01E4 | 08CF | limestone wall|
|485 | 01E5 | 08D0 | earthen wall|
|486 | 01E6 | 08D1 | earthen wall|
|487 | 01E7 | 08D2 | small hole|
|488 | 01E8 | 08D3 | small tube|
|489 | 01E9 | 08D4 | small rod|
|490 | 01EA | 08D5 | small hole|
|491 | 01EB | 08D7 | fine wire|
|492 | 01EC | 08D8 | loose board|
|493 | 01ED | 08DB | loose stone|
|494 | 01EE | 08DC | small crack|
|495 | 01EF | 08EF | ancient tree|
|496 | 01F0 | 08F7 | magic arrow\s|
|497 | 01F1 | 08FF | arrow\s|
|498 | 01F2 | 0903 | tree|
|499 | 01F3 | 0907 | dead tree|
|500 | 01F4 | 090B | tree|
|501 | 01F5 | 091F | tree|
|502 | 01F6 | 0923 | shrub|
|503 | 01F7 | 0924 | bush|
|504 | 01F8 | 0928 | bush|
|505 | 01F9 | 092C | bush|
|506 | 01FA | 092E | crops|
|507 | 01FB | 0977 | cavern|
|508 | 01FC | 0978 | beam|
|509 | 01FD | 097A | fence|
|510 | 01FE | 097B | pillar|
|511 | 01FF | 097F | log wall|
|512 | 0200 | 09A8 | mountains|
|513 | 0201 | 09B5 | snowcaps|
|514 | 0202 | 09B9 | mountains|
|515 | 0203 | 09DE | snowcaps|
|516 | 0204 | 09E3 | slime|
|517 | 0205 | 09E7 | vines|
|518 | 0206 | 1003 | floor|
|519 | 0207 | 1007 | floor|
|520 | 0208 | 1022 | tiles|
|521 | 0209 | 1023 | wall|
|522 | 020A | 1024 | wall|
|523 | 020B | 107F | tiles|
|524 | 020C | 108F | earth|
|525 | 020D | 1093 | earth|
|526 | 020E | 1098 | earth|
|527 | 020F | 10C1 | wall|
|528 | 0210 | 10F2 | wall|
|529 | 0211 | 10F5 | wall|
|530 | 0212 | 1100 | crenellation|
|531 | 0213 | 1101 | crenellation|
|532 | 0214 | 1107 | crenellation|
|533 | 0215 | 1160 | cave floor|
|534 | 0216 | 117F | cave floor|
|535 | 0217 | 1187 | rock|
|536 | 0218 | 120F | shore|
|537 | 0219 | 121A | sand|
|538 | 021A | 121F | sandy ground|
|539 | 021B | 122F | shore|
|540 | 021C | 1233 | sandy ground|
|541 | 021D | 1235 | wall|
|542 | 021E | 1239 | shore|
|543 | 021F | 123A | shore|
|544 | 0220 | 12FF | floor|
|545 | 0221 | 1300 | ethereal void|
|546 | 0222 | 147F | earthen wall|
|547 | 0223 | 7FFF | |
|548 | 0224 | 0000 | |
|549 | 0225 | 0000 | |


