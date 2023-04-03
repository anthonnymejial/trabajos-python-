print("fundamentos de python")
print("anthonny mejia")
print("31/03/2023")
#
letra= input ("ingrese una letra:")
if len(letra) != 1:
    print("no se puede procesar el dato. debe ingresar una sola letra.")
elif letra in "aeiouAEIOU":
    print("es vocal")
else:
    print("no es vocal")