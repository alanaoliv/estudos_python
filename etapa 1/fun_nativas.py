# etapa 1 - Exercício 1
palavra = input("Digite uma palavra: ")

print("A palavra", palavra, "tem", len(palavra), "letras.")

# etapa 1 - Exercício 2
numeros = list(int(input("Digite um número: ")) for i in range(5))

print("A soma dos números é:", sum(numeros))
print("O maior número é:", max(numeros))

# etapa 1 - Exercício 2 - opção alternativa
numero = input("Digite cinco números: ").split()
valor = [int(num) for num in numero]

print("A soma dos números é:", sum(valor))
print("O maior número é:", max(valor))

# etapa 1 - Exercício 3
materia = "Biologia"
trimestre = 1
nota = 8.5

print(type(materia))
print(type(trimestre))
print(type(nota))