
The format of sounds stored in subindex 144 identifies itself by a magic number as 'asnd'. It stores uncompressed sound in a rather odd and inefficient (in terms of disk storage) format. The name 'asnd' might refer to the "Ambrosia Sound Tool," which Delver uses. 


## Header


|**Item** | **Type** | **Value**|
|-|-|-|
|Magic Number |  char[4]  |  'asnd' (0x61736E64) |
|Duration |  uint32  |   (see below) |
|Sample Rate  |  uint16  |  Frequency in Hz |
|Flags |  uint16  |  Usually 0 |
|Sample Data  |  sint16[]  |  Duration*1024 + 512 Samples Follow|



The meaning of the flags is unknown. All of the sounds are monaural (as we would expect). A popular frequency is 22050, but various frequencies are seen in Cythera Data's sounds. 


## Sample Format

The samples are big-endian, 16-bit signed integers. There is no compression. Note that although the samples are 16 bit, the data all range from -128 to +127, i.e. 8 bit - the high bits are unused. 


## Mutations

Cythera seems to play back the sounds with minor variations (at least the duration is affected). While volume variations were expected (as the character moves relative to the sound source), it is unclear why the frequency is affected. This appears to happen to both Cythera's normal sounds and test sounds (e.g. pure sine waves) injected with [redelv](redelv). Perhaps this feature is designed to break up the monotony of the sounds, providing some variation. On the other hand, it could be a bug. Perhaps some as-yet undocumented flag value can disable it. 
