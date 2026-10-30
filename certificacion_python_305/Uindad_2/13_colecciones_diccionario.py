#creando un diccionario en python 
persona={
    "nombbre":"Jenny",
    "edad":16,
    "profesion":"Ingenieria",
    "estuadiante":True
}         
print(persona)
#accediendo a un valor en especifico
print(persona["profesion"])
#se puede usar el metodo ,get()
#Es util porque no da error si la clave no existe 
print(persona.get("edad"))
#Modificar un valor existente 
persona["edad"]=16
print(persona.get("edad"))
#Agreagar un par (clave:valor)
persona["ciudaad"]="San pepe"
print(persona)
#recorrer un diccionario con un bucle 
for clave,valor in persona.items():
    print(f"{clave}:{valor}")
