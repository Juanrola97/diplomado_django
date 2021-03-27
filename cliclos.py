#Ciclos

# For

lista = ['juan','jasmin','edgar','fabian']

for nombre in lista:
    print('hola ' + nombre + ' feliz dia manito')
    

diccionario = {
    'agua': 120000,
    'luz': 50000,
    'gas': 23000,
    'internet': 90000
}

for key in diccionario.keys():
    print(key, ': ' , diccionario[key])

# Ejercicio 2 ciclo for
    
numeros = [1,10,20,15,5,2,4,5,40,2]
cs = sorted(numeros)
for numero in cs:
    print('Numero: ', numero)

numeroMayor = 0
numeroMenor = 0

for numero in numeros:
    if numeroMenor == 0:
        numeroMenor = numero
    elif numero >= numeroMayor:
        numeroMayor = numero
    elif  numero <= numeroMenor:
        numeroMenor = numero   

print('El numero mayor es: ', numeroMayor)
print('El numero menor es: ', numeroMenor)

# Ejercicio 3, pago de materias en la universidad algunas con descuento especial

valorCredito = 250000
materiasDescuento = ['programacion_1', 'lab_fisica']
valorMatricula = 0.0
descuento = 0.8

materias = {
    'programacion_1': 4,
    'matematicas_aplicada': 3,
    'humanidad': 2,
    'ingles': 1,
    'lab_fisica': 5
}

for materia, value in materias.items():
    if materia in materiasDescuento:
        valorMatricula += (value*valorCredito)*(1-descuento)
    else:
        valorMatricula += (value*valorCredito)

print('El valor de la matricula es de: ', valorMatricula)
