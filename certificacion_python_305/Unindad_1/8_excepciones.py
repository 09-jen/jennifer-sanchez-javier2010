try:
 #ejemplo 1 sin manejo de excepciones 
 numero1=int(input("Igresa el primer numero"))
 numero2=int(input("Igresa el segundo numero"))
 resultado=numero1/numero2
 print(resultado)
except ZeroDivisionError:
  print("Division entre cero fallida")
except ValueError:
  print("SOLO INTRODUCE NUMEROS")
  