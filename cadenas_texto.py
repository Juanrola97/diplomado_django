# Ejercicios de cadenas de texto en python

"""
Función para pasando una cadena de texto en snake case,
convertirlo en camel case
"""

def obterCadenaCamelCase(cadena_texto):
    textoTrabajado = cadena_texto.split('_')
    textoCamel = textoTrabajado[0] + ''.join(texto.capitalize() for texto in textoTrabajado[1:])
    return print(textoCamel)

obterCadenaCamelCase('nombre_de_una_variable_con_snake_case')

import random

regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv',
           'patín', 'balón', 'reloj', 'bicicleta', 'anillo']
           
for sorteo in range(5):
    regalo = regalos[random.randint(0, 9)]
    print('Sorteo', sorteo + 1, ':', regalo)