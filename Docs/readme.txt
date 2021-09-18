Responder preguntas y marcar con el nombre de los integrantes

INTEGRANTES:
Nombre: Juan Sebastian Sanchez Delgado, Correo: js.sanchezd1@uniandes.edu.co, Codigo: 2020135577
Nombre: Nicolás Alexander rodriguez Pinilla, Correo: na.rodriguezp1@uniandes.edu.co, Codigo: 20202250

ANALISIS DE COMPLEJIDAD Y PRUEBAS DE EJECUCION:

REQUISITO 1: 

La funcion listarCronologicamente crea una lista nueva y agrega a esta ultimo
todos los artistas que esten en el rango. Para ello se debio haber reccorrido la lista completa 
una vez, por lo que la complejidad hasta este punto es O(N), siendo N el numero de elemntos de
la lista original.

Luego, se crea una segunda lista donde se agregaran los elementos de la primera lista creada ya ordenados. 
En el peor caso, todos los elementos de la lista estaran situados tambien en la primera lista creada, asi que
la complejidad se seguira expresando en terminos de N. El programa recorerra la lista completa un numero definido 
por la siguiente expresion: añoFinal - añoInicial.

En conclusion, la complejidad temporal del programa es N + (añoFinal - añoInicial)N, que en notacion O vendria siendo: O(N).
En el peor caso, la cantidad de memoria extra que se utiliza seria de 2N.

REQUISITO 2:

REQUISITO 3: 

REQUISITO 4:

REQUISITO 5: 
