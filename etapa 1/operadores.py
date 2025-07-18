# etapa 1 - Exercício 1
valor1 = input("Digite o primeiro valor: ")
valor2 = input("Digite o segundo valor: ") 

print("A soma dos valores é:", int(valor1) + int(valor2))
print("A subtração dos valores é:", int(valor1) - int(valor2))
print("A multiplicação dos valores é:", int(valor1) * int(valor2))
print("A divisão dos valores é:", int(valor1) / int(valor2))

# etapa 1 - Exercício 2
numero = input("Digite um número: ")

if int(numero) / 2 == 0:        
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")

# etapa 1 - Exercício 3
idade = input("Digite sua idade: ")
habilitado = input("Você está habilitado para dirigir? (sim/não): ")

if int(idade) >= 18 and habilitado == "sim":
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")