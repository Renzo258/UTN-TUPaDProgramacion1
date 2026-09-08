numero = list(range (10 , 31 , 5 ))
print(numero [ :2 ])

#PUNTO 7
Autos = ["Palio" , "Mustang" , "Camaro" , "Ram"]
Autos [1] = "Honda"
Autos [2] = "Fiat"
print (Autos)

#PUNTO 8
dobles = []
dobles.append (5 * 2)
dobles.append (10 * 2)
dobles.append ( 15 * 2)
print(dobles)

#PUNTO 9
compras = [["Pan" , "Leche,"] , ["Arroz" , "Fideos"] , ["Salsa" , "Agua "]]
# a) Agregamos  "jugo" al tercer cliente 
compras[2].append ("jugo")
# b) Reemplazar "fideos" por "Tallarines "
compras[1][1] = "Tallarines "
# c) Eliminar "pan" del primer cliente 
compras[0].remove("Pan")
# d) Mostrar la lista resultante 
print(compras)

#PUNTO 10
lista_anidada = [ 15 , True , [25.5 , 57.9 , 30.6] , False ]
print(lista_anidada)