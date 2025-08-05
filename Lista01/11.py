"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:"""

inteiro1 = int(input("Digite o primeiro número inteiro: "))
inteiro2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número real: "))
resultado1 = (2 * inteiro1) * (inteiro2 / 2)
resultado2 = (3 * inteiro1) + real
resultado3 = real ** 3
print(f"\nResultado 1 (dobro do 1º * metade do 2º): {resultado1}")
print(f"Resultado 2 (triplo do 1º + número real): {resultado2}")
print(f"Resultado 3 (número real ao cubo): {resultado3:.2f}")
