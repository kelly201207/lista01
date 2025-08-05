"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas 
e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
considere latas cheias."""

import math
area = float(input("Informe o tamanho da área a ser pintada (em metros quadrados): "))
cobertura_por_litro = 6
litros_necessarios = area / cobertura_por_litro
litros_necessarios *= 1.1
litros_necessarios = math.ceil(litros_necessarios)
litros_lata = 18
preco_lata = 80.00

litros_galao = 3.6
preco_galao = 25.00

latas_necessarias = math.ceil(litros_necessarios / litros_lata)
preco_latas = latas_necessarias * preco_lata

galoes_necessarios = math.ceil(litros_necessarios / litros_galao)
preco_galoes = galoes_necessarios * preco_galao

latas_mistas = math.floor(litros_necessarios / litros_lata)
litros_restantes = litros_necessarios - (latas_mistas * litros_lata)
galoes_mistos = math.ceil(litros_restantes / litros_galao)
preco_misto = (latas_mistas * preco_lata) + (galoes_mistos * preco_galao)

print("\n--- Opções de Compra ---")
print(f"1. Apenas latas de 18L: {latas_necessarias} lata(s) - Preço: R$ {preco_latas:.2f}")
print(f"2. Apenas galões de 3,6L: {galoes_necessarios} galão(ões) - Preço: R$ {preco_galoes:.2f}")
print(f"3. Mistura: {latas_mistas} lata(s) e {galoes_mistos} galão(ões) - Preço: R$ {preco_misto:.2f}")
