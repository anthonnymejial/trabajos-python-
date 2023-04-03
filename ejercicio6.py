print("fundamentos de python")
print("anthonny mejia")
print("31/03/2023")
#
valor1=int(input("valor1:"))
valor2=int(input("valor2:"))
valor3=valor1+valor2
valor4=valor1-valor2
valor5=valor1*valor2
print ("presione 1 para sumar")
print ("presione 2 para resta")
print ("presione 3 para multiplicar")
comando=int(input("digite opsion"))
if comando==1:
 print("la suma es:",valor3)
if comando==2:
 print("la resta es:",valor4)
if comando==3:
 print("la muiltiplicacion es:",valor5)
else:
 print("comando no encontrado")
