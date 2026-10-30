promedio=[9,10,6,8,7]
#1. encontrar el promedio mas bajo usando un ciclo for
#Suponemos inicialmente que el promedio mas bajo es el elemnto primer elemnto
promedio_bajo=promedio[0]
promedio_alto=promedio[0]
for contador in promedio:
    if contador>promedio_bajo:
        promedio_bajo=contador
    if contador<promedio_alto:
         promedio_alto=contador
print(promedio_bajo)
print(promedio_alto)
        