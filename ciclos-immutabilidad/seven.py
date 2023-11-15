#!/usr/bin/python3

from typing import Tuple, Union
mi_tupla: Tuple [Union[int,str]] = (1, 2, 3, 'a', 'b')
indices: Tuple [int] = (0, 4, 1, 3, 2)

for i in range(len(mi_tupla)):
    print(mi_tupla[indices[i]], end=' ')    
    