val = float(input("Digite o valor por hora recebido: "))
hor = float(input("Digite a quantidade de horas trabalhadas: "))

sal_brut = val * hor

if sal_brut < 900 :
    desc = 0
elif sal_brut < 1500 :
    desc = 0.05
elif sal_brut < 2500 :
    desc = 0.10
else:
    desc = 0.20

ir = desc * sal_brut
inss = 0.10 * sal_brut
fgts = 0.11 * sal_brut
total_desc = ir + inss
sal_liq = sal_brut - total_desc

print("\nSalário Bruto: ( %i * %i ) : R$ %.2f" % ( val , hor , sal_brut)  ,
      "\n(-) IR (%i%%) : R$ %.2f" % ( desc*100 , ir) , 
      "\n(-) INSS (10%%) : R$ %.2f" %  inss  ,
      "\nFGTS (11%%) : R$ %.2f" % fgts ,
      "\nTotal de descontos : R$ %.2f" % total_desc ,
      "\nSalário Liquido : R$ %.2f" % sal_liq) 