nome = ' '
soma = 0

while nome != '':
    nome = input("Digite o nome do atleta: ")
    if nome == '' or nome == ' ':
        print("Fim de execução")
    else:
        nota_1 = float(input("Digite a nota 1: "))
        nota_2 = float(input("Digite a nota 2: "))
        nota_3 = float(input("Digite a nota 3: "))
        nota_4 = float(input("Digite a nota 4: "))
        nota_5 = float(input("Digite a nota 5: "))
        
        maior_nota = 0
        menor_nota = 10

        notas = [nota_1,nota_2,nota_3,nota_4,nota_5]

        for i in notas:
            if i > maior_nota:
                maior_nota = i
            if i < menor_nota:
                menor_nota = i

        notas.remove(maior_nota)
        notas.remove(menor_nota)

        for i in notas:
            soma += i

        print("\n-> Atleta: " , nome , "\n\nPrimeiro salto: " , nota_1 , "m" "\nSegundo salto: " , nota_2 , 
          "m" "\nTerceiro salto: " , nota_3 , "m" "\nQuarto salto: " , nota_4 , "m" "\nQuinto salto: " , nota_5 , "m"
          "\n\nMelhor salto: " , maior_nota , "m" , "\nPior salto: " , menor_nota , "m" "\nMédia dos demais saltos: " , soma/3 , 
          "m\n\nResultado = " , nome , ":" , soma/3 , "m\n")

        


