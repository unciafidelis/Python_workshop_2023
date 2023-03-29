# Introducción al análisis de datos

## Estadística

La estadística es la disciplina que estudia la _recopilación_, _organización_, _exhibición_, _análisis_, _interpretación_ y _presentación_ de datos.
La estadística es una rama de las matemáticas que se recomienda como requisito previo para la ciencia de datos y el aprendizaje automático. La estadística es un campo muy amplio pero nos centraremos en esta sección solo en la parte más relevante.
Después de completar este desafío, puede pasar al desarrollo web, el análisis de datos, el aprendizaje automático y la ciencia de datos. Cualquiera que sea el camino que pueda seguir, en algún momento de su carrera obtendrá datos en los que puede trabajar. Tener algunos conocimientos estadísticos te ayudará a tomar decisiones basadas en datos.

## Datos

¿Qué son los datos? Los datos son cualquier conjunto de caracteres que se recopilan y traducen para algún propósito, generalmente análisis. Puede ser cualquier carácter, incluidos texto y números, imágenes, sonido o video. Si los datos no se ponen en un contexto, no tienen ningún sentido para un ser humano o una computadora. Para dar sentido a los datos, necesitamos trabajar en los datos utilizando diferentes herramientas.

El flujo de trabajo del análisis de datos, la ciencia de datos o el aprendizaje automático parte de los datos. Los datos se pueden proporcionar desde alguna fuente de datos o se pueden crear. Hay datos estructurados y no estructurados.

Los datos se pueden encontrar en formato pequeño o grande. La mayoría de los tipos de datos que obtendremos se han cubierto en la sección de manejo de archivos.

## Módulo de estadísticas

El módulo Python _statistics_ proporciona funciones para calcular estadísticas matemáticas de datos numéricos. El módulo no pretende ser un competidor de bibliotecas de terceros, como NumPy, SciPy, o paquetes de estadísticas propietarios completos destinados a estadísticos profesionales, como Minitab, SAS y Matlab. Está dirigido al nivel de graficadores y calculadoras científicas.

## NumPy

En la primera sección, definimos a Python como un gran lenguaje de programación de propósito general por sí solo, pero con la ayuda de otras bibliotecas populares como (numpy, scipy, matplotlib, pandas, etc.) se convierte en un poderoso entorno para la computación científica.

NumPy es la biblioteca central para computación científica en Python. Proporciona un objeto de arreglo multidimensional de alto rendimiento y herramientas para trabajar con matrices.

Hasta ahora, hemos estado usando vscode, pero de ahora en adelante recomendaría usar Jupyter Notebook o Google Colab. Si está utilizando anaconda, la mayoría de los paquetes comunes están incluidos y no tiene paquetes de instalación si instaló anaconda.

```sh
$ pip install numpy
```

## Importando NumPy

```python
    # Cómo importar numpy
    import numpy as np
    # Cómo verificar la versión del paquete numpy
    print('numpy:', np.__version__)
    # Comprobación de los métodos disponibles
    print(dir(np))
```

### Creación de arreglos int numpy

```python
    # Crear lista de python
    lista_python = [1,2,3,4,5]

    # Comprobación de tipos de datos
    print('Tipo:', type (lista_python)) # <class 'list'>
    #
    print(lista_python) # [1, 2, 3, 4, 5]

    lista_bidimencional = [[0,1,2], [3,4,5], [6,7,8]]

    print(lista_bidimencional)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    # Creación de un arreglo Numpy (Numerical Python) a partir de la lista de python

    np_arreglo_desde_lista = np.arraylista_python)
    print(type (np_arreglo_desde_lista))   # <class 'numpy.ndarreglo'>
    print(np_arreglo_desde_lista) # array[1, 2, 3, 4, 5])
```

### Creación de matrices numpy con datos flotante

Creación de un arreglo numpy flotante de la lista con un parámetro de tipo de datos flotante

```python
    # Python list
    lista_python = [1,2,3,4,5]

    np_arreglo_lista2 = np.arraylista_python, dtype=float)
    print(np_arreglo_lista2) # array[1., 2., 3., 4., 5.])
```

### Creación de arreglos numpy boolean

Crear un arreglo boolean a numpy de la lista

```python
    np_buleano_arreglo = np.array[0, 1, -1, 0, 0], dtype=bool)
    print(np_buleano_arreglo) # array[False,  True,  True, False, False])
```

### Creando un arreglo multidimensional usando numpy

Un arreglo numpy puede tener una o varias filas y columnas

```python
    lista_bidimencional = [[0,1,2], [3,4,5], [6,7,8]]
    numpy_lista_bidimencional = np.arraylista_bidimencional)
    print(type (numpy_lista_bidimencional))
    print(numpy_lista_bidimencional)
```

```sh
    <class 'numpy.ndarreglo'>
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
```

### Convertir arreglo numpy a lista

```python
# Siempre podemos convertir un arreglo de nuevo en una lista de python usando tolist().
np_a_lista = np_arreglo_desde_lista.tolist()
print(type (np_a_lista))
print('one dimensional arreglo:', np_a_lista)
print('two dimensional arreglo: ', numpy_lista_bidimencional.tolist())
```

```sh
    <class 'list'>
    one dimensional arreglo: [1, 2, 3, 4, 5]
    two dimensional arreglo:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

### Creando un arreglo numpy a partir de una tupla

```python
# arreglo numpy de tupla
# Creando tupla en Python
python_tupla = (1,2,3,4,5)
print(type (python_tupla)) # <class 'tuple'>
print('python_tupla: ', python_tupla) # python_tupla:  (1, 2, 3, 4, 5)

np_arreglo_desde_tupla = np.arraypython_tupla)
print(type (np_arreglo_desde_tupla)) # <class 'numpy.ndarreglo'>
print('np_arreglo_desde_tupla: ', np_arreglo_desde_tupla) # np_arreglo_desde_tupla:  [1 2 3 4 5]
```

### Forma de arreglo numpy

El método de forma proporciona la forma del arreglo como una tupla. La primera es la fila y la segunda es la columna. Si el arreglo es solo unidimensional, devuelve el tamaño de el arreglo.

```python
    numeros = np.array[1, 2, 3, 4, 5])
    print(numeros)
    print('forma de los numeros: ', numeros.shape)
    print(numpy_lista_bidimencional)
    print('forma de los numpy_lista_bidimencional: ', numpy_lista_bidimencional.shape)
    tres_x_cuatro_matriz = np.array[[0, 1, 2, 3],
        [4,5,6,7],
        [8,9,10, 11]])
    print(tres_x_cuatro_matriz.shape)
```

```sh
    [1 2 3 4 5]
    forma de los numeros:  (5,)
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    forma de los numpy_lista_bidimencional:  (3, 3)
    (3, 4)
```

### Tipo de datos de matriz numpy

Tipo de tipos de datos: str, int, float, complex, bool, list, None

```python
lista_enteros = [-3, -2, -1, 0, 1, 2,3]
arreglo_enteros = np.arraylista_enteros)
arreglo_flotantes = np.arraylista_enteros, dtype=float)

print(arreglo_enteros)
print(arreglo_enteros.dtype)
print(arreglo_flotantes)
print(arreglo_flotantes.dtype)
```

```sh
    [-3 -2 -1  0  1  2  3]
    int64
    [-3. -2. -1.  0.  1.  2.  3.]
    float64
```

### Tamaño de una matriz numpy

En numpy para saber la cantidad de elementos en una lista de matriz numpy usamos el tamaño

```python
np_arreglo_desde_lista = np.array[1, 2, 3, 4, 5])
lista_bidimencional = np.array[[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('El tamaño:', np_arreglo_desde_lista.size) # 5
print('El tamaño:', lista_bidimencional.size)  # 3

```

```sh
    El tamaño: 5
    El tamaño: 9
```

## Operación matemática usando numpy

La matriz NumPy no es exactamente como la lista de python. Para realizar una operación matemática en la lista de Python, tenemos que recorrer los elementos, pero numpy puede permitir realizar cualquier operación matemática sin realizar un bucle.
Operacion matematica:

- Suma (+)
- Resta (-)
- Multiplicación (\*)
- División (/)
- Módulos (%)
- División de piso(//)
- Exponencial(\*\*)

### Adición

```python
# Operación matemática
# Adición
np_arreglo_desde_lista = np.array[1, 2, 3, 4, 5])
print('Arreglo original: ', np_arreglo_desde_lista)
suma_10_original = np_arreglo_desde_lista  + 10
print(suma_10_original)

```

```sh
    Arreglo original:  [1 2 3 4 5]
    [11 12 13 14 15]
```

### Sustracción

```python
# Sustracción
np_arreglo_desde_lista = np.array[1, 2, 3, 4, 5])
print('Arreglo original: ', np_arreglo_desde_lista)
resta_10_original = np_arreglo_desde_lista  - 10
print(resta_10_original)
```

```sh
    Arreglo original:  [1 2 3 4 5]
    [-9 -8 -7 -6 -5]
```

### Multiplicación

```python
# Multiplicación
np_arreglo_desde_lista = np.array[1, 2, 3, 4, 5])
print('Arreglo original: ', np_arreglo_desde_lista)
multiplica_10_original = np_arreglo_desde_lista * 10
print(multiplica_10_original)
```

```sh
    Arreglo original:  [1 2 3 4 5]
    [10 20 30 40 50]
```

### División

```python
# División
np_arreglo_desde_lista = np.array[1, 2, 3, 4, 5])
print('Arreglo original: ', np_arreglo_desde_lista)
divide_10_original = np_arreglo_desde_lista / 10
print(divide_10_original)
```

```sh
    Arreglo original:  [1 2 3 4 5]
    [0.1 0.2 0.3 0.4 0.5]
```

### Módulo

```python
# Módulo; Encontrar el resto
np_arreglo_desde_lista = np.array[1, 2, 3, 4, 5])
print('Arreglo original: ', np_arreglo_desde_lista)
modulo_3_original = np_arreglo_desde_lista % 3
print(modulo_3_original)
```

```sh
    Arreglo original:  [1 2 3 4 5]
    [1 2 0 1 2]
```

### División base o de piso

```python
# División base o de piso: el resultado de división sin el resto
np_arreglo_desde_lista = np.array[1, 2, 3, 4, 5])
print('Arreglo original: ', np_arreglo_desde_lista)
multiplica_10_original = np_arreglo_desde_lista // 10
print(multiplica_10_original)
```

### Exponencial

```python
# Exponencial es encontrar algún número la potencia de otro:
np_arreglo_desde_lista = np.array[1, 2, 3, 4, 5])
print('Arreglo original: ', np_arreglo_desde_lista)
multiplica_10_original = np_arreglo_desde_lista  ** 2
print(multiplica_10_original)
```

```sh
    Arreglo original:  [1 2 3 4 5]
    [ 1  4  9 16 25]
```

## Comprobación de tipos de datos

```python
#Enteros, números flotantes
np_entero_arreglo = np.array[1,2,3,4])
np_flotante_arreglo = np.array[1.1, 2.0,3.2])
np_buleano_arreglo = np.array[-3, -2, 0, 1,2,3], dtype='bool')

print(np_entero_arreglo.dtype)
print(np_flotante_arreglo.dtype)
print(np_buleano_arreglo.dtype)
```

```sh
    int64
    float64
    bool
```

### Tipos de conversión

Podemos convertir los tipos de datos de la matriz numpy

1. Entero a Flotante

```python
np_entero_arreglo = np.array[1,2,3,4], dtype = 'float')
np_entero_arreglo
```

    array[1., 2., 3., 4.])

2. Flotante a entero

```python
np_entero_arreglo = np.array[1., 2., 3., 4.], dtype = 'int')
np_entero_arreglo
```

```sh
    array[1, 2, 3, 4])
```

3. Entero a buleano

```python
np.array[-3, -2, 0, 1,2,3], dtype='bool')

```

```sh
    array[ True,  True, False,  True,  True,  True])
```

4. Entero a cadena

```python
np_flotante_lista.astype('int').astype('str')
```

```sh
    array['1', '2', '3'], dtype='<U21')
```

## Arreglos multidimensionales

```python
# arreglo de dos dimensiones
arreglo_dos_dimensiones = np.array[(1,2,3),(4,5,6), (7,8,9)])
print(type (arreglo_dos_dimensiones))
print(arreglo_dos_dimensiones)
print('Forma: ', arreglo_dos_dimensiones.shape)
print('Tamaño:', arreglo_dos_dimensiones.size)
print('tipo de dato:', arreglo_dos_dimensiones.dtype)
```

```sh
    <class 'numpy.ndarreglo'>
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    Shape:  (3, 3)
    Size: 9
    Data type: int64
```

### Obtener elementos de un arreglo numpy

```python
# 2 Dimension arreglo
arreglo_dos_dimensiones = np.array[[1,2,3],[4,5,6], [7,8,9]])
first_row = arreglo_dos_dimensiones[0]
second_row = arreglo_dos_dimensiones[1]
third_row = arreglo_dos_dimensiones[2]
print('primera fila:', first_row)
print('segunda fila:', second_row)
print('Third row: ', third_row)
```

```sh
    primera fila: [1 2 3]
    segunda fila: [4 5 6]
    Third row:  [7 8 9]
```

```python
first_column= arreglo_dos_dimensiones[:,0]
second_column = arreglo_dos_dimensiones[:,1]
third_column = arreglo_dos_dimensiones[:,2]
print('Primera columna:', first_column)
print('Segunda columna:', second_column)
print('Tercera columna: ', third_column)
print(arreglo_dos_dimensiones)

```

```sh
    Primera columna: [1 4 7]
    Segunda columna: [2 5 8]
    Tercera columna:  [3 6 9]
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
```

## Rebanar arreglos Numpy

Rebanar(slicing) en numpy es similar a rebanar en una lista de python

```python
arreglo_dos_dimensiones = np.array[[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = arreglo_dos_dimensiones[0:2, 0:2]
print(first_two_rows_and_columns)
```

```sh
    [[1 2]
     [4 5]]
```

### Cómo invertir las filas y todo arreglo?

```python
arreglo_dos_dimensiones[::]
```

```sh
    array[[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
```

### Invertir las posiciones de fila y columna

```python
    arreglo_dos_dimensiones = np.array[[1,2,3],[4,5,6], [7,8,9]])
    arreglo_dos_dimensiones[::-1,::-1]
```

```sh
    array[[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]])
```

## Cómo representar los valores perdidos?

```python
    print(arreglo_dos_dimensiones)
    arreglo_dos_dimensiones[1,1] = 55
    arreglo_dos_dimensiones[1,2] =44
    print(arreglo_dos_dimensiones)
```

```sh
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [[ 1  2  3]
     [ 4 55 44]
     [ 7  8  9]]
```

```python
    # Numpy Zeroes
    # numpy.zeros(shape, dtype=float, order='C')
    numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
    numpy_zeroes
```

```sh
    array[[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]])
```

```python
# Numpy ceros
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)
```

```sh
    [[1 1 1]
     [1 1 1]
     [1 1 1]]
```

```python
twoes = numpy_ones * 2
```

```python
# Reformar
# numpy.reshape(), numpy.flatten()
first_shape  = np.array[(1,2,3), (4,5,6)])
print(first_shape)
reformado = first_shape.reshape(3,2)
print(reformado)

```

```sh
    [[1 2 3]
     [4 5 6]]
    [[1 2]
     [3 4]
     [5 6]]
```

```python
aplanado = reformado.flatten()
aplanado
```

```sh
    array[1, 2, 3, 4, 5, 6])
```

```python
    ## Pila horizontal
    np_lista_uno = np.array[1,2,3])
    np_lista_dos = np.array[4,5,6])

    print(np_lista_uno + np_lista_dos)

    print('Pilas horizontales:', np.hstack((np_lista_uno, np_lista_dos)))
```

```sh
    [5 7 9]
    Pilas horizontales: [1 2 3 4 5 6]
```

```python
    ## Pila vertical
    print('Pilas verticales:', np.vstack((np_lista_uno, np_lista_dos)))
```

```sh
    Pilas verticales: [[1 2 3]
     [4 5 6]]
```

#### Generación de números aleatorios

```python
    # Generar un número flotante aleatorio
    flotante_aleatorio = np.random.random()
    flotante_aleatorio
```

```sh
    0.018929887384753874
```

```python
    # Generar 5 números flotantes aleatorios
    flotantes_aleatorios = np.random.random(5)
    flotantes_aleatorios
```

```sh
    array[0.26392192, 0.35842215, 0.87908478, 0.41902195, 0.78926418])
```

```python
    # Generando enteros aleatorios entre 0 y 10

    entero_aleatorio = np.random.randint(0, 11)
    entero_aleatorio
```

```sh
    4
```

```python
    # Genera números enteros aleatorios entre 2 y 11, y crea un arreglo de una fila
    entero_aleatorio = np.random.randint(2,10, size=4)
    entero_aleatorio
```

```sh
    array[8, 8, 8, 2])
```

```python
    # Genera enteros aleatorios entre 0 y 10
    entero_aleatorio = np.random.randint(2,10, size=(3,3))
    entero_aleatorio
```

```sh
    array[[3, 5, 3],
           [7, 3, 6],
           [2, 3, 3]])
```

### Generación de números aleatorios

```python
    # np.random.normal(mu, sigma, size)
    normal_arreglo = np.random.normal(79, 15, 80)
    normal_arreglo

```

```sh
    array[ 89.49990595,  82.06056961, 107.21445842,  38.69307086,
            47.85259157,  93.07381061,  76.40724259,  78.55675184,
            72.17358173,  47.9888899 ,  65.10370622,  76.29696568,
            95.58234254,  68.14897213,  38.75862686, 122.5587927 ,
            67.0762565 ,  95.73990864,  81.97454563,  92.54264805,
            59.37035153,  77.76828101,  52.30752166,  64.43109931,
            62.63695351,  90.04616138,  75.70009094,  49.87586877,
            80.22002414,  68.56708848,  76.27791052,  67.24343975,
            81.86363935,  78.22703433, 102.85737041,  65.15700341,
            84.87033426,  76.7569997 ,  64.61321853,  67.37244562,
            74.4068773 ,  58.65119655,  71.66488727,  53.42458179,
            70.26872028,  60.96588544,  83.56129414,  72.14255326,
            81.00787609,  71.81264853,  72.64168853,  86.56608717,
            94.94667321,  82.32676973,  70.5165446 ,  85.43061003,
            72.45526212,  87.34681775,  87.69911217, 103.02831489,
            75.28598596,  67.17806893,  92.41274447, 101.06662611,
            87.70013935,  70.73980645,  46.40368207,  50.17947092,
            61.75618542,  90.26191397,  78.63968639,  70.84550744,
            88.91826581, 103.91474733,  66.3064638 ,  79.49726264,
            70.81087439,  83.90130623,  87.58555972,  59.95462521])
```

## Numpy y la estadística

```python
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_arreglo, color="grey", bins=50)
```

```sh
    (array[2., 0., 0., 0., 1., 2., 2., 0., 2., 0., 0., 1., 2., 2., 1., 4., 3.,
            4., 2., 7., 2., 2., 5., 4., 2., 4., 3., 2., 1., 5., 3., 0., 3., 2.,
            1., 0., 0., 1., 3., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1.]),
     array[ 38.69307086,  40.37038529,  42.04769973,  43.72501417,
             45.4023286 ,  47.07964304,  48.75695748,  50.43427191,
             52.11158635,  53.78890079,  55.46621523,  57.14352966,
             58.8208441 ,  60.49815854,  62.17547297,  63.85278741,
             65.53010185,  67.20741628,  68.88473072,  70.56204516,
             72.23935959,  73.91667403,  75.59398847,  77.27130291,
             78.94861734,  80.62593178,  82.30324622,  83.98056065,
             85.65787509,  87.33518953,  89.01250396,  90.6898184 ,
             92.36713284,  94.04444727,  95.72176171,  97.39907615,
             99.07639058, 100.75370502, 102.43101946, 104.1083339 ,
            105.78564833, 107.46296277, 109.14027721, 110.81759164,
            112.49490608, 114.17222052, 115.84953495, 117.52684939,
            119.20416383, 120.88147826, 122.5587927 ]),
     <a list of 50 Patch objects>)
```

### Matrices en numpy

```python

cuatro_x_cuatro_matriz = np.matrix(np.ones((4,4), dtype=float))
```

```python
cuatro_x_cuatro_matriz
```

```sh
matrix([[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]])
```

```python
np.asarray(cuatro_x_cuatro_matriz)[2] = 2
cuatro_x_cuatro_matriz
```

```sh

matrix([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [2., 2., 2., 2.],
            [1., 1., 1., 1.]])
```

### Numpy numpy.arange()

#### ¿Qué es arange(organizar)?

A veces, desea crear valores que estén espaciados uniformemente dentro de un intervalo definido. Por ejemplo, desea crear valores del 1 al 10; puedes usar función numpy.arange() 

```python
# creando una lista usando el rango (inicio, parada, salto)
lista = range(0, 11, 2)
lista
```

```python
range(0, 11, 2)
```

```python
for l in lista:
    print(l)
```

```sh 0
    2
    4
    6
    8
    10
```

```python
# Similar a rango arange numpy.arange(empezar, parar, salto)
todos_los_numeros = np.arange(0, 20, 1)
todos_los_numeros
```

```sh
array[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19])
```

```python
numeros_naturales = np.arange(1, 20, 1)
numeros_naturales
```

```python
numeros_impares = np.arange(1, 20, 2)
numeros_impares
```

```sh
    array[ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])
```

```python
numeros_pares = np.arange(2, 20, 2)
numeros_pares
```

```sh
    array[ 2,  4,  6,  8, 10, 12, 14, 16, 18])
```

### Crear secuencia de números usando linspace

```python
# numpy.linspace()
# Por ejemplo, se puede usar para crear 10 valores del 1 al 5 espaciados uniformemente.
np.linspace(1.0, 5.0, num=10)
```

```sh
    array[1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
           3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
```

```python
# No incluir el último valor en el intervalo
np.linspace(1.0, 5.0, num=5, endpoint=False)
```

```
array[1. , 1.8, 2.6, 3.4, 4.2])
```

```python
# LogSpace
# LogSpace devuelve números espaciados pares en una escala logarítmica. Logspace tiene los mismos parámetros que np.linspace.

# Syntax:

# numpy.logspace(inicio, parada, número, punto final)

np.logspace(2, 4.0, num=4)
```

```sh

array[  100.        ,   464.15888336,  2154.43469003, 10000.        ])
```

```python
# para ver el tamaño de un arreglo
x = np.array[1,2,3], dtype=np.complex128)
```

```python
x
```

```sh
    array[1.+0.j, 2.+0.j, 3.+0.j])
```

```python
x.itemsize
```

```sh
16
```

```python
# indexando y rebanando arreglos numpy in Python
np_list = np.array[(1,2,3), (4,5,6)])
np_list

```

```sh
    array[[1, 2, 3],
           [4, 5, 6]])
```

```python
print('primera fila: ', np_list[0])
print('segunda fila: ', np_list[1])

```

```sh

    primera fila:  [1 2 3]
    segunda fila:  [4 5 6]
```

```p
print('Primera columna: ', np_list[:,0])
print('Segunda columna: ', np_list[:,1])
print('Tercera columna: ', np_list[:,2])

```

```sh
    Primera columna:  [1 4]
    Segunda columna:  [2 5]
    Tercera columna:  [3 6]
```

### Funciones estadísticas NumPy con ejemplo

NumPy tiene funciones estadísticas bastante útiles para encontrar mínimo, máximo, media, mediana, percentil, desviación estándar y varianza, etc. de los elementos dados en el arreglo.

Numpy está equipado con la función estadística robusta que se detalla a continuación:

- Numpy Functions
  - Min np.min()
  - Max np.max()
  - Mean np.mean()
  - Median np.median()
  - Varience
  - Percentile
  - Standard deviation np.std()

```python
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, media, mediana, desviación estandar
print('min: ', arreglo_dos_dimensiones.min())
print('max: ', arreglo_dos_dimensiones.max())
print('mean: ',arreglo_dos_dimensiones.mean())
#print('median: ', arreglo_dos_dimensiones.median())
print('st: ', arreglo_dos_dimensiones.std())
```

    min:  1
    max:  55
    mean:  14.777777777777779
    sd:  18.913709183069525

```python
min:  1
max:  55
mean:  14.777777777777779
sd:  18.913709183069525
```

```python
print(arreglo_dos_dimensiones)
print('Columna con mínimos: ', np.amin(arreglo_dos_dimensiones,axis=0))
print('Columna con maximos: ', np.amax(arreglo_dos_dimensiones,axis=0))
print('=== Filas ==')
print('Fila con minimos: ', np.amin(arreglo_dos_dimensiones,axis=1))
print('Fila con máximos: ', np.amax(arreglo_dos_dimensiones,axis=1))
```

    [[ 1  2  3]
     [ 4 55 44]
     [ 7  8  9]]
    Columna con minimos:  [1 2 3]
    Columna con maximos:  [ 7 55 44]
    === Row ==
    Fila con minimos:  [1 4 7]
    Fila con máximos:  [ 3 55  9]

### ¿Cómo crear secuencias repetitivas?

```python
a = [1,2,3]

# Repetir todo 'a' dos veces
print('Teja:   ', np.tile(a, 2))

# Repita cada elemento de 'a' dos veces
print('Repetir: ', np.repeat(a, 2))

```

    Tile:    [1 2 3 1 2 3]
    Repeat:  [1 1 2 2 3 3]

### ¿Cómo generar números aleatorios?

```python
# Un número aleatorio entre 0 y 1
un_numero_aleatorio = np.random.random()
un_aleatorio_en = np.random
print(un_numero_aleatorio)
```

    0.6149403282678213

```python
0.4763968133790438
```

    0.4763968133790438

```python
# Números aleatorios entre 0 y 1 de forma 2,3
r = np.random.random(size=[2,3])
print(r)
```

    [[0.13031737 0.4429537  0.1129527 ]
     [0.76811539 0.88256594 0.6754075 ]]

```python
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
```

    ['u' 'o' 'o' 'i' 'e' 'e' 'u' 'o' 'u' 'a']

```python
['i' 'u' 'e' 'o' 'a' 'i' 'e' 'u' 'o' 'i']
```

    ['iueoaieuoi']

```python
## Números aleatorios entre 0 y 1 de forma (2,2)
rand = np.random.rand(2,2)
rand
```

    array[[0.97992598, 0.79642484],
           [0.65263629, 0.55763145]])

```python
rand2 = np.random.randn(2,2)
rand2

```

    array[[ 1.65593322, -0.52326621],
           [ 0.39071179, -2.03649407]])

```python
# Números enteros aleatorios entre 0 y 10 de forma (5,3)
rand_int = np.random.randint(0, 10, size=[5,3])
rand_int
```

    array[[0, 7, 5],
           [4, 1, 4],
           [3, 5, 3],
           [4, 3, 8],
           [4, 6, 7]])

```python
from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # media, desviación estándar, número de muestras
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))
```

```sh

    min:  3.557811005458804
    max:  6.876317743643499
    mean:  5.035832048106663
    median:  5.020161980441937
    mode:  ModeResult(mode=array[3.55781101]), count=array[1]))
    sd:  0.489682424165213

```

```python
plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()
```


### numpy.dot(): Dot Product in Python using Numpy

Dot Product en Numpy es una poderosa biblioteca para el cálculo de matrices. Por ejemplo, puede calcular el producto escalar con np.dot

```python
#Sintaxis
numpy.dot(x, y, out=None)
```

### Álgebra lineal

1. Dot Product

```python
## Álgebra lineal
### Producto punto de dos arreglos
f = np.array[1,2,3])
g = np.array[4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23
```

### NumPy multiplicación de matrices usando np.matmul()

```python
### Matmul: producto entre dos matrices
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)
```

```sh
    array[[19, 22],
           [43, 50]])

```

```python
np.linalg.det(i)
```

```python
Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1
```

```python
new_list = [ x + 2 for x in range(0, 11)]
```

```python
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

```python
np_arr = np.arrayrange(0, 11))
np_arr + 2
```

Usamos ecuaciones lineales para cantidades que tienen una relación lineal. Veamos el ejemplo a continuación:

```python
temp = np.array[1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)
```

```python
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
```

Para dibujar la distribución normal de Gauss usando numpy. Como puede ver a continuación, el numpy puede generar números aleatorios. Para crear una muestra aleatoria, necesitamos la media (mu), sigma (desviación estándar), número de puntos de datos.

```python
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()
```
