# UTN-TUPaDProgramacion1
Entrega de trabajo colaborativo.

#1
print ("hola mundo")

#2
nombre = input("¿Como es tu nombre? ")
print("Mucho gusto, " + nombre)

#3
nombre_completo = input ("Hola, ingrese su nombre completo porfavor: ")
print ("Mucho gusto: "+nombre_completo )
edad = input ("¿Cual es tu edad? ")
nacionalidad = input ("¿De que pais eres? ")
print ("Tu nombre es " +nombre_completo+ " tienes " +edad+ ", y eres de " +nacionalidad )

#4
import math
radio = float (input("ingrese el radio del circulo : "))
area = math.pi * radio**2
print("el area del circulo es :", area )

radio = float (input("ingrese el radio : "))
circunferencia = 2 * 3.1416 * radio
print("la circunferencia es : " , circunferencia)

#5
Nombre = input(" Coloque su nombre porfavor :")
print("¡Mucho gusto ! " + Nombre)
Segundos_totales = int(input("Introduces las cantidad de segundos : "))
# 3600 Segundos = 1 hora
Horas = Segundos_totales / 3600
print(f"{Segundos_totales} Segundos equivale a {Horas:.2f} horas.")

#6
print ("Hola bienvenido usuario.")
numero= int (input ("Ingrese el numero que desea, por favor :" ))
for i in range (1,11): 
    print (f"{numero} x {i} = {numero * i}")

#7
numero1 = int(input("Ingrese el primer numero (distinto de 0) :"))
numero2 = int(input("Ingrese el segundo numero (distinto de 0) :"))

suma = numero1 + numero2 
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print ("La suma entre estos dos numeros es:", suma )
print ("La resta entre estos dos numeros es:", resta )
print ("La multiplicacion entre estos dos numeros es:", multiplicacion )
print ("La division entre estos dos numeros es:", division )

#8
nombre = input ("Coloque su nombre, por favor: ")
print ("Mucho gusto," + nombre)
altura = float(input("Ingrese su altura : "))
peso = float(input("Ingrese su peso : "))
potencia = altura ** 2 
print ("El peso potenciado da : ", potencia )
total = (peso) / (altura)
print ("El resultado del IMC es : ", total)

#9
nombre = input ("¿Cual es tu nombre? : ")
print ("Bienvenido", nombre)
numero1 = float(input("Coloque su numero en grado Celsiu : "))
print ("Su numero es: ", numero1)
fahrenheint = (numero1 * 1.8) + 32
print ("El resultado es : ", fahrenheint)

#10
print ("Hola, bienvenido a este programa")
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero porfavor: "))
numero3 = float(input("Ingrese el tercer numero: "))

promedio = (numero1 + numero2 + numero3) / 3

print("el promedio de los tres numeros es: ",promedio)