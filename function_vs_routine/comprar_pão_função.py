dinheiro = 10.00

def comprar_pão(dinheiro):
    PREÇO_DO_PÃO = 1.25
    número_de_pães = 0

    while dinheiro > PREÇO_DO_PÃO:
        número_de_pães += 1
        dinheiro -= PREÇO_DO_PÃO

    return número_de_pães, dinheiro

número_de_pães, troco = comprar_pão(dinheiro)

print(f'Tenho {número_de_pães} pães e sobraram R${troco}')
