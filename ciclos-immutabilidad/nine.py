#!/usr/bin/python3

mi_tupla = (1, 2, 3)
mi_lista = list(mi_tupla)    # Convertir la tupla en una lista
mi_lista[1] = 42            # Modificar el elemento en la lista
mi_tupla = tuple(mi_lista)    # Convertir la lista de vuelta en una tupla