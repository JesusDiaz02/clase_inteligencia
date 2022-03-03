'''. Dada la cantidad de alumnos de Redes, contabilidad y diseño determine el
porcentaje de alumnos de cada uno de los cursos.'''

alumnos_redes = int(input("Ingrese la cantidad de alunmos de la clase de redes: "))
alunmos_contabilidad = int(input("ingrese la cantidad de alunmos de la clase de redes: "))
alumnos_diseño = int(input("Ingrese la cantidad de alunmos de la clase de diseño: "))

cantidad_total = alumnos_redes + alunmos_contabilidad + alumnos_diseño
print(f"la cantidad de alumnos total enla institucion es de: {cantidad_total}")

porcentaje_1 = 100 *(alumnos_redes/cantidad_total)
porcentaje_2 = 100 *(alunmos_contabilidad/cantidad_total)
porcentaje_3 = 100 *(alumnos_diseño/cantidad_total)
print(f'El porcentaje de alunmos de redes es de: {porcentaje_1}%, el porcentaje es los alumnos de contabilidad es de: {porcentaje_2}%, y el porcentajer de los alumnos de diseño es de {porcentaje_3}%')
