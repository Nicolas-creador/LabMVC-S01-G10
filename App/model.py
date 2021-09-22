"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'obras': None,
               'artistas': None}

    catalog['obras'] = lt.newList()
    catalog['artistas'] = lt.newList('SINGLE_LINKED')

    return catalog
# Funciones para agregar informacion al catalogo

def addObra(catalog, obra):
    lt.addLast(catalog['obras'], obra)

def addArtist(catalog, artista):
    lt.addLast(catalog['artistas'], artista)
# Funciones para creacion de datos



# Funciones de consulta
def listarCronologicamente(catalog, añoInicial, añoFinal):
    listaEnRango = lt.newList()
    for artista in lt.iterator(catalog["artistas"]):
        if int(artista["BeginDate"]) >= añoInicial and int(artista["BeginDate"]) <= añoFinal:
            lt.addLast(listaEnRango, artista)

    listaFinal = lt.newList()
    for i in range(añoInicial,añoFinal+1):
        for elemento in lt.iterator(listaEnRango):
            if int(elemento["BeginDate"]) == i:
                lt.addLast(listaFinal, elemento)  

    return listaFinal
   
   
def transportar_obras(catalog,departamento):
    count = 0
    peso= 0
    tamaño = 0
    mas_antiguo= 0
    conteo= 1
    antigüedad= lt.newList()
    for obra in lt.iterator(catalog["obras"]):
        num_int = (obra["Dimensions"]).replace(")","(")
        num_int = num_int.split ("(")
        for elemento in (num_int):
            if "cm" in elemento:
                elemento = (elemento).replace("x","*")
                elemento = (elemento).replace("cm","")
                print(elemento)
        conteo +=1
        print(conteo)
        if departamento != (obra["Department"]):
            count += 1
            if (obra["Weight (kg)"]) != "":
                peso += float(obra["Weight (kg)"])
        if (obra["Date"]) != "":
            if int(obra["Date"]) < mas_antiguo:
                mas_antiguo = (obra["Date"])
    lt.addLast(antigüedad,obra)
    return count



# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
