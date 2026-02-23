def conversao(c):
    f = c * 1.8 + 32
    return f
    
c = float(input("Digite a temperatura em °C: "))

print(f"A conversão em Fahrenheit será: {conversao(c)}")
