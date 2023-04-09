cod = 1
soma_alt = 0
soma_pes = 0
cont = 0
mais_alt = 0
mais_bai = 5
mais_mag = 1000
mais_gor = 0
res_alt = ""
res_bai = ""
res_mag = ""
res_gor = ""

while cod != 0 :
    cod = int(input("Digite o código: "))
    if cod != 0:
        alt = float(input("Digite a altura: "))
        pes = float(input("Digite o peso: "))
        soma_alt = soma_alt + alt
        soma_pes = soma_pes + pes
        cont = cont + 1
        if alt > mais_alt:
            res_alt = "Código =  %i Altura = %.2fm  Peso = %.2fkg" % (cod , alt , pes)
            mais_alt = alt
        if alt <  mais_bai:
            res_bai = "Código =  %i Altura = %.2fm  Peso = %.2fkg" % (cod , alt , pes)
            mais_bai = alt
        if pes > mais_gor:
            res_gor = "Código =  %i Altura = %.2fm  Peso = %.2fkg" % (cod , alt , pes) 
            mais_gor = pes
        if pes < mais_mag:
            res_mag = "Código =  %i Altura = %.2fm  Peso = %.2fkg" % (cod , alt , pes) 
            mais_mag = pes

    
media_alt = soma_alt/cont
media_pes = soma_pes/cont

print("\nResumo : \nMais alto: " , res_alt , "\nMais baixo: " , res_bai , "\nMais gordo: " , res_gor , "\nMais magro: " , res_mag ,"\nMédia de peso: " , media_pes , "\nMédia de altura: " , media_alt)
