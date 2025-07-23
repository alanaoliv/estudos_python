# etapa 1 - Exercício 1
for i in range(1, 11):
    print("Número:", i)

# etapa 1 - Exercício 2
numero = input("Digite um número: ")
tab = 1 

while tab <= 10:
    resultado = int(numero) * tab
    print( numero, "x", tab, "=", resultado)
    tab += 1

# etapa 1 - Exercício 3
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
for nome in nomes:
    print("Nome:", nome) 