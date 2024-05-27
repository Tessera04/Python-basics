x = 6
y = 4
z = 7

print(f"{x} mas {y} es igual a {x+y}")

print(f"{x} menos {y} es igual a {x-y}")

print(f"{x} por {y} es igual a {x*y}")

print(f"{x} dividido {y} es igual a {x/y}")

#Division al piso, te da el numero aproximado mas bajo p.e(7.5 te va a dar 7)
print(f"{z} dividido al piso de {y} es igual a {z//y}")

#Modulo te devuelve el RESTO de la division, no te devuelve el resultado
#Se puede utilizar para detectar si un numero es par o no, si lo hacemos modulo de 2 y nos devuelve 0 es par
print(f"{z} modulo de {y} es igual a {z%y}")

#Potencia
print(f"{x} elevado a la {y} es igual a {x**y}")

#Raiz Cuadrada
#Todo numero a la 0.5 nos va a devolver su raiz cuadrada
print(f"La raiz cuadrada de {y} es {y**0.5}")

#REDONDEO
#Round funciona con 2 valores, el numero y la cantidad de digitos a los que debe redondear round(num, digitos)
print(90/7)
print(round(90/7))

resultado = 90/7
redondeo = round(resultado)

print(redondeo)

#Como podemos ver a round le damos un numero con muchas comas y le pedimos que redondee solo al num con 2 decimales
valor = round(95.666666666666666666, 2)
print(valor)
valor2 = round(95.666666666666666666, 3)
print(valor2)

valor3 = round(95.666666666666666666)
print(type(valor3))

num10 = round(13/2,0)
print(num10)