def soma(a, b):
    resultado = []
    for i in range(len(a)):
        resultado.append(a[i] + b[i])
    return resultado
    
lista1 = []
x = int(input("Digite a quantidade de elementos da lista 1: "))
for i in range(x):
    num1 = int(input(f"Digite o elemento {i+1}: "))
    lista1.append(num1)
    
lista2 = []
y = int(input("Digite a quantidade de elementos da lista 2: "))
for i in range(y):
    num2 = int(input(f"Digite o elemento {i+1}: "))
    lista2.append(num2)
    
if len(lista1) == len(lista2):
    print(f"A soma das listas será: {soma(lista1, lista2)}")
else:
    print("Erro: As listas precisam ter o mesmo tamanho para somar elemento por elemento.")
