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

#Métodos de listas
● .append(elem) #inserta elementos al final de una lista.
● .insert(pos, elem) #inserta un elemento en la posición pos.
● .index(elem) #devuelve la posición de un elemento, si no está produce un error.
● .pop(pos) #quita el elemento de la posición pos de la lista

#Operaciones que modifican una lista
• l1 + l2 : #Crea una nueva lista concatenan los elementos de la listas l1 y l2.
• l.append(dato) : #Añade dato al final de la lista l.
• l.extend(sequencia) : #Añade los datos de sequencia al final de la lista l.
• l.insert(índice, dato) : #Inserta dato en la posición índice de la lista l y desplaza los elementos
#una posición a partir de la posición índice.
• l.remove(dato) : #Elimina el primer elemento con valor dato en la lista l y desplaza los que están
#por detrás de él una posición hacia delante.
• l.pop([índice]) : #Devuelve el dato en la posición índice y lo elimina de la lista l, desplazando
#los elementos por detrás de él una posición hacia delante.
• l.sort() : #Ordena los elementos de la lista l de acuerdo al orden predefinido, siempre que los elementos
#sean comparables.
• l.reverse() : #invierte el orden de los elementos de la lista l.

#Copia de listas
#Existen dos formas de copiar listas:
• Copia por referencia l1 = l2: #Asocia la la variable l1 la misma lista que tiene asociada la variable l2,
#es decir, ambas variables apuntan a la misma dirección de memoria. Cualquier cambio que hagamos a
#través de l1 o l2 afectará a la misma lista.
• Copia por valor l1 = list(l2): #Crea una copia de la lista asociada a l2 en una dirección de memoria
#diferente y se la asocia a l1. Las variables apuntan a direcciones de memoria diferentes que contienen
#los mismos datos. Cualquier cambio que hagamos a través de l1 no afectará a la lista de l2 y viceversa

#Tuplas
#Una tupla es una secuencias ordenadas de objetos de distintos tipos.
#Se construyen poniendo los elementos entre corchetes ( ) separados por comas.
#Se caracterizan por:
#• Tienen orden.
#• Pueden contener elementos de distintos tipos.
#• Son inmutables, es decir, no pueden alterarse durante la ejecución de un programa.
#Se usan habitualmente para representar colecciones de datos una determinada estructura semántica, como
#por ejemplo un vector o una matriz.

# Tupla vacía
2 type(())
3 <class 'tuple'>
4 # Tupla con elementos de distintos tipos
5 (1, "dos", True)
6 # Vector
7 (1, 2, 3)
8 # Matriz
9 ((1, 2, 3), (4, 5, 6))

#Creación de tuplas mediante la función tuple()
#Otra forma de crear tuplas es mediante la función tuple().
#• tuple(c) : Crea una tupla con los elementos de la secuencia o colección c.
#Se pueden indicar los elementos separados por comas, mediante una cadena, o mediante una colección de
#elementos iterable.
1 >>> tuple()
2 ()
3 >>> tuple(1, 2, 3)
4 (1, 2, 3)
5 >>> tuple("Python")
6 ('P', 'y', 't', 'h', 'o', 'n')
7 >>> tuple([1, 2, 3])
8 (1, 2, 3)

#Operaciones con tuplas
#El acceso a los elementos de una tupla se realiza del mismo modo que en las listas. También se pueden obtener
#subtuplas de la misma manera que las sublistas.
#Las operaciones de listas que no modifican la lista también son aplicables a las tuplas.
1 >>> a = (1, 2, 3)
2 >>> a[1]
3 2
4 >>> len(a)
5 3
6 >>> a.index(3)
7 2
8 >>> 0 in a
9 False
10 >>> b = ((1, 2, 3), (4, 5, 6))
11 >>> b[1]
12 (4, 5, 6)
13 >>> b[1][2]
14 6

Diccionarios
#Un diccionario es una colección de pares formados por una clave y un valor asociado a la clave.
#Se construyen poniendo los pares entre llaves { } separados por comas, y separando la clave del valor con
#dos puntos :.
#Se caracterizan por:
#• No tienen orden.
#• Pueden contener elementos de distintos tipos.
#• Son mutables, es decir, pueden alterarse durante la ejecución de un programa.
#• Las claves son únicas, es decir, no pueden repetirse en un mismo diccionario, y pueden ser de cualquier
#tipo de datos inmutable.

1 # Diccionario vacío
2 type({})
3 <class 'dict'>
4 # Diccionario con elementos de distintos tipos
5 {'nombre':'Alfredo', 'despacho': 218, 'email':'asalber@ceu.es'}
6 # Diccionarios anidados
7 {'nombre_completo':{'nombre': 'Alfredo', 'Apellidos': 'Sánchez Alberca'}}

#Acceso a los elementos de un diccionario
#• d[clave] devuelve el valor del diccionario d asociado a la clave clave. Si en el diccionario no existe
#esa clave devuelve un error.
#• d.get(clave, valor) devuelve el valor del diccionario d asociado a la clave clave. Si en el diccionario
#no existe esa clave devuelve valor, y si no se especifica un valor por defecto devuelve None.

1 >>> a = {'nombre':'Alfredo', 'despacho': 218, 'email':'asalber@ceu.es'}
2 >>> a['nombre']
3 'Alfredo'
4 >>> a['despacho'] = 210
5 >>> a
6 {'nombre':'Alfredo', 'despacho': 218, 'email':'asalber@ceu.es'}
7 >>> a.get('email')
8 'asalber@ceu.es'
9 >>> a.get('universidad', 'CEU')
10 'CEU'

#Operaciones que no modifican un diccionario
#• len(d) : Devuelve el número de elementos del diccionario d.
#• min(d) : Devuelve la mínima clave del diccionario d siempre que las claves sean comparables.
#• max(d) : Devuelve la máxima clave del diccionario d siempre que las claves sean comparables.
#• sum(d) : Devuelve la suma de las claves del diccionario d, siempre que las claves se puedan sumar.
#• clave in d : Devuelve True si la clave clave pertenece al diccionario d y False en caso contrario.
#• d.keys() : Devuelve un iterador sobre las claves de un diccionario.
#• d.values() : Devuelve un iterador sobre los valores de un diccionario.
#• d.items() : Devuelve un iterador sobre los pares clave‑valor de un diccionario.

>>> a = {'nombre':'Alfredo', 'despacho': 218, 'email':'asalber@ceu.es'}
2 >>> len(a)
3 3
4 >>> min(a)
5 'despacho'
6 >>> 'email' in a
7 True
8 >>> a.keys()
9 dict_keys(['nombre', 'despacho', 'email'])
10 >>> a.values()
11 dict_values(['Alfredo', 218, 'asalber@ceu.es'])
12 >>> a.items()
13 dict_items([('nombre', 'Alfredo'), ('despacho', 218), ('email', '
asalber@ceu.es')])

#Operaciones que modifican un diccionario
#• d[clave] = valor : Añade al diccionario d el par formado por la clave clave y el valor valor.
#• d.update(d2). Añade los pares del diccionario d2 al diccionario d.
#• d.pop(clave, alternativo) : Devuelve del valor asociado a la clave clave del diccionario d y
#lo elimina del diccionario. Si la clave no está devuelve el valor alternativo.
#• d.popitem() : Devuelve la tupla formada por la clave y el valor del último par añadido al diccionario
#d y lo elimina del diccionario.
#• del d[clave] : Elimina del diccionario d el par con la clave clave.
#• d.clear() : Elimina todos los pares del diccionario d de manera que se queda vacío.
1 >>> a = {'nombre':'Alfredo', 'despacho': 218, 'email':'asalber@ceu.es'}
2 >>> a['universidad'] = 'CEU'
3 >>> a
4 {'nombre': 'Alfredo', 'despacho': 218, 'email': 'asalber@ceu.es', '
universidad': 'CEU'}
5 >>> a.pop('despacho')
6 218
7 >>> a
8 {'nombre': 'Alfredo', 'email': 'asalber@ceu.es', 'universidad': 'CEU'}
>>> a.popitem()
10 ('universidad', 'CEU')
11 >>> a
12 {'nombre': 'Alfredo', 'email': 'asalber@ceu.es'}
13 >>> del a['email']
14 >>> a
15 {'nombre': 'Alfredo'}
16 >>> a.clear()
17 >>> a
18 {}

#Copia de diccionarios
#Existen dos formas de copiar diccionarios:
#• Copia por referencia d1 = d2: Asocia la la variable d1 el mismo diccionario que tiene asociado la
#variable d2, es decir, ambas variables apuntan a la misma dirección de memoria. Cualquier cambio que
#hagamos a través de l1 o l2 afectará al mismo diccionario.
#• Copia por valor d1 = list(d2): Crea una copia del diccionario asociado a d2 en una dirección de
#memoria diferente y se la asocia a d1. Las variables apuntan a direcciones de memoria diferentes que
#contienen los mismos datos. Cualquier cambio que hagamos a través de l1 no afectará al diccionario
#de l2 y viceversa.
1 >>> a = {1:'A', 2:'B', 3:'C'}
2 >>> # copia por referencia
3 >>> b = a
4 >>> b
5 {1:'A', 2:'B', 3:'C'}
6 >>> b.pop(2)
7 >>> b
8 {1:'A', 3:'C'}
9 >>> a
10 {1:'A', 3:'C'}
1 >>> a = {1:'A', 2:'B', 3:'C'}
2 >>> # copia por referencia
3 >>> b = dict(a)
4 >>> b
5 {1:'A', 2:'B', 3:'C'}
6 >>> b.pop(2)
7 >>> b
8 {1:'A', 3:'C'}
9 >>> a



10 {1:'A', 2:'B', 3:'C'}