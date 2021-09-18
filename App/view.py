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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

def listarCronologicamente(catalog, añoInicial, añoFinal):
    return controller.listarCronologicamente(catalog, añoInicial, añoFinal)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
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
        print("Numero de artistas dentro del rango: " + str(tamaño))

        artist1 = lt.getElement(listaEnRango, 1)
        artist2 = lt.getElement(listaEnRango, 2)
        artist3 = lt.getElement(listaEnRango, 3)
        artist4 = lt.getElement(listaEnRango, tamaño-2)
        artist5 = lt.getElement(listaEnRango, tamaño-1)
        artist6 = lt.getElement(listaEnRango, tamaño)

        artistas = artist1,artist2,artist3,artist4,artist5,artist6
        for artista in artistas:    
            print("Nombre: " + artista["DisplayName"],
                    ", Nacimiento: "+ artista["BeginDate"], 
                    ", Fallecimmiento: " + artista["EndDate"],
                    ", Nacionalidad: " + artista["Nationality"],
                    ", Genero: " + artista["Gender"])
    else:
        sys.exit(0)
sys.exit(0)
