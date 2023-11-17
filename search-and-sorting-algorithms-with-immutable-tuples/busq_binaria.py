from typing import Tuple, Union

def busqueda_binaria(tupla: Tuple[Union[int, str]], objetivo: Union[int, str]) -> int:

    izquierda, derecha = 0, len(tupla) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if tupla[medio] == objetivo:
            return medio
        elif tupla[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

# Ejemplo de uso
datos: Tuple[int] = (1, 2, 3, 5, 8)
indice: int = busqueda_binaria(datos, 5)
print(f"El valor 5 se encontró en el índice {indice}.")

# Ejemplo de uso 1: Elemento encontrado en una tupla ordenada
datos: Tuple[int] = (1, 2, 3, 5, 8)
indice: int = busqueda_binaria(datos, 5)
print(f"El valor 5 se encontró en el índice {indice}.")
# Salida esperada: "El valor 5 se encontró en el índice 3."

# Ejemplo de uso 2: Elemento no encontrado en una tupla ordenada
datos: Tuple[int] = (1, 2, 3, 5, 8)
indice: int = busqueda_binaria(datos, 6)
print(f"El valor 6 se encontró en el índice {indice}.")
# Salida esperada: "El valor 6 se encontró en el índice -1."