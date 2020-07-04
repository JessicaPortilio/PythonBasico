"""
Manipulando Strings
* String indices
* Fatiamento de strings [inicio:fim:passo}
*função built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""
#positivos [012345678]
texto = 'Python S2'
#negativo -[987654321]
print(len(texto))
print(texto[2])
print(texto[-7])

ulr = 'www.google.com.br/'
print(ulr[:-1])

nova_string = texto[2:6]
nova = texto[0:6:2]
print(nova_string)
print(nova)