#SETS
#Solo admiten elementos unicos, no se repiten python los descarta
#No se pueden modificar, son inmutables
#No estan indexados, no pueden reorganizarse aunque los veamos en cierto orden

mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

#Como podemos ver python elimina los repetidos automaticamente
mi_set = set([1,2,3,4,5,1,1,1,1,1,2,2,2,2,2,2])
print(mi_set)

#Podemos ver el tamaño
print(len(mi_set))

#Tambien se pueden buscar valores especificos
print(2 in mi_set)

#Podemos juntar los distintos sets y python va a eliminar elementos repetidos para crear un nuevo set con los valores unicos
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

#Añade el elemento que le digamos al set
s1.add(6)
print(s1)

#Elimina un elemento que le digamos al set
s1.remove(2)
print(s1)

#Elimina un objeto del set con la condicion de encontrarlo, si no lo encuentra no hace nada
s1.discard(5)
print(s1)

#Elimina un elemento aleatorio, ya que estos se diferencian por no tener index
s1.pop()
print(s1)

#Vacia nuestro set
s1.clear()
print(s1)