matriz=[
    ["A","B","C","D","E","F","G","H","I"],#fila 3 x 9 columnas#fila 2 x 3 columnas
    ["J","K","L","M","N","Ñ","O","P","Q"],#fila 3 x 9 columnas#fila 2 x 3 columnas
    ["R","S","T","U","V","X","W","Y","Z"],#fila 3 x 9 columnas#fila 2 x 3 columnas 
]
filas= 3
columnas= 9
for i in range(filas):
    for j in range(columnas):
        print(f"posicion[{i}][{j}]={matriz[i][j]}")