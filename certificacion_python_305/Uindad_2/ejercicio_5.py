carrito=[]
cantidad=int(input("¿Cuantos productos quieres agregar al carrito?"))
for contador in range(cantidad):
    producto=input(f"Ingresa el producto{contador+1}")
    carrito.append(producto)
print("\nTu lista de compra es:")
print(carrito) 