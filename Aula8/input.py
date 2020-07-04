"""
Entrada de dados


input sempre retorna uma string
"""

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

ano_nascimento = 2020 - int(idade)

print(f'{nome} tem {idade} anos.'
      f'{nome} nasceu em {ano_nascimento}')


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(num1 + num2)
