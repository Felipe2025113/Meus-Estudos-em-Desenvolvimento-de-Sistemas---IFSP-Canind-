senha = input("Crie uma senha...\n Sua senha deve:\n .ter no mínimo 8 caracteris;\n .conter pelo menos um número;\n conter pelo menos um caracter especial(@,#,$,%).\n\n Senha:")

comp = len(senha) >= 8
num = any(char.isdigit() for char in senha)
esp = any(char in '@#$%' for char in senha)
maiu = any(char.isupper() for char in senha)

if comp and num and esp and maiu:
    print("Senha válida!")
else:
    print("Senha inválida, verifique os requisitos.")
