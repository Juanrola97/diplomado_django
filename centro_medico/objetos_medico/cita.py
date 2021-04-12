class Cita():
    id = ''
    descripcion = ''
    paciente_id = ''
    doctor_id = ''
    notamedica_id = ''
    
    def __init__(self, id, descripcion, paciente_id, doctor_id, notamedica_id):     
        self.id = id
        self.descripcion = descripcion
        self.paciente_id = paciente_id
        self.doctor_id = doctor_id
        self.notamedica_id = notamedica_id
        
    def obtenerPaciente(self, pacientes):
        mi_paciente = None
        for paciente in pacientes:
            if paciente.id == self.paciente_id:
                mi_paciente = paciente
        
        return mi_paciente
    
    def obtenerDoctor(self, doctores):
        mi_doctor = None
        for doctor in doctores:
            if doctor.id == self.doctor_id:
                mi_doctor = doctor
        
        return mi_doctor
    
    def obtenerNotaMedica(self, notas_medicas):
        mi_notaMedica = None
        for nota_medica in notasmedicas:
            if nota_medica.id == self.notamedica_id:
                mi_notaMedica = nota_medica
        
        return mi_notaMedica
