
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
#exercicio de listas

frutas =  ["maca"," banana", "manga"," uva" ]

frutas[1]= "laranja"
frutas.insert(2, "onibus")
print(frutas)
print(frutas[1])
print(frutas[0])
print(frutas[2])
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
#range
for numeros in range (1,11, 3):
    print(numeros)

#nested for loop

frutas = ["maca","banana","manga"]
vegetais = ["cenoura","alface","brocolis"]

for frutas in frutas:
    for vegetal in vegetais:
        print(fruta , vegetal)
#while loop

i=1
while i <=10:
    i+1
    print(i)

#   loop com break e continue 
print("loopp com o break")
for numero in range(1,11):
   if numero>5:
      break
   print(numero)

print("loopp com o continue:")

for numero in range (1,11):

    if numero == 5:
      continue

print (numero)

#contador
FRUTAS = ["maca","banana","maca", "maca","abacate ","uva"]
contador= 0
for fruta in  FRUTAS:
    if fruta =="maca":
        contador +=1
    
    print("existem numero de macas na lista :",contador)
    #el if
    age = int (input("digite sua idade:"))
    if age < 13 :
        print("voce e uma criaca")
    elif age >= 13 and age <20:
        print("voce e um adolecente")
    else :
        print("voce e um adulto")

        #tuple
cidades = ('sao paulo', 'salvador', 'rio de janeiro')

cidade_usuario= input("adivinhe a cidade")
if cidade_usuario in cidades:
    print("a cidade esta na lista de cidade")
else:
    print("a cidade nao esta na lista de cidade")

    #dicionario
    cidades = {
        "brasil": "brasilia",
        "argentina": "buenos aires",
        "chile":"santiago",
        "autralia": "canberra",
        "canada": "ottawa"    }
    usuario_pais=input("Digite o nome do pais:")

    if usuario_pais in cidades:
        print(f"A capiatal de {usuario_pais} e {cidades[usuario_pais]}!")
    else:
        print("DESCULPE! nao temos informacoes desse pais!") 

    #sets
amigos = {"marcos","ana","sophia","arthur","amanda"}
amigos2= {"jose","arthur","ana","carol","paulo"}

result= amigos.intersection(amigos2)
print(result)

#or setes
amigos = {"marcos","ana","sophia","arthur","amanda"}
amigos2= {"jose","arthur","ana","carol","paulo"}

result= amigos.union(amigos2)
print(result)
#or setes
amigos = {"marcos","ana","sophia","arthur","amanda"}
amigos2= {"jose","arthur","ana","carol","paulo"}

result= amigos.difference(amigos2)
print(result)

# funcao


def quadrado(numero):
    return  numero **2

nuemero = int (input("digite um numero: "))
print(f"o quadrado{numero} e {quadrado(numero)}")

#funcoes 2
def i (numero, numero2):
    return numero +numero2

usuario1= int(input("digite um numero:"))
usuario2= int(input("digite outro  numero:"))

print(f"a soma dos numeros e {i(usuario1 , usuario2)}")

#or
def i (numero, numero2):
 result = numero1 + numero2
 
 print(f"a soma dos numeros e {result}")
 
 usuario1= int(input("digite um numero:"))
usuario2= int(input("digite outro  numero:"))

quadrado (usuario1 , usuario2)

#potenciacao
def potencia(base, expoente=2):
    return base ** expoente
user_number=int(input("digite o numero base: "))
user_expoente=input("digite um expoente (default 2):")

if user_expoente :
    print(F'o RESULTADO E : {potencia(user_number ,int (user_expoente))}')
    
else:
    print(f"o resultado e : {potencia(user_number)}")


    # fatorial
 
def fatorial(n):
    if n == 0 or n ==1:
     return 1
    else:
        return n * fatorial(n-1)
    user_number = int(input("digite um numero: "))
    print(f"o fatorial de {user_number}e{fatorial(user_number)}")
    # duas funcoes

    def dobrar (num):
        return num *2
    def quadrado(num):
        return dobrar (num)**2
    numero = int(input("digite um numero :"))
    print (f"o quadrado do dobrodo numero  {numero} e { quadrado(numero)}")

    

