
`WeightCapacity` returns the weight capacity remaining, in "grains", of a container. It never returns a value less than zero, even for a container that has come to be overfull somehow. It returns 1 for things which have no capacity, so that may need to be checked separately. It applies equally to character inventories and to boxes, crates, etc. It does not provide any information about _equipped_ items.  


|**RDASM Name** | **DVM Machine Language** | **Arguments**|
|-|-|-|
|`System.WeightCapacity` | 0xB7 | Container|



[CategorySystemCalls](CategorySystemCalls) 
