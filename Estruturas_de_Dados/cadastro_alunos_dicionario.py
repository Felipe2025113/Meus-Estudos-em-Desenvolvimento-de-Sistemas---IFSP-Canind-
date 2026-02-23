meu_dicionario = {}
while True:
    nome = input("Digite o nome do aluno: ")
    nota = input("Digite a nota do aluno: ")
    meu_dicionario[nome] = nota
    
    esc = input("Deseja continuar? [S/n] ").lower()
    if esc == 'n':
        break
    elif esc != 's':
        print("Opção inválida, encerrando cadastro.")
        break
        
print("\nRelatório de Notas:")
print(meu_dicionario)
