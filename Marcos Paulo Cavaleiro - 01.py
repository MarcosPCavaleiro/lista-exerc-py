lit = float(input("Digite o número de litros: "))
tipo = input("Digite o tipo de combústivel: ").upper()

valor_alc = 1.90
valor_gas = 2.50

if lit < 0:
    print("Apenas valores positivos são aceitos.")
else:
    if tipo == 'A':
        if lit <= 20:
            valor_alc = valor_alc - 0.03 * valor_alc
        else:
            valor_alc = valor_alc - 0.05 * valor_alc
    elif tipo == 'G':

        if lit <= 20:
            valor_gas = valor_gas - 0.04 * valor_gas
        else:
            valor_gas = valor_gas - 0.06 * valor_gas
    else:
        print("Tipo de combustível inválido.")

    if tipo == 'A':
        print("O valor a ser pago é de R$ %.2f " % ((lit * valor_alc)))
    elif tipo == 'G':
        print("O valor a ser pago é de R$ %.2f " % ((lit * valor_gas)))
    else:
        print("Valor indisponível.")
