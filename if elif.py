# calculo o imc - inde de massa corporal
'''qual e sua altura em cm:
qual e seu peso em kg: '''

#menor que 18,5 magreza
#entre 18,5 e 24,9 normal
#entre 25,0 e 29,90 sobrepeso
#entre 30,0 e 39,9 obsidade
#maior que 40,0 obsidade morbida


altura= float(input("qual e sua altura em cm?  " ))
peso= float(input("qual e seu peso em kg? " ))

imc = peso/(altura/100)**2
print (imc)
if imc < 18.5 :
    print ("magreza")
elif imc >= 18.5 and imc < 24.9:
    print("normal")
elif imc  >= 25.0 and imc < 29.9:
 print("sobrepeso")

else :
 print("obsidade")

