#Metodo Index()
#Sirve para conocer el indice de un caracter, para saber que caracter hay en el indice, etc

#Esto nos devuelve el caracter que tenemos en el indice que le pasemos, si ponemos indices negativos arranca a correr de atras hacia adelante
mi_texto = "Esta es una prueba"
resultado = mi_texto[-3]
print(resultado)

#Esto nos devuelve el lugar donde se encuentra ese caracter que le dimos
mi_texto2 = "Esta es una prueba"
resultado2 = mi_texto2.index("n")
print(resultado2)

#De esta forma tambien podemos buscar palabras completas
mi_texto3 = "Esta es una prueba"
resultado3 = mi_texto3.index("prueba")
print(resultado3)

#Los otros dos valores indican desde donde y hasta donde tiene que buscar los caracteres que le especificamos
mi_texto4 = "Esta es una prueba"
resultado4 = mi_texto4.index("prueba", 5, 10)
print(resultado4)

#Extraer Substrings
#Podemos sacar porciones del texto especificado de donde y hasta con :, si ponemos otros : el siguiente valor va a indicar cada cuantos debe extraer en ese plazo de caracteres

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
#Esto busca del 0 al 10 y toma los que estan cada 2
fragmento2 = texto[0:10:2]
print(fragmento)
print(fragmento2)

#si ponemos [::-1] nos da vuelta toda la cadena
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
resultado = frase[::-1]
print(resultado)