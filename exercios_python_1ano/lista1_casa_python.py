1) Crie um programa que permita fazer a conversão cambial entre Reais e Dólares.
Considere como taxa de câmbio US$1,00 = R$2,40. Leia um valor em Reais pelo
teclado e mostre o correspondente em Dólares.

TAXA = 2.40
valor_reais = float(input("Digite o valor em Reais (R$): "))
valor_dolares = valor_reais / TAXA
print("O valor em dólares será: US$", '%.2f' %valor_dolares)

3) Calcule quantos azulejos são necessários para azulejar uma parede. É necessário
conhecer a altura da parede (AP), a sua largura (LP), e a altura do azulejo (AA) e sua
largura (LA). Leia os dados através do teclado.

AP = float(input("Digite a altura da parede (AP): "))
LP = float(input("Digite a largura da parede (LP): "))
AA = float(input("Digite a altura do azulejo (AA): "))
LA = float(input("Digite a largura do azulejo (LA): "))

area_parede = AP * LP
area_azulejo = AA * LA

quantidade = int(area_parede / area_azulejo)

print ("A quantidade de azuleijos necessária será: ", quantidade)

4) Faça um programa que, a partir das medidas dos lados de um retângulo, lidos via
teclado, calcule a área e o perímetro deste retângulo.

altura = float(input("Digite a altura do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))

area = float(largura * altura)
perimetro = float((largura * 2) + (altura * 2))

print ("A área do retângulo é: ", area)
print ("O perímetro do retângulo é: ", perimetro)

5) A condição física de uma pessoa pode ser medida com base no cálculo do IMC,
Índice de Massa Corporal, o qual é calculado dividindo-se a massa da pessoa ( em kg)
pela altura da mesma (h em m) elevada ao quadrado (IMC= m/h²). Escreva um
programa que leia a massa e a altura de uma pessoa, calcule e mostre o IMC.

massa = float(input("Digite a massa (em Kg): "))
altura = float(input("Digite a altura (em m): "))

IMC = float(massa/altura) ** 2

print ("O IMC será: ", IMC)

6) Dado o valor do raio (r) de uma circunferência, elaborar um programa para calcular
e imprimir sua área (A) e o seu comprimento (C). A fórmula da área do círculo é A=_ r2
e do comprimento é C=2_ r.

raio = float(input("Digite o raio do circulo: "))

area = float((raio ** 2) * 3.14)
comprimento = float(raio * 2)

print ("A área será: ", area)
print ("O comprimento será: ", comprimento)

7) Elaborar um programa para calcular e exibir o volume (V) de uma esfera e a área
(A) de sua superfície, dado o valor de seu raio (R). A fórmula do volume da esfera é
V=4/3 _ R3 e da área é A=4_ R2

raio = float(input("Digite o raio: "))

volume = float((raio ** 3) * 4/3 * 3.14 )
area = float((raio ** 2) * 4 * 3.14)

print ("O volume será: ", volume)
print ("A área será: ", area)

8) Faça um programa para calcular a média final de um aluno, supondo-se que há
quatro notas bimestrais durante o ano e que esta é calculada através de uma média
aritmética simples (todos os bimestres têm o mesmo peso).

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

print ("A média será: ", media)

9) O critério de avaliação semestral de determinada escola segue a regra:
P1 – primeira avaliação do semestre.
P2 – segunda avaliação do semestre.
Ativ – nota atribuída pelas atividades realizadas no semestre.
Média = P1 x 4 + P2 x 4 + Ativ x 2
------------------------------------
 10

p1 = float(input("Digite a nota 1: "))
p2 = float(input("Digite a nota 2: "))
atv = float(input("Digite a nota 3: "))

media = ((p1 * 4) + (p2 * 4) + (atv * 2)) / 10

print ("A média será: ", media)

10) Elaborar um programa para receber valores, via teclado, nas variáveis "a" e "b".
Após isto, o programa, utilizando-se de uma 3a. variável "c", deverá trocar o conteúdo
das variáveis "a" e "b".

A = int(input("Digite um número: "))
B = int(input("Digite outro número: "))

C = A
A = B
B = C

print ("Os valores ficarão: ", A, B)

11) (DESAFIO) Idem o programa anterior, sem utilizar-se de uma 3a. variável.

A = int(input("Digite um número: "))
B = int(input("Digite outro número: "))

A,B = B,A

12) Elaborar um programa que receba, via teclado, os valores do espaço percorrido e
do tempo gasto por um veículo em movimento, para calcular e apresentar em tela sua
velocidade média.

distancia = float(input("Digite a distancia percorrida: "))
tempo = float(input("Digite o tempo gasto: "))

velocidade_media = float(distancia / tempo)

print ("A velocidade média foi de: ", velocidade_media, "Km/h")

13) Num laboratório de física, em uma experiência de Movimento Uniformemente
Variado, foram encontrados os seguintes valores: s0=2m, v0=3m/s, a=10m/s2.
Digitado o valor de t (segundos), apresentar em tela o valor de s (metros). Dada a
fórmula:
s = s0 + v0 . t + ½ . a . t2

s0 = 2.0
v0 = 3.0
a = 10.0

t = float(input("Digite o tempo t (segundos): "))

s = s0 + v0 * t + 0.5 * a * (t ** 2)

print(f"Para t = {t} s, s = {s} m")
