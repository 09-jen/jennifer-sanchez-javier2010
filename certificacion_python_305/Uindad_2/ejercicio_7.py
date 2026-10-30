#el mapa del tesoro
mapa=[
    ["B",".",".","."],
    [".",".",".","."],
    [".",".",".","."],
    [".",".","A",","],
]
filas=len(mapa)
columnas=len(mapa[0])
#recorriendo la matriz con ciclos anidados
#ciclo externo para manejar filas(i)
for i in range(filas):#i<4
    #ciclo interno para manejar columnas(j)
    for j in range(columnas):
        #verificarmos si encontramos el tesoro 
        if mapa [i][j]=="A":
            print(f"tesoro enconrado en la posicion [{i}][{j}]")
        if mapa [i][j]=="B":
             print(f"tesoro enconrado en la posicion [{i}][{j}]")
            
