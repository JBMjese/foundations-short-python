#!/usr/bin/python3

from typing import Tuple
 
def tupla_escala(tup1, tup2, escal):
    return escal*tup1+escal*tup2

resultado: Tuple[int] = tupla_escala((1, 2, 3), (4, 5, 6), 2 )
print(resultado)
