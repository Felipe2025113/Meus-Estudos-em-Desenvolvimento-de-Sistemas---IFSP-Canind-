Questão1
tempo = int(input("Digite o tempo gasto na viagem em horas:"))
velocidade_media = int(input("Digite a velocidade média da viagem em km/h:"))

distancia = tempo * velocidade_media
litros_usados = distancia / 12

print ("Velocidade média: ", velocidade_media, "km/h")
print ("Tempo gasto na viagem: ", tempo, "horas")
print ("Distância percorrida: ", distancia, "km")
print ("Quantidade de litros usada na viagem: ", '%.2f' %litros_usados, "litros")

Questão2
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit:"))
celsius = ((fahrenheit - 32) * 5 ) / 9

print ("Temperatura me celsius:", celsius, "°C")

Questão3
import math
raio = float(input("Digite o raio da lata de óleo em cm: "))
altura = float(input("Digite a altura da lata de óleo em cm: "))

volume = math.pi * raio ** 2 * altura

print ("Volume da lata de óleo: ", volume, "cm")

Questão4
a = input("Digite o valor de A: ")
b = input("Digite o valor de B: ")

a,b = b,a

print ("O valor de A ápos a troca: ", a)
print ("O valor de B ápos a troca: ", b)

Questão5
numero = int(input("Digite um número inteiro: "))
quadrado = numero ** 2

print ("O quadrado de ", numero, "é:", quadrado)

Questão6
valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa de juros (em %): "))
tempo = float(input("Digite o tempo de atraso (em meses): "))

prestacao = valor + (valor*(taxa/100) * tempo)
print ("Valor da prestação em atraso: ", prestacao)

Questão7
nr_coelhos = int(input("Digite o número de coelhos: "))
custo = (nr_coelhos * 0,70) / 1 + 10

print ("Custo de criação de coelhos: ", '%.2f' %custo)
