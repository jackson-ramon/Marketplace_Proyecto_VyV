import random
from datetime import datetime
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.actividad_final = Actividad
        self.tarea = True
        self.esta_aprobado = False

    def entregar_trabajo_final(self,trabajo):
        self.actividad_final = trabajo

class Actividad:
    def __init__(self, nombre, fecha_entrega):
        self.nombre = nombre
        self.calificacion = 0
        self.fecha_entrega = fecha_entrega
        self.fecha_limite = datetime(2024, 1, 31)


    def esta_entregado_a_tiempo(self):

        return self.fecha_entrega <= self.fecha_limite

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.trabajos_recibidos = []

    def recibir_trabajo(self, actividad):
        self.trabajos_recibidos.append(actividad)

    def abrir_trabajo(self, actividad):
        #se abre el trabajo
        pass

    def calificar_trabajo(self, actividad):
        calificacion_criterio_profesor = random.uniform(0, 10)
        actividad.calificacion = calificacion_criterio_profesor

    def revisar_calificacion(self, alumno):
        alumno.esta_aprobado = alumno.actividad_final.calificacion >= 7
