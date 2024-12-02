escolha=input("Que alimento a Madame ou Senhor está procurando?")

ingredientes = [
    {"nome":"Abacate","Carboidrato":"9 g","Proteína":"2 g","Gorduras Totais":"15 g","Calorias":"160 g"},
    {"nome":"Soja","Carboidrato":"30 g","Proteína":"36 g","Goduras Totais":"20 g","Calorias":"446 g"},
    {"nome":"Alface","Carboidrato":"2,9 g","Proteína":"1,4 g","Goduras Totais":"0,2 g","Calorias":"15 g"},
    {"nome":"Morango","Carboidrato":"8 g","Proteína":"0,7 g","Goduras Totais":"0,3 g","Calorias":"33 g"},
    {"nome":"Uva","Carboidrato":"17 g","Proteína":"0,6 g","Goduras Totais":"0,4 g","Calorias":"67 g"},
    {"nome":"Kiwi","Carboidrato":"15 g","Proteína":"1,1 g","Goduras Totais":"0,5 g","Calorias":"61 g"},
    {"nome":"Batata","Carboidrato":"20 g","Proteína":"1,6 g","Goduras Totais":"0,1 g","Calorias":"86 g"},
    {"Nome":None}

]

if  escolha=="abacate":
    print(ingredientes[0])

elif escolha=="soja":
    print(ingredientes[1])

elif escolha=="alface":
    print(ingredientes[2])

elif escolha=="morango":
    print(ingredientes[3])

elif escolha=="uva":
    print(ingredientes[4])

elif escolha=="kiwi":
    print(ingredientes[5])

elif escolha=="batata":
    print(ingredientes[6])

else:
    print("nn encotrado!")
