from random import randint


for dia in ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SÁB', 'DOM']:
    dinheiro = randint(0, 10)
    número_de_pães = 0

    preço_do_pão = 1.25
    while dinheiro > preço_do_pão:
        número_de_pães += 1 
        dinheiro -= preço_do_pão
    
    print(dia)
    print(f'Fui a padaria e comprei {número_de_pães} pães')
    print(f'Sobraram R${dinheiro}')
    print('Preparei o pão e fiz café')
    print('Lavei as vasílias depois que terminei')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
