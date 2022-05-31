#Jennifer Forero Ayala
#Ejercicio 2 
print ( " Identificaremos si la persona es mayor de edad y su indice de masa corporal" )

#Aca empezamos a pedirle al usuario la informacion 
documento= input ("Insertar tipo de documento:")
num= input ("Numero de documento")
nombre= input ("Nombre")
age= int(input ("Ingresar la edad"))

#Se indica si es mayo o menor 
if age <18:
    print("Menor de edad")
else: 
    print("Mayor de edad")

sexo= input ("Indique su sexo")
peso= float (input("Escriba su peso en kg "))
estatura= float (input("Escriba su estatura en metros"))

#Se hace la formula para ontener el indice de masa corporal de la persona 
imc= round (float(peso)/float(estatura)**2,2)
print ("Indice de masa corporal es" +  str(imc))
input()
    