from typing import Tuple, Union

def ordenamiento_burbuja(tupla: Tuple[Union[str, int]]) -> Tuple[Union[str, int]]:
    n = len(tupla)
    tupla_ordenada = tuple(tupla)

    for i in range(n):
        for j in range(0, n-i-1):
            if tupla_ordenada[j] > tupla_ordenada[j+1]:
                # Realiza el intercambio de elementos sin crear variables adicionales
                tupla_ordenada = tupla_ordenada[:j] + (tupla_ordenada[j+1], tupla_ordenada[j]) + tupla_ordenada[j+2:]

    return tupla_ordenada


tupla_original = (4, 2, 8, 5, 1)
tupla_ordenada = ordenamiento_burbuja(tupla_original)

print("Tupla original:", tupla_original)
print("Tupla ordenada:", tupla_ordenada)


datos: Tuple[int] = (5, 1, 8, 3, 2)
datos_ordenados: Tuple[int] = ordenamiento_burbuja(datos)

print(f"Tupla ordenada: {datos_ordenados}")

# Ejemplo de uso
datos: Tuple[int] = (5, 1, 8, 3, 2)
datos_ordenados: Tuple[int] = ordenamiento_burbuja(datos)
print(f"Tupla ordenada: {datos_ordenados}")
# Salida esperada: "Tupla ordenada: (1, 2, 3, 5, 8)"

# Ejemplo de uso 2: Ordenamiento de una tupla de cadenas
nombres: Tuple[str] = ("Alice", "Bob", "Charlie", "David")
nombres_ordenados: Tuple[str] = ordenamiento_burbuja(nombres)
print(f"Tupla ordenada: {nombres_ordenados}")
# Salida esperada: "Tupla ordenada: ('Alice', 'Bob', 'Charlie', 'David')"