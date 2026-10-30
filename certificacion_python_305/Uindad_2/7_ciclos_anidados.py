#ciclo externo para el numero de la base de la tabla 
for i in range(1,4):
    print(f"---tabla del{i}")
    #ciclo interno para multiplicar del 1 al 10
    for j in range(1,11):
    #1(i) x 1(j)=1
      print(f"{i} X {j}= {i*j}")
      #aqui sale del siclo interno
    print(f"aqui termina la tabla del {i}")


