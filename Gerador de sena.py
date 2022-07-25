#Script that generate a list of 6 different numbers
import random
sena = []
while len(sena) != 6:
    x = random.randint(1, 60)
    if x not in sena:
        sena.append(x)
sena.sort() 
print ("$Boa Sorte!$")       
print(sena)
