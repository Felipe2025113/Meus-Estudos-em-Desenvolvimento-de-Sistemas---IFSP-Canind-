n1 = input("Digite seu nome: ")
i1 = int(input("Digite sua idade: "))

n2 = input("\nDigite seu nome: ")
i2 = int(input("Digite sua idade: "))

n3 = input("\nDigite seu nome: ")
i3 = int(input("Digite sua idade: "))

n4 = input("\nDigite seu nome: ")
i4 = int(input("Digite sua idade: "))

n5 = input("\nDigite seu nome: ")
i5 = int(input("Digite sua idade: "))

idades_t = i1 + i2 + i3 + i4 + i5

media_i = (idades_t) / 5
print(f"\n\nA média de idades é: {media_i}")

idades = [i1, i2, i3, i4, i5]
nomes = [n1, n2, n3, n4, n5]

indice_maior = idades.index(max(idades))
print(f"\nA pessoa mais velha é {nomes[indice_maior]}")

quant = 0
for i in range(0,5):
    if idades[i] < 18:
        quant += 1
        
print(f"\n{quant} pessoas são menores de idades")
