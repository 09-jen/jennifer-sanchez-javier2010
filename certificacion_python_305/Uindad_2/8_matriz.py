#creando una  matriz 
matriz=[
    [5,8,6],#fila 1 x 3 columnas
    [3,9,4],#fila 2 x 3 columnas
]
#obteniendo el numero de filas y columnas 
filas=len(matriz)
columnas=len(matriz[0])
#ciclo externo para los indices de las filas(i)
for i in range(0,2):
    #ciclo interno para los indices de las columnas (j)
    for j in range(0,3):
        print(f"posicion[{i}][{j}]={matriz[i][j]}")