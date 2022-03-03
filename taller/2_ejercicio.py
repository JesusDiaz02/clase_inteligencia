'''Haga un programa en Python que permita ingresar el dinero invertido por
tres personas para formar una empresa. Cada una de ellas invierte una
cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
al total de la inversión.'''




primer_inversor = float(input("Ingrese la cantidad invertidad por el primer inversor: "))
segundo_inversor = float(input("Ingrese la cantidad invertidad por el segundo inversor: "))
tercer_inversor = float(input("Ingrese la cantidad invertidad por el tercer inversor: "))

total_capital = primer_inversor + segundo_inversor + tercer_inversor
porcentaje_uno = 100 *(primer_inversor/total_capital)
porcentaje_dos = 100 *(segundo_inversor/total_capital)
porcentaje_tres = 100 *(tercer_inversor/total_capital)
print(total_capital)
print(f'El porcentaje de la inversion de la primera persona fue de:{porcentaje_uno}% ')
print(f'El porcentaje de la inversion de la segunda persona fue de:{porcentaje_dos}% ')
print(f'El porcentaje de la inversion de la tercera persona fue de:{porcentaje_tres}% ')
