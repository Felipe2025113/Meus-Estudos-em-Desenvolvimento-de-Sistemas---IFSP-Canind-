class Carro:
	def __init__(self, cor, modelo):
		self.cor = cor
		self.modelo = modelo

	def acelerar(self):
		print("O carro está acelerando!")
		
# Criando um objeto com valores fixos
meu_carro = Carro("Vermelho", "Fusca")
print(f"Modelo: {meu_carro.modelo}")
print(f"Cor: {meu_carro.cor}")
meu_carro.acelerar()
