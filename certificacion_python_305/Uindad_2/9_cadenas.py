#cadenas y concarenacion (+)
cadena1='hola' 
cadena2=    "mundo"
multilinea= """esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
#cadena y repeticion
eco="ja"*8
print(eco)
#cambiar una cadena de minuscula a mayuscula
tu_nombre='jenny'
print(tu_nombre.upper())
#cambiar una cadena de mayuscula a miniscula 
print(tu_nombre.lower)
#remplazae texto en una  cadena 
frase="no me gusta programacion"
print(frase.replace("programacion","matematicas"))
#formato de concatenar cadenascon valores (F-String)
edad=16
nombre='jenny'
mensaje=f"hola, me llamo {nombre} y tengo\n{edad}años"
print(mensaje)
#contar los  caracteres de una cadena 
texto= "¡felicidades gracias por ya no seguir en el cecy!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto contiene una palabra 
oracion="aprender python es divertido"
if "python" in oracion:
    print("encontradoooo")
else:
    print("no esta")
#validar contenido de una cadena 
ncadena="a"
print(ncadena.isalpha())#True
print(ncadena.isdigit())#False