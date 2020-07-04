"""
Formatando valores modificadores

:s - Texto (String)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(Número)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (Quantidade) (Tipo - s, d ou f)

> - Esquerdo
< - Direita
^ - Centro

"""

num_1 = 3
num_2 = 10
divisao = num_2 / num_1

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

num = 1
print(f'{num:0>9}')
nome = 'Santos'
print(f'{nome:#^8}')
nome1 = 'Jessica'
nome_formatado = '{:@>50}'.format(nome1)
print(nome_formatado)

nome2 = 'Paulo'
sobreno = 'Silva'

print('{:%^30} {:$^20}'.format(nome2, sobreno))

name = 'Larrisa Teles'
print(name.lower())  #tudo minusculo
print(name.upper())  #tudo mausculo
print(name.title())  #primeiras letras mausculas