1) Elaborar um programa que escreva em tela os números de 1 a 20, utilizando o
comando while( ).

numero = 1
while numero <= 20:
    print(numero)
    numero += 1

-------------------------------------------------------------------

2) Elaborar um programa que escreva em tela todos os números pares existentes
entre 20 e 1, utilizando o comando while( ).

x = 0
while x < 21:
    if x % 2 != 0:
        x += 1
        continue
    print(x)
    x += 1

-------------------------------------------------------------------

3) Elaborar um programa que escreva em tela os números de 1 a 20, informando
quando eles são pares e quando são ímpares, utilizando o comando while( )

x = 0
while x <= 20:
    if x % 2 != 0:
        print(f"{x} - É ímpar")
    else:
        print(f"{x} - É par")
    x += 1

------------------------------------------------------------------

4) Elaborar um programa que escreva em tela os números de 20 a 1, utilizando o
comando for( ).

for x in range(1,21):
    print(x)

-------------------------------------------------------------------

5) Elaborar um programa que escreva em tela todos os números impares existentes
entre 1 e 20, utilizando o comando for( ).

for x in range(1,21):
    if x % 2 == 0:
        continue
    print(x)

-----------------------------------------------------------------------

6) Elaborar um programa que escreva em tela os números de 20 a 1, informando
quando eles são pares e quando são ímpares, utilizando o comando for( ).

for x in range(1,21):
    if x % 2 == 0:
        print(f"{x} - É par")
    else:
        print(f"{x} - É impar")

-----------------------------------------------------------------------

7) Elaborar um programa que escreva em tela os números de 1 a 20, utilizando o
comando do-while( ).

numero = 1
while True:
    print(numero)
    numero += 1
    if numero > 20:
        break

----------------------------------------------------------------------

8) Elaborar um programa que escreva em tela todos os números pares existentes
entre 1 e 20, utilizando o comando do-while( ).

numero = 1
while True:
    if numero % 2 == 0:
        print(numero)
    numero += 1
    if numero > 20:
        break

----------------------------------------------------------------------

9) Elaborar um programa que escreva em tela os números de 1 a 20, informando
quando eles são pares e quando são ímpares, utilizando o comando do-while( ).

numero = 1
while True:
    if numero % 2 == 0:
        print(f"{numero} - PAR")
    else:
        print(f"{numero} - ÍMPAR")
    
    numero += 1
    if numero > 20:  # Condição de saída no final
        break

---------------------------------------------------------------------

10) Elaborar um programa que seja uma “Calculadora”, onde o usuário deverá digitar
uma das seguintes teclas: ‘+’, ‘-‘, ‘*’, ‘/’ ou ‘S’. - Caso escolha ‘S’, para sair, o programa
deverá ser encerrado; - Caso escolha ‘+’, ‘-‘, ‘*’ ou ‘/’, como operações aritméticas, o
programa
deverá solicitar a digitação de dois números quaisquer (número a e número b), um por
vez, realizar a respectiva operação aritmética (soma, subtração, multiplicação ou
divisão) entre os respectivos números (a e b, nessa ordem) e então apresentar o seu
resultado. Após isto, deverá voltar à etapa inicial de digitação das teclas ‘+’, ‘-‘, ‘*’, ‘/’
ou ‘S’ e repetir este item até a digitação da tecla ‘S’.

for i in range(10):
    tecla = input("Digite a operação (+, -, *, /) ou 'S' para sair: ")
    
    if tecla.upper() == 'S':
        print("Programa encerrado!")
        break
    
    else:
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        
        if tecla == '+': res = a + b
        elif tecla == '-': res = a - b
        elif tecla == '*': res = a * b
        elif tecla == '/': res = a / b
        
        print(f"Resultado: {res}")

--------------------------------------------------------

11) Escreva um programa para mostrar na tela os resultados de uma tabuada de um
número qualquer fornecido via teclado.
Exemplo:
Digite o número para a tabuada: 5 <Enter>
Tabuada do 5:
5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

# Recebe o número do usuário
numero = int(input("Digite o número para a tabuada: "))

print(f"\nTabuada do {numero}:")

# Gera a tabuada de 0 a 10
for i in range(11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
