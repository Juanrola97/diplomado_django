def HelloWorld():
  print("Hello World!")

# Ejercicio 1 promedio del semestre

listaNotas = [ 4.0, 3.2, 2.5, 3.0, 4.0, 4.9, 5.0 ]
def calcularPromedioMaterias(listaNotas):
    sumNotas = 0
    numeroMaterias = len(listaNotas)
    for i in listaNotas:
        sumNotas += i;
    promedio = sumNotas/numeroMaterias
    return promedio

print('Tu promedio este semestre es de: ', calcularPromedioMaterias(listaNotas))


# Ejercicio 2

personas = [
    {
        'nombre': 'Juan',
        'edad': '23',
        'profesion': 'Ing'
    },
    {
        'nombre': 'Maria',
        'edad': '30',
        'profesion': 'Magister'
    },
    {
        'nombre': 'Pepe',
        'edad': '18',
        'profesion': 'Estudiante'
    },
]

def saludo(persona):
    nombre = persona.get('nombre')
    edad = persona.get('edad')
    profesion = persona.get('profesion')

    return 'Hola mi nombre es: {nombre}, tengo {edad} años, y soy {profesion}'.format(
        nombre=nombre,
        edad=edad,
        profesion=profesion
    )

for persona in personas:
    print(saludo(persona))