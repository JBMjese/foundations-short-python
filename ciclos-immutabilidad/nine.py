#!/usr/bin/python3

from typing import Tuple

mi_tupla: Tuple[int] = (1, 2, 3)
mi_tupla = mi_tupla[:1] + (42,) + mi_tupla[2:]
print(mi_tupla)
