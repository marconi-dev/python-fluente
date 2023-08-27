dinheiro = 10.00
número_de_pães = 0

preço_do_pão = 1.25
while dinheiro > preço_do_pão:
    número_de_pães += 1 
    dinheiro -= preço_do_pão

print(f'Tenho {número_de_pães} pães!')
print(f'E tenho R${dinheiro} sobrando!')
