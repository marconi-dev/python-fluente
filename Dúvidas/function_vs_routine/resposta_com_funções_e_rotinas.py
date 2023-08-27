def comprar_pão(dinheiro):
    PREÇO_DO_PÃO = 1.25
    número_de_pães = 0

    while dinheiro > PREÇO_DO_PÃO:
        número_de_pães += 1
        dinheiro -= PREÇO_DO_PÃO

    return número_de_pães, dinheiro

def tomar_café_da_manhã(dia, dinheiro):
    número_de_pães, troco = comprar_pão(dinheiro)

    print(dia)
    print(f'Fui a padaria e comprei {número_de_pães} pães')
    print(f'Sobraram R${troco}')
    print('Preparei o pão e fiz café')
    print('Lavei as vasílias depois que terminei')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


for dia in ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SÁB', 'DOM']:
    dinheiro = 10
    tomar_café_da_manhã(dia, dinheiro)
