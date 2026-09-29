#Punto 1 y 2

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario resultante:")
print(precios_frutas)

#punto 3

lista_frutas = list(precios_frutas.keys())

print("Lista de frutas sin precios:")
print(lista_frutas)

#punto 4

contactos = {}

print("Por favor, ingrese los datos de 5 contactos:")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero

nombre_consulta = input("\nIngrese el nombre del contacto que desea buscar: ")

if nombre_consulta in contactos:
    print(f"El número asociado a {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print("El contacto no existe en la agenda.")

#punto 5

frase = input("Ingrese una frase: ")
palabras = frase.lower().split()

palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print(f"Recuento: {recuento}")

#punto 6

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")


#punto 7

parcial_1 = {"Juan", "Ana", "Luis", "Sofia"}
parcial_2 = {"Ana", "Pedro", "Sofia", "Carlos"}

aprobaron_ambos = parcial_1.intersection(parcial_2)
print(f"Aprobaron ambos parciales: {aprobaron_ambos}")

aprobaron_solo_uno = parcial_1.symmetric_difference(parcial_2)
print(f"Aprobaron solo uno de los parciales: {aprobaron_solo_uno}")

total_aprobados = parcial_1.union(parcial_2)
print(f"Total de estudiantes que aprobaron al menos un parcial: {total_aprobados}")

#punto 8

productos = {"Manzanas": 50, "Bananas": 30, "Naranjas": 20}

print("Opciones disponibles: 1 (Consultar), 2 (Agregar stock), 3 (Nuevo producto)")
opcion = input("Seleccione una opción (1/2/3): ")

if opcion == "1":
    prod = input("Ingrese el nombre del producto a consultar: ")
    if prod in productos:
        print(f"El stock actual de {prod} es de {productos[prod]} unidades.")
    else:
        print("El producto no existe en el inventario.")

elif opcion == "2":
    prod = input("Ingrese el nombre del producto para añadir stock: ")
    if prod in productos:
        cantidad = int(input("Ingrese la cantidad de unidades a añadir: "))
        productos[prod] += cantidad
        print(f"Stock actualizado. Nuevo stock de {prod}: {productos[prod]}")
    else:
        print("El producto no existe. Use la opción 3 para darlo de alta.")

elif opcion == "3":
    prod = input("Ingrese el nombre del nuevo producto: ")
    if prod not in productos:
        cantidad = int(input("Ingrese el stock inicial: "))
        productos[prod] = cantidad
        print(f"Producto {prod} registrado con un stock inicial de {cantidad}.")
    else:
        print("El producto ya se encuentra registrado.")


#punto 9

agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "18:00"): "Gimnasio"
}

dia_consulta = input("Ingrese el día de la consulta (ej. lunes): ").strip().lower()
hora_consulta = input("Ingrese la hora de la consulta (ej. 10:00): ").strip()

clave_busqueda = (dia_consulta, hora_consulta)

if clave_busqueda in agenda:
    print(f"Actividad programada: {agenda[clave_busqueda]}")
else:
    print("No hay ninguna actividad agendada para ese día y hora.")

#punto 10

original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Uruguay": "Montevideo"}

invertido = {capital: pais for pais, capital in original.items()}

print("Diccionario original:")
print(original)
print("\nDiccionario invertido (Capitales como claves):")
print(invertido)