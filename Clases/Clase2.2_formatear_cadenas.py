x = 10
y = 4

#Hay 3 versiones para formatear el texto, vamos de la mas rustica a la mas moderna
print("Mis numeros son: " + str(x) + " y " + str(y))

#De esta forma se ponen los valores que van dentro de los corchetes ordenados de forma lineal, llegariamos al mismo resultado
print("Mis numeros son: {} y {}".format(x,y))

#La siguiente forma es la mas actual y se parece mucho a lo que encontramos en JS o PHP
print(f"Mis numeros son: {x} y {y}")

#Otro ejemplo
matricula = "MEG410"
color = "Negro"

print(f"El auto es {color} y su matricula es {matricula}")

#Tambien se pueden realizar operaciones dentro del format
print("La suma de {} y {} es igual a {}".format(x,y,x+y))