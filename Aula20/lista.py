"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#         0    1         2    3    4    5
lista = ['A', 'Bacana', 'C', 'D', 'E', 10.5]
#      -  6    5         4    3    2    1

string ='ABacanaCDE'
print(string[1])  # suporta somente um valor

print(lista[5])  # suporta varios valores

print(lista[0:3])

print(lista[1:4])
print(lista[::2])

lista1 = [1,2,3]
lista2= [4,5,6]
# lista3 = lista1 + lista2

lista2.insert(0, 'Banana') # insere no inicio da lista
lista2.append('b') # insere valor no final da lista
lista1.extend(lista2)   # Junta as listas
lista2.pop() # remove o ultimo da lista



print(lista1)
print(lista2)
# print(lista3)

l = [1,2,3,4,5,6,7,8,9]
del(l[3:5])
print(l)
print(max(l))
print((min(l)))


criando_lista_atraves_de_uma_funcao = list(range(1,10))

print(criando_lista_atraves_de_uma_funcao)

for valor in criando_lista_atraves_de_uma_funcao:
    print(valor)

