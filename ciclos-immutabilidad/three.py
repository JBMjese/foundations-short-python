#!/usr/bin/python3

from typing import Union

numero: Union[int, float] = 0
while numero < 5:
    print(numero, "es un número par" if numero % 2 == 0 else "es un número impar")
    numero += 1
    