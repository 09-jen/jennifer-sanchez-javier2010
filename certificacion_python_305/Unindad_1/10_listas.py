try:
    #declarando una lista 
    materias=["programacion","filosofia","matematicas","ingles"]
    print(materias[0])
    materias.append("lengua y comunicacion")
    print(materias)
    materias[1]="biologia"
    print(materias)
    materias.remove("matematicas")
    print(materias)
except ImportError:
    print("indice incorrecto")