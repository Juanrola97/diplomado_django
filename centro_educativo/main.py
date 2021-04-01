import tkinter as tk


class Profesor():
    def __init__(self,id, doc_identidad, nombre, apellido, correo, lista_materias ):
        self.id = id
        self.doc_identidad = doc_identidad
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.lista_materias = lista_materias

class Estudiante():
     def __init__(self, nombre, idProfesor):
        self.nombre = nombre
        self.id_profesor = idProfesor

profesor_1 = Profesor(
    id = 1,
    doc_identidad = 123456789,
    nombre = 'Juan Sebastian',
    apellido = 'Rodriguez',
    correo = 'jsebastian@institucion.edu.co',
    lista_materias = ['Matematicas', 'Religion']
    )
profesor_2 = Profesor(
    id = 2,
    doc_identidad = 123456789,
    nombre = 'Juan Sebastian',
    apellido = 'Rodriguez',
    correo = 'jsebastian@institucion.edu.co',
    lista_materias = ['Matematicas', 'Religion']
    )
profesor_3 = Profesor(
    id = 3,
    doc_identidad = 123456789,
    nombre = 'Juan Sebastian',
    apellido = 'Rodriguez',
    correo = 'jsebastian@institucion.edu.co',
    lista_materias = ['Matematicas', 'Religion']
    )
