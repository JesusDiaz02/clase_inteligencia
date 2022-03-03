'''Un vendedor recibe un sueldo base más un 15% extra por comisión de sus
ventas efectuadas en el mes. El vendedor desea saber cuanto dinero en
total obtendrá por las ventas que realiza en el mes. Desarrolle un programa
en Python que permita mostrar el valor ganado por comisión y el valor total
a pagar al vendedor.''' 

sueldo_vendedor = float(input("Ingrese el sueldo base del vendedor: "))

venta = float(input("Ingrese el valor total de las ventas: "))
comision_ventas = venta * 0.15
print(f'El valor ganado por las comisiones es de {comision_ventas} y el valor total a pagar es de {sueldo_vendedor + comision_ventas}')