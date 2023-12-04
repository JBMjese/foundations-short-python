#!/usr/bin/python3

from typing import Tuple

def tupla_ordenada(tupla1):
    tupla_sin_dupli = ()
    for elemento in tupla1:
            tupla_sin_dupli += (elemento, )
    tupla_ordenada = sorted(tupla_sin_dupli)         
    return tupla_ordenada
    
result = tupla_ordenada((1, 4, 2, 3, 5))  
print(result)
