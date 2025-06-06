from random import randint

numeros = []

for i in range(100):
    numeros.append(randint(0,10))
print(numeros)  

for i in range(len(numeros)):
    if i%2==0:#solo se muestren indices pares
        print(f"[{i}] : {numeros[i]}")

print("el numero mayor es ",max(numeros))

print("Indices donde se encuentra el numero mayor")
for i in range(len(numeros)):
    if numeros[i]==max(numeros):
        print(i, end=" .- ")

print("el numero menor es ",min(numeros))

print("Indices donde se encuentra el numero menor")
for i in range(len(numeros)):
    if numeros[i]==min(numeros):
        print(i, end=" .- ")
print(" ")        