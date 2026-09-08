#punto 1    
edad = int(input("Por favor, ingresa tu edad: "))

if edad > 18:
    print("Es mayor de edad")

#punto 2

nota = float(input("Por favor, ingresar su nota de examen: "))

if nota >= 6:
    print("Aprobaste el examen. ¡¡Felicitaciones!!")
else:
    print("Desaprobaste el examen. ¡¡No bajes los brazos!!")

#punto3

numero = int(input("Por favor,ingresar un numero par: "))

if numero % 2 == 0:
    print("Ha ingresado un muero par.")
else:
    print("Por favor, ingrese un numero par.")

#punto 4

edad = int(input("Bienvenido!!. Por favor, ingrese su edad: "))

if edad < 12:
    print("Niño/a.")

elif edad < 18:
    print ("Adolescente.")

elif edad < 30:
    print("Adulto/a joven.")

else:
    print("Aulto/a.")


#punto 5

contraseña = input("Por favor, ingrese su contraseña: ")
longitud = len(contraseña)

if 8 <= longitud <= 14:
    print("Ha ingresado una contrasña correcta.")
else:
    print("Por favor ingrese una contrasña de 8 y 14 caracteres.")

#punto 6

import random 
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100)for i in range(50)]

la_moda = mode(numeros_aleatorios)
la_mediana = median(numeros_aleatorios)
la_media = mean(numeros_aleatorios)

print (f"Media: {la_media:.2f} / Mediana: {la_mediana} / Moda: {la_moda}")

if la_media > la_mediana and la_mediana > la_moda:
    print("El resultado determina que hay: Sesgo positivo o a la derecha.")

elif la_media < la_mediana and la_mediana < la_moda:
    print("El resultado determina que hay: Sesgo negativo o a la izquierda.")

elif la_media == la_mediana == la_moda:
    print("El resultado determina: Sin sesgo.")

else:
    print("El resultado no cumple estrictamente con los criterios de sesgo definidos.")

#punto 7

texto = input("Por favor, ingresa una palabra o frase: ")

ultima_letra = texto [-1]

vocales="aeiouAEIOU"

if ultima_letra in vocales:
    texto_resultante = texto + "!"
else:
    texto_resultante = texto

print("Resultado:", texto_resultante)

#punto 8

nombre = input("Ingresa tu nombre: ")

print("\n---MENU DE OPCIONES---")
print("1. Mostrar en MAYUSCULAS.")
print("2. Mostrar en minusculas.")
print("3. Mostrar con la primera letra minuscula.")
opcion = input("Elegi una opcion (1, 2 o 3): ")

if opcion == "1":
    nombre_transformado = nombre.upper()
    print("Resultado:", nombre_transformado)
elif opcion == "2":
    nombre_transformado = nombre.lower()
    print("Resultado:", nombre_transformado)
elif opcion == "3":
    nombre_transformado = nombre.title()
    print("Resultado:", nombre_transformado)
else:
    print("Opcion invalida. Por favor, selecciona 1,2 o 3.")

#punto 9 

magnitud = float(input("Ingresa la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud < 4:
    print("Leve (perceptible).")
elif magnitud < 5:
    print("Moderado (sentido por personas, oero generalmente no causan daños).")
elif magnitud < 6: 
    print("Fuerte (puede causar daños en estructuras debiles).")
elif magnitud < 7:
    print("Muy fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#punto 10

hemisferio = input("¿En que hemisferio estas? (N para el norte / S para el sur).")
mes = int(input("Ingresa el numero de mes (1 al 12): "))
dia = int(input("Ingresa el numero del dia (1 al 31): "))

periodo = 0

if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    periodo = 1

elif (mes == 3 and dia >=21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    periodo = 2

elif (mes == 6 and dia >=21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <=20):
    periodo = 3

elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <=20):
    periodo = 4

print("\n---RESULTADO---")

if periodo == 1:
    if hemisferio == "N" or hemisferio == "n":
        print("Estas en imvierno.")
    else:
        print("Estas en verano.")

elif periodo == 2:
    if hemisferio == "N" or hemisferio == "n":
        print("Estas en primavera.")
    else:
        print("Estas en otoño.")

elif periodo == 3:
    if hemisferio == "N" or hemisferio == "n":
        print("Estas en verano.")
    else:
        print("Estas en invierno.")

elif periodo == 4:
    if hemisferio == "N" or hemisferio == "n":
        print("Estas en otoño.")
    else:
        print("Estas en primavera.")
        

