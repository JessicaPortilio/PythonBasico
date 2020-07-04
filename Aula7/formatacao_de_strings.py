nome = "Jessica"
idade = 28
altura = 1.60
e_maior = idade > 18
data_1 = True
peso = 58.9
imc = peso / altura ** 2
ano = 2020
ano_nascimento = ano - idade

print(nome, "tem: ", idade, "anos de idade e seu imc é", imc)
print(f'{nome} tem {idade} anos de idade e seu imc é, {imc:.2f}')
print('{} tem {} anos de idade e seu imc e {:.2f}'.format(nome, idade, imc))

"""
Criar variáveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa
Criar variável com o ano atual (int)
Obter o ano de nascimento da pessoa (baseado na idae e no ano atual)
Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibir um texto com todos os valores na tela usando F-Strings (com chaves)
"""

print(f'{nome} tem {idade} anos de idade, nasceu no ano {ano} e seu imc é {imc:.2f}, '
      f'tem {peso:.2f} de peso e {altura:.2f} de altura')

