"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""
texto = 'Python'
nova_string = ''



for letra in texto:
    print(letra)

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

for n, letra in enumerate(texto):
    print(n, letra)

for numero in range(10):
    print(numero)

for a in range(0, 10, 2):  #inicia com zero, vai até 10, pulando de dois em dois
    print(a)

for b in range(20, 9, -1):
    print(b)

for c in range(100):
    if c % 8 == 0:
        print(c)