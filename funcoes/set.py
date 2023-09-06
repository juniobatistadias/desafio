'''crie um programa que gera 3 listas de acordo com a necessidade logo abaixo:
lista1 = funcionarios que tem carro e trabalham a noite 
lista2 = funcionarios que te, carro e trabalham durante o dia 
lista3 = funcionarios que nao tem carro '''
funcionarios = ["Ana","Marcos","Alice","Pedro","Sophia","Bruno","Melissa"]
turno_dia =  ["Ana","Marcos","Alice","Melissa"]
turno_noite =  ["Pedro","Sophia","Bruno"]
tem_carro = ["Marcos","Alice","Bruno","Melissa"]


#LIST1

lista1= set (tem_carro). intersection(turno_noite)
print(lista1)

#lista 2

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

#lista 3
lista3= set(funcionarios). difference(tem_carro)
print(lista3)
