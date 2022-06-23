from re import X
from tkinter import N, S, Y
import sys

#N = int(input('Summa chisel: '))

#print ("Summa n chisel", (N*(N+1))/2)



N = int(input("Enter a natural number: "))

answer=0

for i in range(0,N+1):
	answer = answer + i;

print(answer)