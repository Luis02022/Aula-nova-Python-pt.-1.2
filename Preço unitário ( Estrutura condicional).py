import os

nome = input ("Digite o nome do produto adquirido:")
quant = int (input("Digite a quantidade de produto comprada:"))
preço = float(input("Preço unitário:"))


if quant <= 5:
  desconto = 0.2
elif quant > 5 or quant <= 10:
  desconto = 0.3
if quant > 5:
   desconto = 0.5  


total = quant * preço
totalpagar = total - (total * desconto)


print(f"Total a pagar: {totalpagar}")

