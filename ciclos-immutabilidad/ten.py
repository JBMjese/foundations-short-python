#!/usr/bin/python3

from typing import Tuple

partes = ((), (1, 2, 3), (1,), (1, 2), (1, 3), (2,), (2, 3), (3,))
nueva_tupla = tuple (elemento for tupla in partes for elemento in tupla if tupla)
print (nueva_tupla)
