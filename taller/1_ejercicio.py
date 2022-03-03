'''1. Una Institución educativa ha recibido una donación especial que será
repartida entre las carreras de Telecomunicaciones, Sistemas,
Administración y Contabilidad de la siguiente forma:
a. Telecomunicaciones 10% del valor dado a sistemas
b. Sistemas: 25% del valor dado a Administración
c. Administración: 35% del valor de la donación
d. Contabilidad: lo que resta de la donación'''


donaciones = int(input("ingrese el valor de la donacion: "))

administracion = donaciones * 0.35
sistemas = administracion * 0.25
telecomunicaciones = sistemas * 0.1
contabilidad = donaciones * 0.65
print(f'la donacion realiza fue de {donaciones}, el valor dado a administracion fue de {administracion} el valor dado al departamento de sistemas fue de {sistemas}, el valor dado al departamento de telecominicaciones fue de {telecomunicaciones} y el valor otorgado a contabilidad fue de {contabilidad}')

