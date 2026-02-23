n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

media = (n1 + n2 + n3) / 3

if media >= 6.0:
    print ("Aprovado", media)
else:
    print ("Reprovado", media)
-----------------------------------------------------------------

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

media1 = (n1 + n2) / 2

if media1 >= 6.0:
    print ("Aprovado com média: ", media1)
else:
    print ("Reprovado com média: ", media1)
    exame = float(input("Digite a nota do exame: "))

media2 = media1 + exame

if media2 >= 5.0:
    print ("Aluno aprovado por exame com media: ", media2)
else:
    print ("Infelizmente você não atingiu a média")

---------------------------------------------------------------

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a > b:
    res = a - b
    print ("Resposta: ", res)

else:
    res = b - a
    print ("Resposta: ", res)

--------------------------------------------------------------

A = int(input("Digite o lado 1 do triangulo: "))
B = int(input("Digite o lado 2 do triangulo: "))
C = int(input("Digite o lado 3 do triangulo: "))

if A < B + C and B < A + C and C < A + B:
    if A == B or B == C or A == C:
        print ("É um triângulo isósceles")
    elif A != B and B != C:
        print ("É um triângulo escaleno")
    elif A == B and B == C:
        print ("É um triângulo equilatero")  
else:
    print ("Não é um triângulo")

---------------------------------------------------------------

A = int(input("Digite o número 1: "))
B = int(input("Digite o número 2: "))
C = int(input("Digite o número 3: "))

valores_ordenados = sorted([A, B, C])

print ("Os valores ordenado em ordem crescente são: ", 
valores_ordenados)

----------------------------------------------------------------

import math

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

delta = (B ** 2) -(4 * A * C)

raiz1 = (-B + math.sqrt(delta)) / (A * 2)
raiz2 = (-B - math.sqrt (delta)) / (A * 2)

print ("A raizes serão: ", raiz1, raiz2)


--------------------------------------------------------------


A = int(input("Digite um número: "))

valor_absoluto = abs(A)

print ("O valor absoluto do número fornecido é: ", valor_absoluto)


-----------------------------------------------------------------

A = int(input("Digite o primeiro número inteiro: "))
B = int(input("Digite o segundo número inteiro: "))
C = int(input("Digite o terceiro número inteiro: "))

if A % 2 == 0 and A % 3 == 0:
    print (A, "É divisivel por 2 e 3.")
else: 
    print (A, "Não é divisivel por 2 e 3")

if B % 2 == 0 and B % 3 == 0:
    print (B, "É divisivel por 2 e 3.")
else: 
    print (B, "Não é divisivel por 2 e 3") 

if C % 2 == 0 and C % 3 == 0:
    print (C, "É divisivel por 2 e 3.")
else: 
    print (C, "Não é divisivel por 2 e 3")
