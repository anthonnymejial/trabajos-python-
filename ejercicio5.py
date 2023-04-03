print("fundamentos de python")
print("anthonny mejia")
print("30/03/2023")
#
salario=float(input("ingresa su sueldo"))
impuesto=0
if salario< 10000:
    print("el impuesto es de5%")
    impuesto=0.05
elif salario>= 10000 and salario <20000:
    print("el impuesto es del 15%")
    impuesto=0.15
elif salario>=20000 and salario <35000:
    print ("el impuesto es del 20%")
    impuesto=0.20
elif salario>=35000 and salario <60000:
    print ("el impuesto es del 30%")
    impuesto=0.30
elif salario>=60000:
    print ("el impuesto es del 45%")
    impuesto=0.45
else:
    print("el salario ingresado es incorrecto")
total=salario*impuesto
print("el valor al impuesto a pagar es",total)
print("el salario a recibir es ",salario-total)

