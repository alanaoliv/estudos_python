# etapa 1 - Exercício 1
numero = input("Digite um número: ") 

if int(numero) > 0:
    print("O número", numero, "é positivo.")
elif int(numero) < 0:
    print("O número", numero, "é negativo.")
else:
    print("O número é zero.")

# etapa 1 - Exercício 2
nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Parabéns, você foi aprovado!")
elif nota >= 5:
    print("Você está de recuperação.")
else:
    print("Você foi reprovado.")

# etapa 1 - Exercício 3
idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você é uma criança.")
elif idade >= 0 and idade <= 17:
    print("Você é um adolescente.")
elif idade >= 0 and idade <= 59:
    print("Você é um adulto.")
elif idade >= 0 and idade >= 60:
    print("Você é um idoso.")
else:
    print("Idade inválida.")
