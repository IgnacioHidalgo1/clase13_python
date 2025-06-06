import random#librería para llamar y crear números random

numeros = []#colección vacía
for i in range(100):#Ciclo para repetir 100 veces la iteraciónes
    n=random.randint(1,100)#Guardamos en la lista el número aleatorio
    numeros.append(n)

print(numeros)#Visualizamos lista