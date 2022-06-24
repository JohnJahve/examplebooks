from re import X
from tkinter import N, S, Y

X = float(input('Pervyi vznos: '))

print ("Vsego", "Dohod za 1 god", X+0.4*100)
print ("Vsego", "Dohod za 2 god", (X+0.4*100)+0.4*100)
print ("Vsego", "Dohod za 3 god", ((X+0.4*100)+0.4*100)+0.4*100)
