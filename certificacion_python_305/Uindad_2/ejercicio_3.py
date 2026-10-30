colores=["azul","morado","rojo","amarillo","negro"]
color=input("Ingresa el color")#naranja
encontrado=False
for contador in colores: #recorre los elementos de la lista
    print(contador)
    #Si el color actual es "rojo", detener el bucle
    if contador==color:
        print("color encontado! Saliendo del bucle")
        encontrado=True
        break
if not encontrado:
        print("el color,no se enconrtro") 