#!/usr/bin/python3

from typing import Tuple

#tupla1 = (1, 2, 3)
tupla1: Tuple[int] = (1, 2, 3, 4, 5)

for num in tupla1:
    print(num)
    
#tupla2 = 'a', 'b', 'c'
snacks: Tuple[str] = ('doritos', 'chitos', 'tocinetas')

for comida in snacks:
    if comida != 'chitos':
        print(comida)

#tupla_vacia = ()
tupla_vacia: Tuple[int] = ()

for i in range(5):
    tupla_vacia += (i,)
    print(tupla_vacia)
    
#tupla_instancia = tuple()
tupla_instancia: Tuple[str] = tuple()

mi_string = "bonito"

for char in mi_string:
    tupla_instancia += (char,)
print(tupla_instancia)

#tupla_de_un_elemento = (42,)

mi_tupla: Tuple[int] = (42,)

for num in mi_tupla:
    print(num)    

    
