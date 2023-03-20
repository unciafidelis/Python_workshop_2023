## Listas

Hay cuatro tipos de datos de colección en Python:

- Lista: es una colección ordenada y cambiable (modificable). Permite miembros duplicados.
- Tupla: es una colección ordenada e inalterable o inmodificable (inmutable). Permite miembros duplicados.
- Conjunto: es una colección que está desordenada, no indexada y no modificable, pero podemos agregar nuevos elementos al conjunto. No se permiten miembros duplicados.
- Diccionario: es una colección desordenada, cambiable (modificable) e indexada. No hay miembros duplicados.

Una lista es una colección de diferentes tipos de datos ordenados y modificables (mutables). Una lista puede estar vacía o puede tener diferentes elementos de tipo de datos.

### Cómo crear una lista

En Python podemos crear listas de dos formas:

- Uso de la función incorporada de lista

```python
# sintaxis
lista = list()
```

```python
lista_vacia = list() # esta es una lista vacía, no hay ningún elemento en la lista
print(len(lista_vacia)) # 0
```

- Usando corchetes cuadrados, []

```python
# sintaxis
lista = []
```

```python
lista_vacia = [] # esta es una lista vacia, no hay ningun elemento en la lista
print(len(lista_vacia)) # 0
```

Listas con valores iniciales. Usamos `_len()_` para encontrar la longitud de una lista.

```python
frutas = ['platano', 'naranja', 'mango', 'limón'] # lista de frutas
verduras = ['Tomate', 'Patata', 'Repollo', 'Cebolla', 'Zanahoria'] # lista de verduras
productos_animales = ['leche', 'carne', 'mantequilla', 'yogur'] # lista de productos animales
tech_web = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB'] # lista de tecnologías web
paises = ['Méxicoia', 'Estonia', 'Dinamarca', 'Suecia', 'Noruega'] # lista de paises

# print las listas y su longitud
print('Frutas:', frutas)
print('Número de frutas:', len(frutas))
print('Verduras:', verduras)
print('Número de verduras:', len(verduras))
print('Productos animales:',productos_animales)
print('Número de productos animales:', len(productos_animales))
print('Tecnologías web:', tech_web)
print('Número de tecnologías web:', len(tech_web))
print('Países:', paises)
print('Número de países:', len(paises))
```

- Las listas pueden tener elementos de diferentes tipos de datos

```py
 lista = ['Alejandro', 38, True, {'pais':'México', 'ciudad':'Zacatecas'}] # lista que contiene diferentes tipos de datos
```

### Acceder a los elementos de la lista mediante la indexación positiva

Accedemos a cada elemento de una lista utilizando su índice. Un índice de lista comienza desde 0.

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
primera_fruta = fruta[0] # estamos accediendo al primer elemento usando su índice
print(primera_fruta) # plátano
segunda_fruta = frutas[1]
print(segunda_fruta) # naranja
ultima_fruta = frutas[3]
print(ultima_fruta) # limón
# Último índice
last_index = len(frutas) - 1
ultima_fruta = frutas[ultimo_index]
```

### Acceder a los elementos de la lista mediante la indexación negativa

La indexación negativa significa comenzar desde el final, -1 se refiere al último elemento, -2 se refiere al penúltimo elemento.

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
primera_fruta = frutas[-4]
ultima_fruta = frutas[-1]
segundo_ultimo = frutas[-2]
print(primera_fruta) # plátano
print(ultima_fruta) # limón
print (segundo_ultimo) # mango
```

### Elementos de la lista de desembalaje

```python
lista = ['item','item2','item3', 'item4', 'item5']
primer_item, segundo_item, tercer_item, *resto = lista
print(primer_item)     # item1
print(segundo_item)    # item2
print(tercer_item)     # item3
print(resto)           # ['item4', 'item5']

```

```python
# Primer ejemplo
frutas = ['plátano', 'naranja', 'mango', 'limón', 'lima', 'manzana']
primera_fruta, segundo_fruta, tercer_fruta, *resto = lista
print(primera_fruta) # plátano
print(segundo_fruta) # naranja
print(tercer_fruta) #mango
print(resto) # ['limón','lima','manzana']
# segundo Ejemplo de lista de desembalaje
first, segundo, tercer,*resto, decimo = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(segundo)         # 2
print(tercer)          # 3
print(resto)           # [4,5,6,7,8,9]
print(decimo)          # 10
# tercer Ejemplo de lista de desembalaje
paises = ['Alemania', 'Francia', 'Bélgica', 'Suecia', 'Dinamarca', 'México', 'Noruega', 'Islandia', 'Estonia']
al, fr, be, su, *scandinavo, es = paises
print(al)
print(fr)
print(be)
print(su)
print(escandinavo)
print(es)
```

### Slicing Items from a List

- Indexación positiva: podemos especificar un rango de índices positivos especificando el inicio, el final y el paso, el valor de retorno será una nueva lista. (valores predeterminados para `inicio = 0, final = len (lista) - 1 (último elemento), paso = 1`)

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
all_frutas = frutas[0:4] # devuelve todas las frutas
# esto también dará el mismo resultado que el anterior
all_frutas = frutas[0:] # si no ponemos donde parar toma todo el resto
naranja_and_mango = frutas[1:3] # no incluye el primer índice
naranja_mango_limon = frutas[1:]
naranja_and_limon = frutas[::2] # aquí usamos un tercer argumento, paso. Tomará cada segundo artículo - ['plátano', 'mango']
```

- Indexación negativa: podemos especificar un rango de índices negativos especificando el inicio, el final y el paso, el valor de retorno será una nueva lista.

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
all_frutas = frutas[-4:] # devuelve todas las frutas
naranja_y_mango = frutas[-3:-1] # no incluye el ultimo indice,['naranja', 'mango']
naranja_mango_limon = frutas[-3:] # esto dará a partir de -3 hasta el final,['naranja', 'mango', 'limón']
reversa_frutas = frutas[::-1] # un paso negativo llevará la lista en orden inverso,['limón', 'mango', 'naranja', 'plátano']
```

### Modificación de listas

Lista es una colección ordenada mutable o modificable de elementos. Modifiquemos la lista de frutas.

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
frutas[0] = 'aguacate'
print(frutas) # ['aguacate', 'naranja', 'mango', 'limón']
frutas[1] = 'manzana'
print(frutas) # ['aguacate', 'manzana', 'mango', 'limón']
last_index = len(frutas) - 1
frutas[last_index] = 'lima'
print(frutas) # ['aguacate', 'manzana', 'mango', 'lima']
```

### Comprobación de elementos en una lista

Comprobación de un elemento si es miembro de una lista mediante el operador *in*. Vea el ejemplo a continuación.

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
existe = 'plátano' in frutas
print(existe)  # True
existe = 'lima' in frutas
print(existe)  # False
```

### Adición de elementos a una lista

Para agregar elementos al final de una lista existente, usamos el método *append()*.

```python
# sintaxis
lista = list()
lista.append(item)
```

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
frutas.append('manzana')
print(frutas)           # ['plátano', 'naranja', 'mango', 'limón', 'manzana']
frutas.append('lima')   # ['plátano', 'naranja', 'mango', 'limón', 'manzana', 'lima']
print(frutas)
```

### Inserción de elementos en una lista

Podemos usar el método *insert()* para insertar un solo elemento en un índice específico en una lista. Tenga en cuenta que otros elementos se desplazan a la derecha. Los métodos *insert()* toman dos argumentos: índice y un elemento para insertar.

```python
# sintaxis
lista = ['item1', 'item2']
lista.insert(index, item)
```

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
frutas.insert(2, 'manzana') # intercalar manzana entre naranja y mango
print(frutas)           # ['plátano', 'naranja', 'manzana', 'mango', 'limón']
frutas.insert(3, 'lima')   # ['plátano', 'naranja', 'manzana', 'lima', 'mango', 'limón']
print(frutas)
```

### Eliminación de elementos de una lista

El método de eliminación elimina un elemento específico de una lista

```python
# sintaxis
lista = ['item1', 'item2']
lista.remove(item)
```

```python
frutas = ['plátano', 'naranja', 'mango', 'limón', 'plátano']
frutas.remove('plátano')
print(frutas)  # ['naranja', 'mango', 'limón', 'plátano'] - este método elimina la primera aparición del elemento en la lista
frutas.remove('limón')
print(frutas)  # ['naranja', 'mango', 'plátano']
```

### Eliminación de elementos mediante Pop

El método *pop()* elimina el índice especificado (o el último elemento si no se especifica el índice):

```python
# sintaxis
lista = ['item1', 'item2']
lista.pop()       # last item
lista.pop(index)
```

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
frutas.pop()
print(frutas)       # ['plátano', 'naranja', 'mango']

frutas.pop(0)
print(frutas)       # ['naranja', 'mango']
```

### Eliminación de elementos mediante del

La palabra clave *del* elimina el índice especificado y también se puede usar para eliminar elementos dentro del rango del índice. También puede eliminar la lista por completo.

```python
# sintaxis
lista = ['item1', 'item2']
del lista[index] # elimina un solo item
del lista        # elimina completamente la lista
```

```python
frutas = ['plátano', 'naranja', 'mango', 'limón', 'kiwi', 'lima']
del frutas[0]
print(frutas)       # ['naranja', 'mango', 'limón', 'kiwi', 'lima']
del frutas[1]
print(frutas)       # ['naranja', 'limón', 'kiwi', 'lima']
del frutas[1:3]     # esto elimina los elementos entre los índices dados, en este caso que no elimina el elemento con el índice 3
print(frutas)       # ['naranja', 'lima']
del frutas
print(frutas)       # Esto debería dar: NameError: el nombre 'frutas' no está definido
```

### Elementos de la lista de compensación

El método *clear()* vacía la lista:

```python
# sintaxis
lista = ['item1', 'item2']
lista.clear()
```

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
frutas.clear()
print(frutas)       # []
```

### Copiar una lista

Es posible copiar una lista reasignándola a una nueva variable de la siguiente forma: lista2 = lista1. Ahora, lista2 es una referencia de lista1, cualquier cambio que hagamos en lista2 también modificará el original, lista1. Pero hay muchos casos en los que no nos gusta modificar el original sino que nos gusta tener una copia diferente. Una forma de evitar el problema anterior es usar `_copy()_`.

```python
# sintaxis
lista = ['item1', 'item2']
lista_copy = lista.copy()
```

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
frutas_copia = frutas.copy()
print(frutas_copia)       # ['plátano', 'naranja', 'mango', 'limón']
```

### Unirse a las listas

Hay varias formas de unir o concatenar dos o más listas en Python.

- Operador Plus (+)

```python
# sintaxis
lista3 = lista1 + lista2
```

```python
numeros_positivos = [1, 2, 3, 4, 5]
cero = [0]
numeros_negativos = [-5,-4,-3,-2,-1]
enteros = numeros_negativos + cero + numeros_positivos
imprimir(enteros) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
frutas = ['plátano', 'naranja', 'mango', 'limón']
verduras = ['Tomate', 'Patata', 'Repollo', 'Cebolla', 'Zanahoria']
frutas_y_verduras = frutas + verduras
print(frutas_y_verduras ) # ['plátano', 'naranja', 'mango', 'limón', 'Tomate', 'Papa', 'Repollo', 'Cebolla', 'Zanahoria']
```
- Unirse usando el método extend ()
  El método *extend()* permite añadir lista en una lista. Vea el ejemplo a continuación.

```python
# sintaxis
lista1 = ['item1', 'item2']
lista2 = ['item3', 'item4', 'item5']
lista1.extend(lista2)
```

```python
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Números:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
numeros_negativos = [-5,-4,-3,-2,-1]
numeros_positivos = [1, 2, 3,4,5]
zero = [0]

numeros_negativos.extend(zero)
numeros_negativos.extend(numeros_positivos)
print('Integers:', numeros_negativos) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
frutas = ['plátano', 'naranja', 'mango', 'limón']
verduras = ['tomate', 'papa', 'repollo', 'cebolla', 'zanahoria']
frutas.extend(verduras)
print('frutas y verduras:', frutas ) # frutas y verduras: ['plátano', 'naranja', 'mango', 'limón', 'tomate', 'papa', 'repollo', 'cebolla', 'zanahoria']
```

### Contar elementos en una lista

El método *count()* devuelve el número de veces que aparece un elemento en una lista:

```python
# sintaxis
lista = ['item1', 'item2']
lista.count(item)
```

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
print(frutas.count('naranja'))   # 1
edades = [22, 19, 24, 25, 26, 24, 25, 24]
print(edades.count(24))           # 3
```

### Encontrar el índice de un artículo

El método *index()* devuelve el índice de un elemento de la lista:

```python
# sintaxis
lista = ['item1', 'item2']
lista.index(item)
```

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
print(frutas.index('naranja'))   # 1
edades = [22, 19, 24, 25, 26, 24, 25, 24]
print(edades.index(24))           # 2, la primera ocurrencia
```

### Invertir una lista

El método *reverse()* invierte el orden de una lista.

```python
# sintaxis
lista = ['item1', 'item2']
lista.reverse()

```

```python
frutas = ['plátano', 'naranja', 'mango', 'limón']
frutas.reverse()
print(frutas) # ['limón', 'mango', 'naranja', 'plátano']
edades = [22, 19, 24, 25, 26, 24, 25, 24]
edades.reverse()
print(edades) # [24, 25, 24, 26, 25, 24, 19, 22]
```

### Clasificación de elementos de la lista

Para ordenar listas podemos usar el método `_sort()_` o las funciones integradas `_sorted()_`. El método `_sort()_` reordena los elementos de la lista en orden ascendente y modifica la lista original. Si un argumento del método `_sort()_` reverse es igual a verdadero, ordenará la lista en orden descendente.

- `sort()`: este método modifica la lista original

  ```python
  # sintaxis
  lista = ['item1', 'item2']
  lista.sort()                # ascendente
  lista.sort(reverse=True)    # descendente
  ```

  **Ejemplo:**

  ```python
  frutas = ['plátano', 'naranja', 'mango', 'limón']
  frutas.sort()
  print(frutas)             # ordenados en orden alfabético, ['plátano', 'limón', 'mango', 'naranja']
  frutas.sort(reverse=True)
  print(frutas) # ['naranja', 'mango', 'limón', 'plátano']
  edades = [22, 19, 24, 25, 26, 24, 25, 24]
  edades.sort()
  print(edades) #  [19, 22, 24, 24, 24, 25, 25, 26]
 
  edades.sort(reverse=True)
  print(edades) #  [26, 25, 25, 24, 24, 24, 22, 19]
  ```

  sorted(): devuelve la lista ordenada sin modificar la lista original
  **Ejemplo:**
  
  ```python
  frutas = ['plátano', 'naranja', 'mango', 'limón']
  print(sorted(frutas))   # ['plátano', 'limón', 'mango', 'naranja']
  # Reverse order
  frutas = ['plátano', 'naranja', 'mango', 'limón']
  frutas = sorted(frutas,reverse=True)
  print(frutas)     # ['naranja', 'mango', 'limón', 'plátano']
  ```

