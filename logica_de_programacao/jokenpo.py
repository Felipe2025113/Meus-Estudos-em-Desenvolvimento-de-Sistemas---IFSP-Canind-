import random
jogo = ['pedra', 'papel', 'tesoura']

while True:
    esc_comp = random.choice(jogo)
    esc_usu = input("Digite a sua escolha (ou 'sair'): ").lower()

    if esc_usu == 'sair':
        break

    print(f"\nEu escolhi: {esc_comp}\nVocê escolheu: {esc_usu}\n")

    if (esc_comp == 'tesoura' and esc_usu == 'pedra') or \
       (esc_comp == 'papel' and esc_usu == 'tesoura') or \
       (esc_comp == 'pedra' and esc_usu == 'papel'):
        print("Você Ganhou\n")
    
    elif esc_comp == esc_usu:
        print("Empate\n")
    
    else:
        print("Eu Ganhei\n")
