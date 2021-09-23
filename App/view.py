"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print(chr(27)+"[1;32m")
    print("Bienvenido")
    print(chr(27)+"[0;37m")
    print(chr(27)+"[4;32m"+"1" + chr(27)+ "[0;37m" + "- Cargar información en el catálogo")
    print(chr(27)+"[4;32m"+ "2" + chr(27)+ "[0;37m" + "- Listar cronológicamente los artistas")
    print(chr(27)+"[4;32m"+ "3" + chr(27)+ "[0;37m" + "- Listar cronologicamente las adquisiciones")
    print(chr(27)+"[4;32m"+ "4" + chr(27)+ "[0;37m" + "- Clasificar las obras de un artista por tecnica")
    print(chr(27)+"[4;32m"+ "5" + chr(27)+ "[0;37m" + "- Clasificar las obras por la nacionalidad de sus creadores")
    print(chr(27)+"[4;32m"+ "6" + chr(27)+ "[0;37m" + "- Transportar obras de un departamento")

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

# Requisito 1
def listarCronologicamente(catalog, añoInicial, añoFinal):
    return controller.listarCronologicamente(catalog, añoInicial, añoFinal)
 
# Requisito 2
def listarAdquisiciones(catalog, fechaInicial, fechaFinal):
    return controller.listarAdquisiciones(catalog, fechaInicial, fechaFinal)

# Requisito 4
def nacionalidadCreadores(catalog):
    nacionalidades = controller.nacionalidadCreadores(catalog)
    return nacionalidades
# Requisito 5
def transportar_obras(catalog,departamento):
    return controller.transportar_obras(catalog,departamento)
def obra_antigua(catalog,departamento):
    return controller.obra_antigua(catalog,departamento)

def printSortResults(ord_obras, sample=5):
    size = lt.size(ord_obras)
    if size > sample:
        print("Las cinco obras más antiguas son: ")
        i=1
        while i <= sample:
            obra = lt.getElement(ord_obras,i)
            print('Titulo: ' + obra['Title'],
            ", Clasificación " + obra["Classification"],
            ", Artista " + obra["ConstituentID"],
            ", Fecha "+ obra["Date"],
            ", medio "+ obra["Medium"],
            ", dimensiones"+ obra["Dimensions"])
            i+=1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    print(chr(27)+"[1;37m")
    inputs = input('Seleccione una opción para continuar: ')
    print(chr(27)+"[0;37m")

    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Obras cargadas: ' + str(lt.size(catalog['obras'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artistas'])))

    elif int(inputs[0]) == 2:
        añoInicial = int(input("Ingrese el año inicial(yyyy): "))
        añoFinal = int(input("Ingrese el año final(yyyy): "))
        print("Listando los artistas de manera cronologica ....")
        
        listaEnRango = listarCronologicamente(catalog, añoInicial, añoFinal)
        tamaño = lt.size(listaEnRango)
        print("\n")
        print("Numero de artistas dentro del rango: " + str(tamaño)+"\n")

        artist1 = lt.getElement(listaEnRango, 1)
        artist2 = lt.getElement(listaEnRango, 2)
        artist3 = lt.getElement(listaEnRango, 3)
        artist4 = lt.getElement(listaEnRango, tamaño-2)
        artist5 = lt.getElement(listaEnRango, tamaño-1)
        artist6 = lt.getElement(listaEnRango, tamaño)

        print(chr(27)+"[1;37m"+"Los primeros y los últimos 3 son: "+chr(27)+"[0;37m")

        artistas = artist1,artist2,artist3,artist4,artist5,artist6
        for artista in artistas:    
            print(chr(27)+"[1;34m"+ "Nombre: " + chr(27)+"[0;37m"+ artista["DisplayName"],
                    chr(27)+"[1;34m"+ ", Nacimiento: "+ chr(27)+"[0;37m"+ artista["BeginDate"], 
                    chr(27)+"[1;34m"+ ", Fallecimmiento: " + chr(27)+"[0;37m"+ artista["EndDate"],
                    chr(27)+"[1;34m"+ ", Nacionalidad: " + chr(27)+"[0;37m"+ artista["Nationality"],
                    chr(27)+"[1;34m"+ ", Genero: " + chr(27)+"[0;37m"+ artista["Gender"])
    
    elif int(inputs[0]) == 3:
        fechaInicial = (input("Ingrese la fecha inicial(yyyy-mm-dd): "))
        año, mes, día = map(int, fechaInicial.split('-'))
        fechaInicial= (año, mes, día)
        fechaFinal = (input("Ingrese el año final(yyyy-mm-dd): "))
        año2, mes2, día2 = map(int, fechaFinal.split('-'))
        fechaFinal= (año2, mes2, día2)
        print("Listando las adquisiciones de manera cronologica ....")
        resultado,compras = listarAdquisiciones(catalog, fechaInicial, fechaFinal)
        tamaño = lt.size(resultado)
        print("Numero de obras dentro del rango: " + str(tamaño))
        print("Número total de obras adquiridas por compra " + str(compras))

        obra1 = lt.getElement(resultado, 1)
        obra2 = lt.getElement(resultado, 2)
        obra3 = lt.getElement(resultado, 3)
        obra4 = lt.getElement(resultado, tamaño-2)
        obra5 = lt.getElement(resultado, tamaño-1)
        obra6 = lt.getElement(resultado, tamaño)

        print(chr(27)+"[1;37m"+"Las primeros y las últimos 3 obras son: "+chr(27)+"[0;37m")

        obras = obra1,obra2,obra3,obra4,obra5,obra6
        for obra in obras:    
            print("Título: " + obra["Title"],
                    ", Fecha: " + obra["Date"],
                    ", Medio: " + obra["Medium"],
                    ", Dimensiones: " + obra["Dimensions"])

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
       clasificacion,obras = nacionalidadCreadores(catalog)
       print(chr(27)+"[1;44m"+"NACIONALIDADES CON EL MAYOR NUMERO DE OBRAS"+chr(27)+"[0;37m")
       print("\n")
       for pais in lt.iterator(clasificacion): 
           for llave in pais.keys():
               print(chr(27)+"[1;34m"+llave+"   "+chr(27)+"[0;37m"+str(pais[llave]))
               print("\n")

       print(chr(27)+"[1;44m"+"INFORMACION DE LAS 20 PRIMERAS OBRAS DE LA NACIONALIDAD CON EL MAYOR NUMERO DE OBRAS"+chr(27)+"[0;37m")
       conteo = 0
       for obra in lt.iterator(obras): 
           print("\n")
           conteo += 1
           for llave2 in obra.keys():
               print(chr(27)+"[1;34m"+llave2+": "+chr(27)+"[0;37m"+obra[llave2])
           if conteo == 25:
               break 
           
    elif int(inputs[0]) == 6:
        departamento = (input("Ingrese el departamento a transportar las obras: "))
        transporte,count,peso,precio_estimado = transportar_obras(catalog,departamento)
        print("El número de obras a transportar es: " + str(count))
        result = controller.ordenarObras(transporte)
        print("Peso estimado de las obras: " + str(peso))
        printSortResults(result)
        
    else:
        sys.exit(0)
sys.exit(0)
