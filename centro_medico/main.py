'''
2) Implementar la logica de una institucion de servicios medicos.

    Doctores
    Pacientes
    Citas
    Notas medicas
    Horarios de citas (*opcional)

estas entidades deben ser implementadas mediante objetos. el programa debe permitir las siguientes funciones:

1) un doctor debe poder ver las citas que tienen asignadas (un doctor puede atender varias citas al dia pero debe al menos dar una y no debe tener mas de 10 horas de trabajo)

2) cada cita debe tener un paciente y un doctor

3) un paciente puede tener inscritas en muchas citas

4) las notas medicas son ingresadas por el doctor que atiende la cita medica con en paciente tiene asignado

5) los paciente deben poder ver un historial de notas medicas escritas por cada doctor

6) {OPCIONAL} - los horarios son definidos de maximo 12 horas diarias en horario de oficina, un paciente no puede estar en dos citas con el mismo horario, un doctor no puede atender dos citas medicas que sean vistas el mismo tiempo

'''

from objetos_medico.cita import Cita
from objetos_medico.doctor import Doctor
from objetos_medico.paciente import Paciente
from objetos_medico.nota_medica import NotaMedica

def rellenarDatos():
    
    doctores = []
    pacientes = []
    citas = []
    notas_medicas = []
    
    # --- DOCTORES ---
    doctor_1 = Doctor(
        id = 1,
        nombre = 'Dr Sebastian', 
        documento = 123
    )

    doctor_2 = Doctor(
        id = 2,
        nombre = 'Dr Lopez',
        documento = 124
         
    )

    doctor_3 = Doctor(
        id = 3,
        nombre = 'Dra Hernandez',
        documento = 125
    )
    
    doctores.append(doctor_1)
    doctores.append(doctor_2)
    doctores.append(doctor_3)
    
     # --- PACIENTES ---
    paciente_1 = Paciente(
        id = 1,
        nombre = 'Jaime Garcia', 
        documento = 123
    )

    paciente_2 = Paciente(
        id = 2,
        nombre = 'Pedro Felicia',
        documento = 124
         
    )

    paciente_3 = Paciente(
        id = 3,
        nombre = 'Carlos Jose',
        documento = 125
    )
    
    pacientes.append(paciente_1)
    pacientes.append(paciente_2)
    pacientes.append(paciente_3)
    
    # --- NOTAS MEDICAS ---
    nota_medica_1 = NotaMedica(
        id = 1,
        descripcion = 'Persona problemas Respiratorios', 
        diagnostico = 'Enfermedad de los pulmones nivel 1'
    )

    nota_medica_2 = NotaMedica(
        id = 2,
        descripcion = 'Dearrea y mareos continuos', 
        diagnostico = 'Covid - 19'
         
    )

    nota_medica_3 = NotaMedica(
        id = 3,
        descripcion = 'Molestia en las articulaciones', 
        diagnostico = 'Osteoartritis'
    )
    
    notas_medicas.append(nota_medica_1)
    notas_medicas.append(nota_medica_2)
    notas_medicas.append(nota_medica_3)
    
    # --- CITAS ---
    cita_1 = Cita(
        id = 1,
        descripcion = 'Persona problemas Respiratorios', 
        paciente_id = paciente_1.id,
        doctor_id = doctor_1.id,
        notamedica_id = nota_medica_1.id
    )

    cita_2 = Cita(
        id = 2,
        descripcion = 'Dearrea y mareos continuos', 
        paciente_id = paciente_2.id,
        doctor_id = doctor_2.id,
        notamedica_id = nota_medica_2.id
         
    )

    cita_3 = Cita(
        id = 3,
        descripcion = 'Molestia en las articulaciones', 
        paciente_id = paciente_3.id,
        doctor_id = doctor_3.id,
        notamedica_id = nota_medica_3.id
    )
    
    citas.append(cita_1)
    citas.append(cita_2)
    citas.append(cita_3)
    
    
    return {
        'doctores': doctores,
        'pacientes': pacientes,
        'citas': citas,
        'notas_medicas': notas_medicas,
    }
    
# Rellenar Datos
data = rellenarDatos()
print('---- MENU --- ')
opcion = 1 
index_paciente = 1
index_doctor = 1
index_cita = 1
index_notaMedica = 1

while opcion != '0':
    print('selecciona una opcion: ')

    print('''
    1) Agregar Doctor
    2) Agregar Paciente
    8) Imprimir Doctores
    9) Imprimir Pacientes
    0) Salir

    ''')
    try:
        opcion = input('ingresa el dato: ')
        if opcion == '1':
            # Agregar doctor
            
            nombre = input('ingresa el nombre del doctor: ')
            doctor = Doctor(index_doctor, nombre)
            data.get('doctores').append(doctor)
    
            index_doctor += 1
        
        if opcion == '2':
            # Agregar paciente
            
            nombre = input('ingresa el nombre del paciente: ')
            paciente = Profesor(index_paciente, nombre)
            data.get('pacientes').append(paciente)
    
            index_paciente += 1

        if opcion == '8':
            # Imprimir Doctores 
            print('-- Doctores --')
            for doctor in data.get('doctores'):
                print(doctor.nombre)
                print('')
                print('')

        if opcion == '9':
            # Imprimir Pacientes 
            print('-- Pacientes --')
            for paciente in data.get('pacientes'):
                print(paciente.nombre)
                print('')
                print('')

        else:
            print('Ingrese una opcion valida')
    except:
        pass
print('-- se acabo de ejecutar todo el codigo--')