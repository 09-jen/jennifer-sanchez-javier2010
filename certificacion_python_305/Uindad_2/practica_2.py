inventario={
    "lapiz":10,
    "cuadernos":16,
    "borrador":10,
        "estuadiante":True                                                                                                                                                     
}
producto=input("ingresa el producto:")
cantidad=int(input("ingresa la cantidad:"))
if producto in inventario:
    if  cantidad <= inventario[producto]:
     print("venta autorizada")
     inventario[producto] -=cantidad 
    else:
     print("venta rechazada")
print(inventario)