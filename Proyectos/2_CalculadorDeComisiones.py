#Debe preguntar nombre y cuanto vendio, debemos almacenarlos en variables como strings
#calcular el 13% del num del usuario, no debe tener mas de 2 decimales

nombre = input("Dime tu nombre: ")
total_ventas = input("Dime tu total de ventas: ")

total_ventas = int(total_ventas)
total_ventas = round(total_ventas*13/100, 2)

print(f"{nombre} el total de comisiones de tus ventas es de {total_ventas}")