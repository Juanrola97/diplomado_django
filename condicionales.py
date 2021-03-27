# Evaluar una condicion

condicion_1 = 1>2
condicion_2 = 3>2

if condicion_1 or condicion_2:
    print("es verdad")
else:
    print("no es verdad")

if condicion_1 and condicion_2:
    print("es verdad")
else:
    print("no es verdad")


# Ejercicio 1 Condicionales

# Condiciones para ir a una discoteca edad > 18 y tener el documento de identidad a la mano

edad = 15
traeDocumento = True;

if edad >= 18 and traeDocumento == True:
    print('Puede ingresar a la discoteca')
else:
    print('No puede ingresar a la discoteca')
    