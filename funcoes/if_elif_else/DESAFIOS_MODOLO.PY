'''
#desafio 1
print("OLA MUNDO PYTHON")

#desafio 2
nome = "junio" 
sobrenome ="alves "
idade = 19
print("ola meu" , nome ,"e eu tenho ",idade , "anos")

#desafio numero 3

num1= 10
num2=  3.5

divisao = num1 / num2

print(divisao) 

# desafio numero 4
nome =  input("qual seu nome? " )
idade= int(input("qual sua idade? " ))

print("ola ",nome ,"voce tem", idade," anos")
#ou

print("ola {} voce tem {} anos" .format(nome,idade))
#desafio 5
num=int (input("Digite um numero:" ))
num2 = int (input("Digite um outro numero:" ))

soma = num + num2
print("o resulta do da soma e :",soma)

subtracao= num - num2 
print("o resulta do da  subtracao e :" ,subtracao)

multiplicacao = num * num2
print("o resulta do da  multiplicacao e: ",multiplicacao)

divisao=float(num / num2)
print("o resulta do da divisao e: ",divisao)

exponecial = num**num2
print("o resulta do da exponecial e: ",exponecial)
#exercicio de listas'''

'''frutas =  ["maca"," banana", "manga"," uva" ]

frutas[1]= "laranja"
frutas.insert(2, "onibus")
print(frutas)
print(frutas[1])
print(frutas[0])
print(frutas[2])'''
# desafio 6

frutas =  ["maca"," morango", " uva"," abacaxi" ]

frutas.remove(" morango")
print(frutas)
del frutas[-1]
print(frutas)

#lopps desafio

frutas =  ["maca"," morango", " uva"," abacaxi" ]

for fruta in frutas:
    print ("eu gosto de "+fruta)
    