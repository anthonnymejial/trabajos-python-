print("fundamentos de python")
print("anthonny mejia")
print("30/03/2023")
#10. Determinar si un año es bisiesto.
"Es divisible entre 4, pero no es divisible entre 100.Es divisible entre 400.Por ejemplo, los años 2000 y 2020 son bisiestos porque son divisibles entre 400,mientras que el año 1900 no es bisiesto porque es divisible entre 100 pero no entre 400."
año = int(input("ingrese el año"))

if año % 4 != 0: #no divisible entre 4
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
	print("Es bisiesto")