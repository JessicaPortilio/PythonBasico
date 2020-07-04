"""
Iterando strings com while em Python
strip = remove os espaços
upper = deixa as letras grandes
"""

minha_string = 'o rato roeu a roupa do rei de roma.'
tamanho_string = len(minha_string)

print(minha_string.count('p'))


c = 0
nova_string = ''

while c < tamanho_string:
    if minha_string[c] == 'r':
        nova_string += minha_string[c].upper()
    else:
        nova_string += minha_string[c]

    c+=1

print(nova_string)



x = 0
contagem_atual = 0
letra = ''
while x < tamanho_string:
    qtd_vezes_letra = minha_string.count(minha_string[x])
    if contagem_atual < qtd_vezes_letra and minha_string[x].strip():
        letra = minha_string[x]
        contagem_atual = qtd_vezes_letra
    #print(minha_string[x], conta)
    x += 1

print(letra, contagem_atual)