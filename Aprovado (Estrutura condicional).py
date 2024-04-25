#Exercício 1
import os
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))

media = nota1 + nota2 
mediatotal = media/2

os.system("clear||cls")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Nome: {nota1}")
print(f"Nome: {nota2}")
print(f"Média: {mediatotal}")

if mediatotal >= 7:
    print("Aprovado")        
else:
    print("Reprovado")    