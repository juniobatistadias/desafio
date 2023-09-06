tem_cel = int(input("qual e a temperatura da carne?"))

if tem_cel< 48:
    print("precisa cosionhar mais! ")
elif tem_cel in range(48,53):
    print("selada")
elif tem_cel in range(54,59):
    print("Ao ponto para mal")
elif tem_cel in range(60,64):
    print("Ao ponto ")
elif tem_cel in range(65,70):
    print("Ao ponto para bem ")
elif tem_cel in range(71, 79):
    print("bem passada ")
else :
    print("queimada")