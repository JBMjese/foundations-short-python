#!/usr/bin/python3

from typing import Tuple

def funcion_de_ejemplo(tupla1, tupla2):
    return *tupla1, *tupla2

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla_retornada = funcion_de_ejemplo(tupla1, tupla2)
print(tupla_retornada) 
