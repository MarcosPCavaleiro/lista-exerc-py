base = float(input("Digite a base para calcular: "))
expo = float(input("Digite o expoente para calcular: "))
expo_inicial = expo
resu = 1

while expo > 0:
    resu = resu * base
    expo = expo - 1
    
print("A resposta de " , base , " elevado a " , expo_inicial , " é " , resu)

