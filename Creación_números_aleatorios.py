import random#librería para llamar y crear números random

numeros = []#colección vacía
for i in range(10):#Ciclo para repetir 100 veces la iteraciónes
    n=random.randint(1,100)#Crea el numero entre 1 y 100
    numeros.append(n)#Guardamos en la lista el número aleatorio
cont = 0
print(numeros)#Visualizamos lista
for i in range(len(numeros)):
    if numeros[i]%2==0:
        cont+=1
print(f"cantidad de números pares : {cont}")
for i in range (len(numeros)):
    if numeros[i]%3==0:
        cont+=0
print(f"cantidad de números impares : {cont}")                