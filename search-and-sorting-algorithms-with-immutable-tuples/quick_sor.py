from typing import Tuple, Union

def quick_sort(tupla: Tuple[Union[int, str]]) -> Tuple[Union[int, str]]:

    if len(tupla) <= 1:
        return tupla
    else:
        pivot = tupla[0]
        menores = tuple(elemento for elemento in tupla[1:] if elemento <= pivot)
        mayores = tuple(elemento for elemento in tupla[1:] if elemento > pivot)
        return quick_sort(menores) + (pivot,) + quick_sort(mayores)

# Ejemplo de uso
tupla_original = (4, 2, 8, 5, 1, 3)
tupla_ordenada = quick_sort(tupla_original)

print("Tupla original:", tupla_original)
print("Tupla ordenada:", tupla_ordenada)