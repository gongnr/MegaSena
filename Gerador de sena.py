# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import random
sena = []
while len(sena) != 6:
    x = random.randint(1, 60)
    if x not in sena:
        sena.append(x)
print(sena)
