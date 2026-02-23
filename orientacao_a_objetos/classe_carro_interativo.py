class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo

    def acelerar(self):
        print("O carro está acelerando... Vrummm!")

cor_digitada = input("Qual a cor do carro? ")
modelo_digitado = input("Qual o modelo do carro? ")

meu_carro = Carro(cor_digitada, modelo_digitado)

print(f"\nSucesso! Você criou um {meu_carro.modelo} na cor {meu_carro.cor}!")
meu_carro.acelerar()
