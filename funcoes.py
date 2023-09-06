'''crie um programa que calcule a quatidade de tinta necessaria para pintar
uma parede.Ousuario deverfa fornecer as seguintes informacoes: redimento, altura e largura .
o programa deve mostrar na tela a mensagem "voce necessita zx latas de tinta'''
rendimento = int(input("qual e oo rendimento da lata "))
altura= int(input("qual e a altura da parede ?"))
largura = int(input("qual e largura da parede?"))

def calculo_tinta():
    area = altura * largura
    total= area / rendimento
    print(f'voce precisa de {total}latas de tintas')
  
  
    calculo_tinta()