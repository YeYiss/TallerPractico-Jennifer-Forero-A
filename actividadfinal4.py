#Jennifer Forero Ayala 
#Ejercicio 4 

#Damos la opcion de que elegia dos numeros 
num1= input ("Dijite un numero: ")
num2= input ("Dijita otro numero: ")

#Puede elegir que quiere hacer con estos numeros 
while True:
  print(f"Preciona s para sumar\n\
r para restar.\n\
m para multiplicar\n\
d para dividir\n")

#segun la letra que elgia, se indicara la respuesata 
  Opcion=input()
  
  if Opcion=='s':
     res= int(num1) + int(num2) 
     print ("Resusltado de la suma" +  str (res))

  elif Opcion=='r':
     res= int(num1) - int(num2)  
     print ("Resusltado de la resta " +  str (res))

  elif Opcion=='m':
      res= int(num1) * int(num2) 
      print ("Resusltado de la multiplicacion " +  str (res))

  elif Opcion=='d':
      res= int(num1) / int(num2) 
      print ("Resusltado de la division " +  str (res))
      
  input ()