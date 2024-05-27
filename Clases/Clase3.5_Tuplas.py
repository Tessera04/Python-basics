#TUPLAS
#Son como las listas, pero inmutables, una vez que entra un objeto no se puede modificar
#ocupan menos espacio de memoria por lo que son mas rapidas
#Al no poder ser modificadas, son a prueba de daños

mi_tuple = (1,2,3,4)
print(type(mi_tuple))

#Pueden tener todo tipo de valores y de objetos

mi_tuple2 = (1,'Hola',[1,2,3])
print(mi_tuple2)

#Podemos transformar tuples en listas

mi_tuple = list(mi_tuple)
print(type(mi_tuple))

#Tambien se puede hacer una lista a taple
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

#Se pueden usar distintos metodos
#Podemos consultar la longitud
t = (1,2,3,4,1)
print(len(t))

#Permite contar la cantidad de apariciones en el tuple
print(t.count(1))

#Tambien podemos consultar el caracter
print(t.index(1))