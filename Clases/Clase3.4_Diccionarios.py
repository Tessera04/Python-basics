#DICCIONARIOS
#Estan formados por pares, una clave y un valor asocioado a esa clave
#Se escribe entre llaves{} y estan separados por comas, la clave:valor va a estar separada por un :
#Ejemplo: {"clave1":"valor1","clave2":"valor2"}
#Se puede acceder a los valores de un diccionario mediante la clave, se escribe entre corchetes[] y se escribe la
#clave entre comillas
#Ejemplo: diccionario["clave1"]

diccionario = {'c1':'valor1','c2':'valor2','c3':'valor3','c4':'valor4','c5':'valor5'}
print(type(diccionario))

#Aca podemos ver el diccionario, los valores pueden repetirse pero las claves no
print(diccionario)

#Podemos guardar valores en variables, ponemos la clave y nos devuelve el valor asociado a esa clave
resultado = diccionario["c1"]
print(resultado)

#Ejemplo
cliente = {'nombre':'Juan','apellido':'Perez','Peso':92, "talla":1.70}
consulta = cliente['Peso']
print(consulta)

#Dentro de los diccionarios se pueden meter todo tipo de datos, listas, otros diccionarios, etc
dic = {"c1":['a','b','c'], 'c2':['d','e','f'], 'c3':88, 'c4':[1,2,3]}
print(dic)
#Podemos usar metodos y entrar en los datos de las listas dentro de las listas
print(dic['c1'])
print(dic['c4'][1])
print(dic['c2'][1].upper())

#Agregar elementos a un diccionario
dic2 = {1:'a', 2:'b'}
print(dic2)
#Lo agregamos
dic2[3] = 'c'
print(dic2)

#Tambien podemos modificar valores dentro de un diccionario
dic[2] = 'B'
print(dic2)

#Podemos filtrar para ver todos los valores o todas las claves o todo junto (separados por parentesis)

print(dic2.keys())
print(dic2.values())
print(dic2.items())