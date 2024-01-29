# Created by MI EQUIPO at 29/01/2024
  # language: es
Característica: Calificar trabajo final de verificación y validación
  Como profesor
  quiero calificar el trabajo final de mis estudiantes estrictamente
  para aprobar a los estudiantes que demestre conocimiento de la materia.

  Escenario: Profesor califica personalmente
    Dado que un alumno ha entregado su trabajo final a tiempo
    Cuando asigno una calificación sobre 10 basado en una rúbrica
    Entonces apruebo al estudiante si la calificación es mayor o igual a 7
    Pero si no cumple ese mínimo, repruebo al estudiante

    # Enter steps here