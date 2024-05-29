#Input para ingresar texto, input para 3 letras a eleccion. Debe devolver cuantas veces aparece cada letra,
#cuantas palabras hay en total en todo el texto.
#debe devolver cual es la primer y ultima letra
#Deve devolver las palabras en order inverso y encontrar si esta la palabra python

#Variables que toman los datos
texto = input("Ingrese su texto: ")
letras = []

texto = texto.lower()

letras.append(input("Ingrese la primer letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercer letra: ").lower())

print("\n")
#Funcion para ver cuantas veces aparece cada letra
print("CANTIDAD DE VECES QUE SE REPITE UNA LETRA")
cantidadLetras1 = texto.count(letras[0])
cantidadLetras2 = texto.count(letras[1])
cantidadLetras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} repetida {cantidadLetras1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetida {cantidadLetras2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetida {cantidadLetras3} veces")

#Metodo para separar texto en lista de distintos strings y contar sus palabras
print("\n")
print("CANTIDAD DE PALABRAS")
texto_separado = texto.split()
print(f"Tu texto tiene {len(texto_separado)} palabras")

#Devuelve palabras en orden inverso
print("\n")
print("ORDEN INVERSO")
inverso = texto[::-1]
print(f"Tu texto al reves: {inverso}")

#Metodo para devolver primer y ultima letra
print("\n")
print("PRIMER Y ULTIMA LETRA")
primerLetra = texto[0]
ultimaLetra = texto[-1]

print(f"La primer letra de tu texto es la letra: {primerLetra}")
print(f"La ultima letra de tu texto es la letra: {ultimaLetra}")

#Encontrar si esta la palabra Python
print("\n")
print("ESTA LA PALABRA PYTHON?")
encontrada = "python" in texto
dic = {True:"Si", False:"No"}
print(f"La palabra 'Python' {dic[encontrada]} se encuentra en el texto")