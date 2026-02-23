import random

num = random.randint(0,100)
tenta = 10

while True:
    res = int(input("Adivinhe meu número: "))
    
    if res != num:
        tenta -= 1
        
    if tenta == 0:
        print(f"Suas tentativas acabaram! O número era {num}")
        break
    
    if res > num:
        print("\nMenos")
        print(f"tentativa: {tenta}\n")
    
    elif res < num:
        print("\nMais")
        print(f"tentativa: {tenta}\n")
        
    else:
        print(f"\n\nVocê acertou com {tenta} tentativas sobrando, o número é: {num}")
        break
