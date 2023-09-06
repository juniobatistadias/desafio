primeiro = int(input("digite o primeireo numero:  "))
segundo = int(input("digite o psegundo numero:  "))
terceiro= int(input("digite oterceiro numero:  "))

maior = primeiro
if (segundo > maior):
    maior = segundo 
if(terceiro > maior):
    maior = terceiro
    print("Maior", maior)

    menor = primeiro
    if(segundo < menor):
        menor = segundo
    if (terceiro < menor ):
        menor = terceiro
        print("menor", menor )