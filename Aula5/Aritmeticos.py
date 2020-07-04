"""
+
-
*
/
// divisão inteira
** 3² isso que ele faz
% resto mod
() altera a presedência
1-( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

2- ** - Depois vem a exponenciação

3- * / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

4- +  - - Por fim, soma e subtração
"""

print("Multiplicação: 10 *10 =", (10*10))
print("Adição: 10 + 10 =", (10+10))
print("Substração: 10 - 10 =", (10-10))
print("Divisão: 10 / 10 =", (10/10))
print("Divisão: 10 // 10 =", (10//10))
print("Potência: 10 ** 2 =", (10**2))
print("(100+2)-4*2/2 =", ((100+2)-4*2/2))
print("Resto da divisão: 10 % 3 =", (10%3))

#Multiplicar um inteiro com uma string
print(10 * "Jessica\n")
print("Jessica" + " " + "Portilio", "Tem", str(28), "anos")