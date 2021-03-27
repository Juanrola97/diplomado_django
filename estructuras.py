# Estructuras listas, duplas, diccionarios.

# lista 
my_lista = ['yurley', 'ricardo', 'angi', 'edgar']

# Dicionarios

valores_tienda = {
    'arroz': 1000,
    'leche': 2000,
    'c_huevos': 8000,
    'huevos': 300
}

# tuplas

my_tupla = ( 1,1,1,2,2,3)

print(my_tupla.count(1))

my_tupla_2 = ({'key': 'value'}, [1,2,3], 1,2,3)

# Ejemplos 1 lista

numeros = [1,10,20,15,5,2,4,5,40,2]

# Ejemplo 2 diccionarios

materias = {
    'programacion_1': 4,
    'matematicas_aplicada': 3,
    'humanidad': 2,
    'ingles': 1,
    'lab_fisica': 5
}

# Ejemplo 3 tuplas

valores = ("Juan", True, "C#", 5, "30")
print(valores.index(True))
print(valores.index("30"))