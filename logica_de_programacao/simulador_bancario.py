saldo = 1000
while True:
    escolha = input("O que deseja fazer hoje?\n 1. Ver Saldo, 2. Depositar, 3. Sacar ou 4. Sair.\n")

    if escolha == '1' or escolha.lower() == 'saldo':
        print(f"\nSeu saldo atual é: R${saldo}\n")
    
    elif escolha == '2' or escolha.lower() == 'depositar':
        deposito = float(input("\nQuanto deseja depositar: R$"))
        saldo += deposito
        print(f"\nSeu saldo atual é: R${saldo}\n")
    
    elif escolha == '3' or escolha.lower() == 'sacar':
        saque = float(input("\nQuanto deseja sacar: R$"))
        if saque >= saldo:
            print("\nVocê não pode deixar sua conta negativa ou zerada\n")
        else:
            saldo -= saque
            print(f"\nSeu saldo atual é: R${saldo}\n")

    elif escolha == '4' or escolha.lower() == 'sair':
        break
    else:
        print("\nEssa opção não existe...\n")
