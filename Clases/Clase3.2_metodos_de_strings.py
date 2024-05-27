texto = "Este es el texto de Matias"
#Metodo UPPER Pasa todo a mayusculas, tambien podemos asignar un caracter en especifico

resultadoUpper = texto.upper()
print(resultadoUpper)
#Metodo LOWER() Pasa todo a minusculas

resultadoLower = texto.lower()
print(resultadoLower)
#Metodo SPLIT() separa todo en partes (listas) usa los espacios vacios para separar, dentro del () podemos especificar por que caracter debe cortar

resultadoSplit = texto.split()
print(resultadoSplit)
#Metodo JOIN() Une items usando separados mediante listas

a = "Aprender" 
b = "Python"
c = "es"
d = "Genial"
e = " ".join([a,b,c,d])
print(e)
#Metodo FIND() similar a lo de index, sirve para encontrar un sub-string debemos especificar la palabra entre los parentesis, devuelve un numero

resultadoFind = texto.find("texto")
print(resultadoFind)
#Metodo REPLACE() reemplaza un sub-string o un caracter con la palabra o caracter que le especifiquemos

resultadoReplace = texto.replace("Matias", "todos")
print(resultadoReplace)

#PROPIEDADES
#Repite palabras
nombre = "Carina"
nombre = nombre * 5
print(nombre)

#Con 3 comillas se puede escribir de la forma que le damos nosotros al texto, con saltos de linea

poema = """Mil pequenos peces blancos
como si hirviera
el color del agua"""
print(poema)

#Podemos preguntar si existe o no alguna palabra en el string (nos devuelve un booleano)
print("agua" in poema)
print("agua" not in poema)

#De esta forma preguntamos el largo en caracteres del poema
print(len(poema))