#Variables

nombre = "Matias"
print(nombre)

nombre = "Eluney"
print(nombre)

edad = 30
print(edad)

edad2 = 15
print(edad + edad2)

#nombreInput = input("Dime tu nombre: ")
#print("Tu nombre es " + nombreInput)

#INTEGERS Y FLOATS

mi_numero = 4
print(mi_numero)

print(type(mi_numero))

mi_numero_decimal = 5.8
print(mi_numero_decimal)
print(type(mi_numero_decimal))

#todo lo que ingrese como input queda como string

num1 = 7.5
num2 = 2.5

print(type(num1 + num2))

#CONVERSIONES automaticas

numero1 = 20
numero2 = 30.5

print(type(numero1))

numero1 = numero2 + numero1

print(type(numero1))
print(type(numero2))

#CONVERSIONES manuales

num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1)
print(num2)
print(type(num2))

edad_persona = input("Dime tu edad: ")
edad_persona = int(edad_persona)
nueva_edad = 1 + edad_persona
print(nueva_edad)