"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

def calcular_peso_ideal(altura, sexo):
    if sexo.lower() == 'masculino' or sexo.lower() == 'm':
        peso_ideal = (72.7 * altura) - 58
    elif sexo.lower() == 'feminino' or sexo.lower() == 'f':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        raise ValueError("Sexo inválido. Use 'masculino' ou 'feminino'.")
    return peso_ideal

try:
    altura = float(input("Digite sua altura (em metros): "))
    sexo = input("Digite seu sexo (masculino/feminino): ")

    peso = calcular_peso_ideal(altura, sexo)
    print(f"Seu peso ideal é: {peso:.2f} kg")
except ValueError as e:
    print(f"Erro: {e}")
