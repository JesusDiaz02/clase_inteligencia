'''Un alumno desea saber cuál será su calificación final en la materia de
fundamentos de programación. Dicha calificación se compone de los
siguientes porcentajes: 50% del promedio de sus tres talleres, 30% de la
calificación de un examen en clase y 20% de la calificación de un proyecto
final.'''

taller1 = float(input("ingrese la nota del primer taller: "))
taller2 = float(input("Ingrese la nota del segundo taller: "))
taller3 = float(input("ingrese la nota del tercer taller: "))
calificacion_examen = float(input("Ingrese la calificacion del examen: "))
calificacion_proyecto = float(input("Ingrese la calificacion del proyecto: "))
total_notas_taller = (taller1 + taller2 + taller3)/3

nota_final = (total_notas_taller * 0.50 ) + (calificacion_examen * 0.30)+(calificacion_proyecto * 0.20)
print(f'la nota filan del estudiante es de: {nota_final}')

