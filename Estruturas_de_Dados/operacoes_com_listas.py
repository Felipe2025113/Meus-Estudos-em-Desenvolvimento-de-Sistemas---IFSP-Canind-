lista1 = []
x = int(input("Quantidade de elementos da lista 1: "))
for i in range(x):
    lista1.append(int(input(f"Elemento {i+1}: ")))
    
lista2 = []
y = int(input("Quantidade de elementos da lista 2: "))
for i in range(y):
    lista2.append(int(input(f"Elemento {i+1}: ")))
    
tamanho = min(len(lista1), len(lista2))
lista3 = []
for i in range(tamanho):
    lista3.append(lista1[i] + lista2[i])

print(f"Resultado da soma das listas: {lista3}")
