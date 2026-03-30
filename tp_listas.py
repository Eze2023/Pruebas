#ejercicio 1
notas = [5,2,7,1,9,7,10,4,1,6]
aux = 0
promedio = 0
notabaja = 0
notaalta = 10

for nota in notas:
    print(nota)
    aux += nota
    if nota >= notabaja:
        notabaja = nota
    elif nota <= notaalta:
        notaalta = nota
    else:
        print("error")

promedio = aux/len(notas)
print(f"promedio: {promedio}")
print(f"nota mas baja: {notabaja}")
print(f"nota mas alta: {notaalta}")

#ejercicio 2
lista = [""] * 5
aux = 5

for i in range(5):
    lista[i] = input(f"cargue {aux} productos: ")
    aux-=1
lista.sort()
print(lista)

opcion = input(f"que producto desea eliminar? (escribir el elemento, no la posicion) ")

for producto in lista:
    if producto == opcion:
        lista.remove(opcion)
print(lista)

#ejercicio 3
numeros = [7,65,72,2,39,0,52,95,22,90,23,68,51,12,4]
par = []
impar = []

print(numeros)

for numero in numeros:
    if numero % 2 == 0:
       par.append(numero)
    else:
        impar.append(numero)

print(f"par: {par},impar:{impar}")

#ejercicio 4
datos = [1,3,5,3,7,1,9,5,3]

datosnuevos = sorted(set(datos))

print(datosnuevos)

#ejercicio 5
alumnos = ["lucas", "miguel", "camila", "sofia", "marta", "nico", "mauro", "pamela"]

opcion1 = ""
opcion2 = ""

opcion1 = input("quiere agregar un nuevo estudiante? (si o no)")
if opcion1 == "si":
    nuevoalumno = input("introduce el nombre: ")
    alumnos.append(nuevoalumno)
    print("nombre ingresado...")
if opcion1 == "no" or opcion1 == "si":
    opcion2 = input("quiere eliminar uno existente? (si o no)")
    if opcion2 == "si":
        opcion3 = input("a quien quiere eliminar?")
        alumnos.remove(opcion3)
        print("nombre eliminado...")
    else:
        print("codigo terminado...")
print(alumnos)

#ejercicio 6
numeros = [1,2,3,4,6,8,9]
aux = 0
nuevalista = []

aux = len(numeros)
nuevalista.append(numeros[aux-1])

nuevalista += numeros[0:aux-1]
print(nuevalista)

#ejercicio 7
temperaturas = [[10,24],[3,26],[8,31],[2,23],[8,33],[12,28],[1,7]]
pmaximas = 0
pminimas = 0
resultado = 0
atermica = 0

for minimas in range(len(temperaturas)):
    pminimas += temperaturas[minimas][0] 

for maximas in range(len(temperaturas)):
    pmaximas += temperaturas[maximas][1]

total1 = pminimas/len(temperaturas)
total2 = pmaximas/len(temperaturas)

for i in range(len(temperaturas)):
    resultado = temperaturas[i][1] - temperaturas[i][0]
    if resultado >= atermica:
        atermica = resultado

print(f"promedio minimas: {total1}, promedio maximas: {total2}")
print(f"la mayor amplitud termica fue de: {atermica}")

#ejercicio 8
notas = [[2,2,7],[4,6,7],[2,4,9],[8,8,4],[2,1,3]]

for i in range(len(notas)):
    promedio = sum(notas[i])/len(notas[i])
    print(f"alumno {i+1}: {promedio} ")

for x in range(len(notas[0])):
    resultado = 0
    for i in range(len(notas)):
        resultado += notas[i][x]
    
    promedio = resultado/len(notas)
    print(f"materia {x+1}: {promedio} ")

#ejercicio 9
matriz = [["-","-","-"],["-","-","-"],["-","-","-"]]
fila = 0
columna = 0

for i in range(9):
    print("Jugador 1 usted jugara con las X")
    fila = int(input("ingrese la fila: "))
    columna = int(input("ingrese la columna: "))
    if matriz[fila][columna] == "-":
        matriz[fila][columna] = "X"
        fila = 0
        columna = 0
    print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")

    print("Jugador 2 usted jugara con las O")
    fila = int(input("ingrese la fila: "))
    columna = int(input("ingrese la columna: "))
    if matriz[fila][columna] == "-":
        matriz[fila][columna] = "O"
        fila = 0
        columna = 0
    print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")

#ejercicio 10
ventas = [[10, 12, 8, 9, 15, 7, 11],[5, 7, 6, 8, 10, 9, 4],[20, 18, 25, 22, 19, 30, 28],[3, 4, 2, 5, 6, 4, 3]]

for i in range(len(ventas)):
    print(f"producto {i+1}: {sum(ventas[i])}")

mayor_venta = 0
dia_mayor = 0
for j in range(len(ventas[0])):
    suma_dia = 0
    for i in range(len(ventas)):
        suma_dia += ventas[i][j]
    if suma_dia > mayor_venta:
        mayor_venta = suma_dia
        dia_mayor = j + 1
print(f"dia con mas ventas: {dia_mayor}")

mayor_total = 0
producto_mayor = 0
for i in range(len(ventas)):
    total = sum(ventas[i])
    if total > mayor_total:
        mayor_total = total
        producto_mayor = i + 1

print(f"producto mas vendido: {producto_mayor}")

#ejercicio 11
estudiantes = ["lucas", "miguel", "camila", "sofia", "marta", "nico", "mauro", "pamela", "juan", "ana"]

nombre = input("ingrese el nombre a buscar: ")

for i in range(len(estudiantes)):
    if estudiantes[i] == nombre:
        print(f"el nombre se encuentra en la lista y es el: {i}")
        break
    else:
        print("no esta en la lista")
        
#ejercicio 12
numeros = []

for i in range(8):
    num = int(input(f"ingrese el numero {i+1}: "))
    numeros.append(num)

print("original:", numeros)

ascendente = sorted(numeros)
print("menor a mayor:", ascendente)

ascendente.reverse()
print("mayor a menor:", ascendente)

#ejercicio 13
puntajes = [450, 1200, 875, 990, 300, 1500, 640] 

aux = 0

puntajes.sort()

numero = len(puntajes)

print(f"puntaje mas bajo: {puntajes[0]}")
print(f"puntaje mas alto: {puntajes[numero-1]}")
puntajes.reverse()
print(puntajes)

for i in range(len(puntajes)):
    if puntajes[i] == 990:
        print(f"la posicion es: {i}")
