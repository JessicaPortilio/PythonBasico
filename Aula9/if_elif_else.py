"""
Condições IF, ELIF e ELSE
Operadores Relacionais
Operadores Lógicos
and = &&
or = ||
not = !
in = Está em..
not in = Não estiver dentro...
== > < <= !=
"""

if False:
    print('Verddadeiro')
elif True:
    print('Agora é verdadeiro')
elif False:
    print('Agora não é mais verdadeiro')
else:
    print('Não é verdadeiro')


nome = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))

menor_idade = 18
muito_velhor = 60

if idade >= menor_idade and idade <= muito_velhor:
    print(f'{nome} parabéns você tem idade para isso.')
else:
    print(f'{nome} você não pode')

if 's' in nome:
    print('Existe a letra "s"')
else:
    print('Não existe a letra "s" ')

if 's' not in nome:
    print('Existe a letra "s"')
else:
    print('Não existe a letra "s" ')