# Jennifer Forero Ayala 
# Ejercicio 3
#Tiene la ocpion de elegir que area quiere calcular 
while True:
  print(f"Preciona t para el area del triangulo \n\
o para el area del circulo.\n\
c para el area del cuadrado\n")

  Opcion=input()

  if Opcion=='t':
#area del triangulo 

      base = None
      altura = None
#se le pide a la persona que digite la informacion 
      while True: 
        try:
           base = float (input("Indique la base del triangulo: "))
           break
        except:
            print("Debe escribir un numero.")

      while True:
        try:
            altura = float (input("Indique la altura del triangulo: "))
            break
        except:
            print("Debe escribir un numero.")
#se hace la formula a calcular 
      area = base * altura / 2
      print("el area del triangulo es igual: {}".format(area))

#area del circulo
#se le pide a la persona que digite la informacion 
  elif Opcion=='o':
        radio= float(input("Indique el radio del circulo"))
        pi=3.1416
#se hace la formula a calcular 
        area=pi * radio**2

        print ("El area del circulo es: "+ str(area))

# area del cuadrado 
#se le pide a la persona que digite la informacion 
  elif Opcion=='c':
     lado= int(input("Indique el lado del cuadrado"))
#se hace la formula a calcular      
     area= lado * lado 
     print("El area del cuadrado es:", area )

  input ()      


