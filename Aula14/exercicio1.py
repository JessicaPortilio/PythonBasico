num_inteiro = input('Informe um número inteiro: ')

if num_inteiro.isdigit():
    num_inteiro = int(num_inteiro)

    if num_inteiro % 2 == 0:
        print(f'{num_inteiro} é par')
    else:
        print(f'{num_inteiro} é impar')
else:
    print('Isso não é um número inteiro!')


horario = input('Informe o horario (0-23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Hórario deve está entre 0 á 23')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Por favor, digite o hórario entre 0 á 23!')


nome = input('Informe seu primeiro nome: ')

tamanho = len(nome)

if tamanho <=4:
    print('Seu nome é curto!')
elif tamanho <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande!')