acumulador = 0
print('Bem vindo a Pizzaria do Eduardo da Costa Santos ★')
while True:
    print('                 Cardápio                 ')
    print('| Código | Descrição | Pizza-M | Pizza-G |')
    print('|   21   |Napolitana | R$20,00 | R$26,00 |')
    print('|   22   |Margherita | R$20,00 | R$26,00 |')
    print('|   23   |Calabresa  | R$25,00 | R$32,50 |')
    print('|   24   |Toscana    | R$30,00 | R$39,00 |')
    print('|   25   |Portuguesa | R$30,00 | R$39,00 |')
    tam=(input('Ecolha o tamanho desejado (M/G):'))
    if tam == 'M':
        cod=(input('Digite o código:'))
        if cod == '21':
            acumulador = acumulador + 20
        elif cod == '22':
            acumulador = acumulador + 20
        elif cod == '23':
            acumulador = acumulador + 25
        elif cod == '24':
            acumulador = acumulador + 30
        elif cod == '25':
            acumulador = acumulador + 30
        else:
            print('Código inválido!')
    elif tam == 'G':
        cod = (input('Digite o código:'))
        if cod == '21':
            acumulador = acumulador + 26
        elif cod == '22':
            acumulador = acumulador + 26
        elif cod == '23':
            acumulador = acumulador + 32.50
        elif cod == '24':
            acumulador = acumulador + 39
        elif cod == '25':
            acumulador = acumulador + 39
        else:
            print('Código inválido!')
    else:
        print('Tamanho inválido!')
        continue
    continuar = input('Deseja continuar?(sim/não)')
    if continuar == 'sim':
        continue
    else:
        print('O total a pagar é : {:.2f}'.format(acumulador))
        break
