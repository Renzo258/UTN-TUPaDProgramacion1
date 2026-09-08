#punto 1

for i in range(0, 101):
    print(i)

#punto 2   

numero = int(input("Ingresa un numero entero: "))

temporal = numero
contador_digitos = 0 

if temporal == 0:
    contador_digitos = 1
else:
    if temporal < 0:
        temporal = temporal * -1
    while temporal > 0:
        temporal = temporal // 10
        contador_digitos += 1

print(f"El numero {numero} tiene {contador_digitos} digitos.")

#punto 3

numero1 = int(input("Ingresa el primer numero entero: "))
numero2 = int(input("Ingresa el segundo numero entero: "))

if numero1 < numero2:
    inicio = numero1 + 1
    fin = numero1
else:
    inicio = numero2 + 1
    fin = numero1

suma = 0 
for numero in range(inicio, fin):
    suma += numero
suma = sum(range(inicio, fin))

print(f"La suma de los numeros entre {numero1} y {numero2}, excluyendolos, es: {suma}")

#punto 4

suma_acumulada = 0
print("Ingresa numeros enteros para sumarlos. Despues ingrese 0 para finalizar.")

while True:
    numero = int(input("Ingresa un numero: "))
    if numero == 0:
        break

    suma_acumulada += numero

print(f"El total acumalado de estos numeros es: {suma_acumulada}")

#punto 5 

import random
numero_secreto = random.randint(0, 9)
intentos = 0
print("¡Bienvenido al juego! Intenta adivinar el numero entre 0 y 9.")

while True:
    intento_usuario = int(input("Ingresa tu numero: "))
    intentos += 1 

    if intento_usuario ==numero_secreto:
        print(f"¡Acertaste! El numero era {numero_secreto}.")
        print(f"Cnatidad de intentos necesarios:{intentos}")
        break
    else:
        print("Incorreco. ¡Segui intentando!")

#punto 6

for i in range(100, -1, -2):
    print(i)

#punto 7

limite = int(input("Ingresa un numero entero positivo: "))
suma_final = 0

for i in range(0, limite + 1):
    suma_final += i 
print(f"La suma de todos los numeros desde 0 hasta {limite} es: {suma_final}")

#punto 8

cantidad_total = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Vas a ingresar {cantidad_total} numeros enteros.")

for i in range(cantidad_total):
    numero = int(input("Ingresa un numero entero: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\n---RESULTADOS FINALES---")
print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)
print("Cantidad de numeros positivos:", positivos)
print("Cantidad de numeros negativos:", negativos)

#punto 9

cantidad_total = 100
suma_total = 0

print(f"Vas a ingresar {cantidad_total} numeros para calcular su promedio.")

for i in range(cantidad_total):
    numero = int(input("Ingresa un numero: "))
    suma_total += numero

media = suma_total / cantidad_total
print("\n---RESULTADO---")
print("La media de los numeros ingresados es:", media)

#punto 10

numero = int(input("Ingresa un numero entero: "))
numero_anbsoluto = abs(numero)
numero_invertido = 0 

while numero_absoluto > 0:
    digito = numero_absoluto % 10 
    numero_invertido = numero_invertido * 10 + digito
    numero_absoluto //= 10

if numero < 0:
    numero_invertido = -numero_invertido

print(f"El numero invertido es: {numero_invertido}")

