try:
 numero1=float(input("Igresa el primer numero"))
 numero2=float(input("Igresa el segundo numero"))
 resultado=numero1/numero2
except ZeroDivisionError:
  print("SOLO INTRODUCE NUMEROS")
except ValueError:
  print("Division entre cero fallida")
else:
  print("el resultadoes",resultado)
finally:
  print("PROGRAMA FINALIZADO")