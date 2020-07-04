"""
Tipos de dados
str - string - texto 'Assim' ou "Assim"
int - inteiro - números -...,5,4,3,2,1,0,1,2,3,4,5,...
float - real/ponto flutuante -...,5.0,4.0,3.0,2.0,1.0,0.0,1.0,2.0,3.0,4.0,5.0,...
bool - booleano/lógico true/false 10==10 true 10==9 false

obs: type retorna o tipo do valor digitado
"""

print("Lúíz", type("Luís"))
print(10, type(10))
print(0.2, type(0.2))
print(10==10, type(10==10))
print('10', type('10'), type(int('10')))
print(int('10')) #ele converteu uma string para inteiro
print(float(10))

print('Jessica', type('Jessica'))
print(28, type(28))
print(58.900, type(58.900))
print(28>18, type(28>18))