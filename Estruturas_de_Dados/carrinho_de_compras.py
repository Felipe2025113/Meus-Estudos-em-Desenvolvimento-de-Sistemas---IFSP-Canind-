produtos = []
preços = []
while True:
    prod = input(f"Digite o produto {len(produtos) + 1}: ")
    produtos.append(prod)
    preç = float(input(f"Digite o preço do produto {len(preços) + 1}: R$"))
    preços.append(preç)
    
    perg = input("Deseja continuar? [S/n] ")
    if perg.lower() == 'n':
        break
    
total = sum(preços)
quant_baratos = 0
for i in range(len(preços)):
    if preços[i] < 50:
        quant_baratos += 1
        
barato = min(preços)

print(f"\nO total da compra foi: R${total:.2f}")
print(f"{quant_baratos} produtos custaram menos de R$50,00")
print(f"O produto mais barato custou: R${barato:.2f}")
