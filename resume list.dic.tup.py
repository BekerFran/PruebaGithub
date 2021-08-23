#Para crear una lista constante:
lista_enteros = [1, 3, 900]
lista_heterogenea = [“Hola”, 1, 2.34]
lista_de_listas = [“Elemento”, [1, 2, 3], [3.4, “casa”]]
lista_vacia = []

#Indexado
#● Para acceder a los elementos, usamos la misma notación que vimos para
#strings.
#Los índices en el caso de listas funcionan de manera análoga al caso de strings.
#○ Cualquier expresión entera puede usarse.
#○ Debemos controlar que el índice exista, de lo contrario tendríamos un error en la ejecución.
#○ Si el índice es negativo, se cuenta desde el final de la lista

>>> lista_enteros[2]
900
>>> lista_heterogenea[0]
'Hola'
>>> lista_de_listas[1]
[1, 2, 3]
>>> lista_de_listas[2]
[3.4, 'casa']
>>> lista_de_listas[2][1]
'casa'

#Pertenencia
#● Para evaluar si un elemento está en una lista, usamos el operador in.
    >>> lista = [1, 5 ,8, "palabra"]
    >>> 1 in lista   
    True

    #Operaciones sobre listas
#● Análogamente a strings, el símbolo + concatena dos listas.
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> c
[1, 2, 3, 4, 5, 6]

#Slicing
#● El operador : también funciona para listas.
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']

#Operaciones que no modifican una lista
• len(l) : #Devuelve el número de elementos de la lista l.
• min(l) : #Devuelve el mínimo elemento de la lista l siempre que los datos sean comparables.
• max(l) : #Devuelve el máximo elemento de la lista l siempre que los datos sean comparables.
• sum(l) : #Devuelve la suma de los elementos de la lista l, siempre que los datos se puedan sumar.
• dato in l : #Devuelve True si el dato dato pertenece a la lista l y False en caso contrario.
• l.index(dato) : #Devuelve la posición que ocupa en la lista l el primer elemento con valor dato.
• l.count(dato) : #Devuelve el número de veces que el valor dato está contenido en la lista l.
• all(l) : #Devuelve True si todos los elementos de la lista l son True y False en caso contrario.
• any(l) : #Devuelve True si algún elemento de la lista l es True y False en caso contrario.
