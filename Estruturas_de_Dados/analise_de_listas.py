lista = []
x = int(input("Digite o tamanho da lista: "))
for i in range(x):
    ele = int(input(f"Digite o elemento {i+1}: "))
    lista.append(ele)
    
print(f"A lista é: {lista}")
print(f"O menor elemento é o: {min(lista)}")
print(f"O maior elemento é o: {max(lista)}")
print(f"A lista invertida ficará: {lista[::-1]}")
print(f"A lista em ordem crescente ficará: {sorted(lista)}")
print(f"A lista em ordem decrescente ficará: {sorted(lista, reverse=True)}")
