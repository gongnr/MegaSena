# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
sena = []
while len(sena) != 6:
    x = random.randint(1, 61)
    if x not in sena:
        sena.append(x)
print(sena)