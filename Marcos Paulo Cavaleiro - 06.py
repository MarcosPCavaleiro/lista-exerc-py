val = float(input("Digite o valor do pão: "))

print("\nPreço do pão: R$ %.2f" % val)
print("Panificadora Pão de Ontem - Tabela de preços\n")

cont = 1
while cont <= 50:
    print( "%i - R$ %.2f" % ( cont, val * cont))
    cont += 1