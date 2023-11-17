from typing import Tuple, Union

def busqueda_lineal(tupla: Tuple[Union[int, str]], objetivo: Union[int, str]) -> int:
  
  for index, elemento in enumerate (tupla):
    if elemento == objetivo:
      return index
  if elemento not in tupla:
    return -1

# Ejemplo de uso
datos: Tuple[int] = (5, 1, 8, 3, 2)
indice: int = busqueda_lineal(datos, 3)
print(f"El valor 3 se encontró en el índice {indice}.")

# Ejemplo de uso 1: Elemento encontrado
datos: Tuple[int] = (5, 1, 8, 3, 2)
indice: int = busqueda_lineal(datos, 3)
print(f"El valor 3 se encontró en el índice {indice}.")
# Salida esperada: "El valor 3 se encontró en el índice 3."

# Ejemplo de uso 2: Elemento no encontrado
datos: Tuple[int] = (5, 1, 8, 3, 2)
indice: int = busqueda_lineal(datos, 6)
print(f"El valor 6 se encontró en el índice {indice}.")
# Salida esperada: "El valor 6 se encontró en el índice -1."

# Ejemplo de uso 3: Búsqueda en una tupla de cadenas
nombres: Tuple[str] = ("Alice", "Bob", "Charlie", "David")
indice: int = busqueda_lineal(nombres, "Charlie")
print(f"El nombre 'Charlie' se encontró en el índice {indice}.")
# Salida esperada: "El nombre 'Charlie' se encontró en el índice 2."