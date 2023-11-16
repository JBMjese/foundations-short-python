#!/usr/bin/python3

from typing import Tuple
tupla_original = (1, 2, 3)

nueva_tupla = ()
for elemento in tupla_original:
    nueva_tupla += (elemento,)

# Verificar los IDs
print("ID de la tupla original:", id(tupla_original))
print("ID de la nueva tupla:", id(nueva_tupla))