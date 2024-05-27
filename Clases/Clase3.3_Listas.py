#LISTAS
#Son secuencias ordenadas de objetos, pueden estar conformadas por todos los tipos de datos disponibles
#Deben estar entre corchetes y separados por comas, pueden anidarse, es decir listas dentro de listas
#Las listas son mutables, es decir pueden ser modificadas
#Las listas son indexadas, es decir pueden ser accedidas por medio de un indice

mi_lista = ['a','b', 'c']
otra_lista = ["hola", 55, 61.44]
print(type(mi_lista))

#Podemos preguntar el tamaño de numeros dentro de la lista
resultado = len(mi_lista)
print(resultado)

#Podemos preguntar por un objeto en especifico dentro de la lista, o un rango de items dentro de la lista
resultado2 = mi_lista[0]
print(resultado2)

resultado3 = mi_lista[0:2]
print(resultado3)

#Se pueden concatenar las dos listas sin que se fusionen para siempre, aunque metiendolo en una variable si podriamos fusionarlas y guardar todos los valores
print(mi_lista+otra_lista)

#como dice arriba llegariamos al mismo resultado
mi_lista3 = mi_lista + otra_lista
print(mi_lista3)

#Podemos modificar elementos dentro de una lista 
mi_lista3[0] = "Alfa"
print(mi_lista3)

#Podemos agregar elementos dentro de una lista al final de la cadena
mi_lista3.append("Omega")
print(mi_lista3)

#Podemos remover elementos de una lista, si lo dejamos sin parametros va a eliminar el ultimo, si se lo especificamos va directo a ese rango o caracter
mi_lista3.pop()
print(mi_lista3)

#Podemos ordenar la lista de objetos
mi_lista4 = ["a","h","m","g","c"]
mi_lista4.sort()
print(mi_lista4)

#Tambien podemos dar vuelta el orden de la lista
mi_lista4.reverse()
print(mi_lista4)