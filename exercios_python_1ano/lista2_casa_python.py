1) Elaborar um programa em que informe se o número digitado pelo usuário é par ou
impar

A = int(input("Digite um número: "))

if A % 2 == 0:
    print ("É par")
else:
    print ("É impar")

--------------------------------------------------------------------
2) Digitado um número inteiro entre 0 e 100, informar o quanto ele está distante de um
determinado número chave, carregado no próprio programa. Ex.: Número chave=20,
número digitado=15, resposta=5. Número chave=17, número digitado=20, resposta=3
(Obs.: a resposta deverá ser sempre um número positivo).

chave = int(input("Defina um número chave: "))
num = int(input("Escolha um número entre 0 a 100: "))

if num > chave:
    res = num - chave
    print ("A resposta é: ", res)

else: 
    res = chave - num
    print ("A resposta é: ", res)

---------------------------------------------------------------------
3) Uma Universidade tem problemas com arredondamento das médias dos alunos,
pois cada professor estipula um critério de arredondamento. Devemos elaborar um
programa, em Linguagem C++, para a secretaria da Universidade, resolvendo esse
problema. O programa deve solicitar uma nota e fazer o devido arredondamento.
Regras:
Notas que ultrapassem 0,5 de resto serão arredondas para CIMA.
Ex: 4,6 –>5,0
Notas que abaixo ou igual a 0,5 de resto serão arredondas para BAIXO.
Ex: 4,5 –> 4,0

nota = float(input("Digite a nota: "))

parte_inteira = int(nota)
parte_decimal = nota - parte_inteira

if parte_decimal > 0.5:
    resultado = parte_inteira + 1
else:
    resultado = parte_inteira

print ("Nota arredondada: ", resultado)

------------------------------------------------------------------------
4) Faça um programa que leia 3 números e exiba:
a) O maior número;
b) O menor número;
c) O número do meio

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

meio = (n1 + n2 + n3) - maior - menor

print("Maior número: ",  maior)
print("Menor número: ", menor)
print("Número do meio: ", meio)

------------------------------------------------------------------------
5)- Faça o programa que calcule o salário líquido dos funcionários de uma empresa. O
salário líquido é composto por descontos e adicionais, seguindo as seguintes regras:
Descontos:
Salário bruto < 800,00 – não realizar nenhum desconto;
800,00 <= Salário bruto <=1600,00 – descontar 8% de Imposto de Renda e 5
% de encargos.
>1600,00 – descontar 15% de Imposto de Renda e 7% de encargos.
Adicionais:
Caso o funcionário tenha trabalhado mais de 160 horas no mês, divida o seu salário
bruto por 160 (representa horas trabalhadas) e calcule 50% de adicional nas horas
que excederam a 160.
O usuário deverá digitar o salário bruto e o número de horas trabalhadas no mês de
cada funcionário, e deverá receber como resultado o salário líquido. O usuário poderá 

salario_bruto = float(input("Digite o salário bruto: "))
horas_trabalhadas = float(input("Digite as horas trabalhadas: "))

if salario_bruto < 800:
    desconto_ir = 0
    desconto_encargos = 0
elif salario_bruto <= 1600:
    desconto_ir = salario_bruto * 0.08
    desconto_encargos = salario_bruto * 0.05
else:
    desconto_ir = salario_bruto * 0.15
    desconto_encargos = salario_bruto * 0.07

if horas_trabalhadas > 160:
    valor_hora = salario_bruto / 160
    horas_extras = horas_trabalhadas - 160
    adicional = valor_hora * horas_extras * 0.5
else:
    adicional = 0

salario_liquido = salario_bruto - desconto_ir - desconto_encargos + adicional

print("Salário líquido: ", salario_liquido, "R$")

----------------------------------------------------------------------------
6)- Faça um programa que receba como entrada o mês (de 1 a 12) e retorne o nome
do respectivo mês

mes = int(input("Digite um número de 1 à 12: "))

if mes == 1:
    print ("Mês 1 é janeiro")
elif mes == 2:
    print ("Mês 2 é fevereiro")
elif mes == 3:
    print ("Mês 3 é março")
elif mes == 4:
    print ("Mês 4 é maio")
elif mes == 5:
    print ("Mês 5 é abril")
elif mes == 6:
    print ("Mês 6 é junho")
elif mes == 7:
    print ("Mês 7 é julho")
elif mes == 8:
    print ("Mês 8 é agosto")
elif mes == 9:
    print ("Mês 9 é setembro")
elif mes == 10:
    print ("Mês 10 é outubro")
elif mes == 11:
    print ("Mês 11 é novembro")
elif mes == 12:
    print ("Mês 12 é dezembro")

------------------------------------------------------------------
7)- Entrar um código de acesso a um curso. Se o código for 1, 2,3,4 e 5 exibir na tela
Engenharia, Edificações, Sistemas Elétricos, Turismo e Análise de Sistemas
respectivamente; caso contrário exibir que o código é inválido.

num = int(input("Escolha um número: "))

if num == 1:
    print ("Engenharia")
elif num == 2:
    print ("Edificações")
elif num == 3:
    print ("Sistemas elétricos")
elif num == 4:
    print ("Turismo")
elif num == 5:
    print ("Análise de sistemas")
else: 
    print ("Número imválido")
