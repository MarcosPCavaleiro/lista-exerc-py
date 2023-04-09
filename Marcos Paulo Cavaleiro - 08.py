cod = 1
votos_1 = 0
votos_2 = 0
votos_3 = 0
votos_4 = 0
votos_5 = 0
votos_6 = 0

while cod != 0:
    cod = int(input("Digite o código do candidato: (1 - José / 2 - João / 3 - Carlos / 4 - Edna / 5 - Nulo / 6 - Branco): "))
    if cod == 1:
        votos_1 += 1
    if cod == 2:
        votos_2 += 1
    if cod == 3:
        votos_3 += 1
    if cod == 4:
        votos_4 += 1
    if cod == 5:
        votos_5 += 1
    if cod == 6:
        votos_6 += 1
    if cod != 0 :
        print("Obrigado por votar! ")
    else:
        print("Votação finalizada.")

soma_votos = votos_1 + votos_2 + votos_3 + votos_4 + votos_5 + votos_6
porc_nulo = (votos_5/soma_votos) * 100
porc_bran = (votos_6/soma_votos) * 100

print("Votos: \nJosé: " , votos_1 , "\nJoão: " , votos_2 , "\nCarlos: " , votos_3 , "\nEdna: " , votos_4 ,
      "\nNulos: " , votos_5 , "\nBrancos: " , votos_6 , "\nPorcentagem de votos nulos em relação ao total: " , porc_nulo , 
      "% \nPorcentagem de votos em branco em relação ao total: " , porc_bran , "%")
