alumno=alumnos=["cristian","geraldine","santa","giovanni","josafat","mayte","shantal","yael"]
promedio=[]
for nombre in alumnos:
    calificacion=float(input("ingresa el promedio de"+nombre+":"))
    promedio.append(calificacion)
    promedio_alto=promedio[0]
    promedio__bajo=promedio[0]
    alumno_alto=alumnos[0]
    alumno_bajo=[0]
    print("\n---PROMEDIO DE CADA ALUMNO---")
    for i in range(8):
        print(alumnos[0],":",promedio[0])

        if promedio[0]>promedio_alto:
            promedio_alto=promedio[0]
            alumno_alto=alumnos[0]
        if promedio[0]<promedio__bajo:
            promedio__bajo=promedio[0]
            alumno_bajo=alumnos[0]
    print("\npromedio mas alto:", alumno_alto,promedio_alto)
    print("\npromedio mas bajo:", alumno_bajo,promedio__bajo)
