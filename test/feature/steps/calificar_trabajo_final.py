from behave import *
from modelos.modelos_calificaciones import *
from datetime import datetime

use_step_matcher("re")


@step("que un alumno ha entregado su trabajo final a tiempo")
def step_impl(context):
    context.alumno = Alumno("nombre")
    fecha_entrega = datetime(2024, 1, 30)
    context.actividad_final = Actividad("Proyecto final", fecha_entrega)
    context.alumno.entregar_trabajo_final(context.actividad_final)
    assert(context.actividad_final.esta_entregado_a_tiempo() == True)


@step("asigno una calificación sobre 10 basado en una rúbrica")
def step_impl(context):
    context.profesor = Profesor("nombre")
    context.profesor.recibir_trabajo(context.alumno.actividad_final)
    context.profesor.abrir_trabajo(context.alumno.actividad_final)
    context.profesor.calificar_trabajo(context.alumno.actividad_final)

    assert (0 < context.alumno.actividad_final.calificacion < 10)

@step("apruebo al estudiante si la calificación es mayor o igual a 7")
def step_impl(context):
    context.profesor.revisar_calificacion(context.alumno)
    print(context.alumno.actividad_final.calificacion)
    assert (context.alumno.esta_aprobado)


@step("si no cumple ese mínimo, repruebo al estudiante")
def step_impl(context):
    context.profesor.revisar_calificacion(context.alumno)
    print(context.alumno.actividad_final.calificacion)
    assert not (context.alumno.esta_aprobado)