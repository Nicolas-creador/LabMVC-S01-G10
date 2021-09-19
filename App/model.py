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

def nacionalidadCreadores(catalog):
    listaNacionalidades = {}
    info = {}
    for artista in lt.iterator(catalog["artistas"]):
        if artista["Nationality"] not in listaNacionalidades:
            listaNacionalidades[artista["Nationality"]]= 0 
        info[artista["ConstituentID"]] = artista["Nationality"]
    
    for obra in lt.iterator(catalog["obras"]):
        for id in obra["ConstituentID"].split(", "):
            id = id.replace("[","")
            id = id.replace("]","")
            pais = info[id]
            listaNacionalidades[pais] += 1
            

    return listaNacionalidades

# Funciones utilizadas para comparar elementos dentro de una lista



# Funciones de ordenamiento
