'''
1) Implementar la logica de una institucion educativa.
Profesores
Estudiantes
Materias
Notas
Horarios de Clase (*opcional)
estas entidades deben ser implementadas mediante objetos. el programa debe permitir las siguientes funciones:
1) un profesor debe poder ver las materias que tienen asignadas (un profesor puede dictar varias clases pero debe al menos dar una)
2) Una materia puede ser dictada por varios profesores y pueden estar inscritos varios estudiantes
3) un estudiante puede estar inscritos en muchas materias
4) las notas son ingresadas por el profesor que dicta la materia en la clase donde el estudiante este incrito
5) los estudiantes deben poder ver que notas tienen y ver un promedio por materia y general en todas sus materias
6) {OPCIONAL} - los horarios son definidos de maximo 6 horas diarias, un estudiante no puede estar en dos materias con el mismo horario, un profesor no puede dictar dos materias que sean vistas el mismo
'''

from objetos.nota import Nota, Matricula
from objetos.materia import Materia
from objetos.estudiante import Estudiante
from objetos.profesor import Profesor

def rellenarDatos():
    
    profesores = []
    estudiantes = []
    materias = []
    notas = []
    matriculas = []

    # --- PROFESORES ---
    profesor_1 = Profesor(
        id = 1,
        nombre = 'sebastian henao', 
    )

    profesor_2 = Profesor(
        id = 2,
        nombre = 'luis lopez', 
    )

    profesor_3 = Profesor(
        id = 3,
        nombre = 'daniel vargas', 
    )

    profesores.append(profesor_1)
    profesores.append(profesor_2)
    profesores.append(profesor_3)


    # --- ESTUDIANTE ---
    estudiante_1 = Estudiante(
        id = 1,
        nombre = 'Wilson sanmiguel', 
    )

    estudiante_2 = Estudiante(
        id = 2,
        nombre = 'Juan giovanny', 
    )


    estudiantes.append(estudiante_1)
    estudiantes.append(estudiante_2)

    # --- MATERIAS ---
    materia_1 = Materia(
        id = 1,
        nombre ='Programacion'
    )

    materia_2 = Materia(
        id = 2,
        nombre ='Python'
    )

    materia_3 = Materia(
        id = 3,
        nombre = 'Html'
    )

    materia_4 = Materia(
        id = 4,
        nombre = 'Web'
    )

    materias.append(materia_1)
    materias.append(materia_2)
    materias.append(materia_3)
    materias.append(materia_4)

    matricula_1 = Matricula(
        id=1,
        estudiante_id=estudiante_1.id,
        materia_id=materia_1.id,
        profesor_id=profesor_1.id,
    )
    
    matricula_2 = Matricula(
        id=2,
        estudiante_id=estudiante_1.id,
        materia_id=materia_2.id,
        profesor_id=profesor_1.id,
    )

    matricula_3 = Matricula(
        id=3,
        estudiante_id=estudiante_1.id,
        materia_id=materia_4.id,
        profesor_id=profesor_2.id,
    )
    
    matricula_4 = Matricula(
        id=4,
        estudiante_id=estudiante_2.id,
        materia_id=materia_1.id,
        profesor_id=profesor_1.id,
    )
    
    matricula_5 = Matricula(
        id=5,
        estudiante_id=estudiante_2.id,
        materia_id=materia_3.id,
        profesor_id=profesor_3.id,
    )

    matricula_6 = Matricula(
        id=6,
        estudiante_id=estudiante_2.id,
        materia_id=materia_4.id,
        profesor_id=profesor_2.id,
    )
    
    matriculas.append(matricula_1)
    matriculas.append(matricula_2)
    matriculas.append(matricula_3)
    matriculas.append(matricula_4)
    matriculas.append(matricula_5)
    matriculas.append(matricula_6)

    nota_1 = Nota(
        matricula_id=matricula_1.id,
        valor=5
    )

    nota_2 = Nota(
        matricula_id=matricula_1.id,
        valor=4
    )

    nota_3 = Nota(
        matricula_id=matricula_1.id,
        valor=3
    )

    notas.append(nota_1)
    notas.append(nota_2)
    notas.append(nota_3)

    return {
        'profesores': profesores,
        'estudiantes': estudiantes,
        'materias': materias,
        'notas': notas,
        'matriculas': matriculas
    }

'''
# Rellenar datos
data = rellenarDatos()

# Imprimir valores 
for key, value in data.items():
    print('\n lista de: {}'.format(key))
    if key in ['profesores', 'estudiantes', 'materias']:
        for val in value:
            print(val.nombre)


matriculas = data.get('matriculas')
notas = data.get('notas')
estudiantes = data.get('estudiantes')
materias = data.get('materias')

for matricula in matriculas:
    print('estudiante: ', matricula.obtenerEstudiante(estudiantes).nombre)
    print('materia: ', matricula.obtenerMateria(materias).nombre)
    print('promedio: ', matricula.obtenerPromedio(notas))
    print('')

'''
print('---- MENU --- ')
# Rellenar datos
data = rellenarDatos()
a = 1 
index_materia = 1
index_profesor = 1
index_nota = 1

while a != '0':
    print('selecciona una opcion: ')

    print('''
    1) Agregar Materia
    2) Agregar Profesor
    3) Ver notas estudiante
    8) Imprimir Profesores
    9) Imprimir Materias
    0) Salir

    ''')
    try:
        a = input('ingresa el dato: ')
        if a == '1':
            # Agregar la materia
            
            nombre = input('ingresa el nombre de la materia: ')
            materia = Materia(index_materia, nombre)
            data.get('materias').append(materia)
    
            index_materia += 1
        
        if a == '2':
            # Agregar profesor
            
            nombre = input('ingresa el nombre del profesor: ')
            profesor = Profesor(index_profesor, nombre)
            data.get('profesores').append(profesor)
    
            index_materia += 1

        if a == '3':
            # Ver notas estudiante

            id_matricula = input('Ingresa id de matricula')
            contador = 1
            for nota in data.get('notas'):
                if nota.matricula_id == int(id_matricula):
                    print(nota.valor)
                    contador += 1

        if a == '8':
            # Imprimir profesor 
            print('-- Profesores --')
            for profesor in data.get('profesores'):
                print(profesor.nombre)
                print('')
                print('')

        if a == '9':
            # Imprimir materias 
            print('-- Materias --')
            for materia in data.get('materias'):
                print(materia.nombre)
                print('')
                print('')

        else:
            print('Ingrese una opcion valida')
    except:
        pass
print('-- se acabo de ejecutar todo el codigo--')