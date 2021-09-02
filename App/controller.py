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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    catalog = model.newCatalog()
    return catalog
# Funciones para la carga de datos
def loadData(catalog):
    loadObras(catalog)
    loadNombre(catalog)
    loadAnioNac(catalog)
    loadNacionalidad(catalog)
    loadGenero(catalog)

def loadObras(catalog):
    obrasfile = cf.data_dir + 'MoMA/Artists-utf8-5pct.csv'
    input_file = csv.DictReader(open(obrasfile, encoding='utf-8'))

def loadNombre(catalog):
    nombrefile = cf.data_dir + 'MoMA/Artists-utf8-5pct.csv'
    input_file = csv.DictReader(open(nombrefile, encoding='utf-8'))


def loadAnioNac(catalog):
    anionacfile = cf.data_dir + 'MoMA/Artists-utf8-5pct.csv'
    input_file = csv.DictReader(open(anionacfile, encoding='utf-8'))


def loadNacionalidad(catalog):
    nacionalidadfile = cf.data_dir + 'MoMA/Artists-utf8-5pct.csv'
    input_file = csv.DictReader(open(nacionalidadfile, encoding='utf-8'))

def loadGenero(catalog):
    generofile = cf.data_dir + 'MoMA/Artists-utf8-5pct.csv'
    input_file = csv.DictReader(open(generofile, encoding='utf-8'))  

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
