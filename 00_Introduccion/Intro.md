## Introducción

Python es un lenguaje de programación de alto nivel para propósito general. Es un lenguaje de programación de código abierto, interpretado y orientado a objetos. Python fue creado por un programador holandés, Guido van Rossum. El nombre del lenguaje de programación Python se derivó de una serie de comedia británica, *Month Python's Flying Circus*. La primera versión se lanzó el 20 de febrero de 1991. 

Su última versión es Python 3, y es la que te recomendamos usar ya que las anteriores ya tienen soporte oficial.



## ¿Por qué Python?

Es un lenguaje de programación muy cercano al lenguaje humano y por eso es fácil de aprender y usar.

Python es utilizado por varias industrias y empresas (incluido Google). Se ha utilizado para desarrollar aplicaciones web, aplicaciones de escritorio, administración de sistemas y bibliotecas de machine learning. Python es un lenguaje muy aceptado en la comunidad de ciencia de datos y machine learning.

Existe una tendencia clara y seguramente el interés en Python vaya a seguir creciendo en los próximos años. Estos son los motivos por lo que ha crecido tanto y lo seguirá haciendo:

Se trata de un lenguaje fácil de aprender, con una sintaxis muy sencilla que se asemeja bastante al pseudocódigo. En otras palabras, poco código hace mucho.

Su uso no está ligado a un sector concreto. Por ejemplo el lenguaje R es útil para análisis de datos, pero no puede ser usado para desarrollo web. Python vale para todo.

Tiene una comunidad enorme, además de gran cantidad de librerías para hacer prácticamente cualquier cosa, literalmente.

Es un lenguaje multiplataforma, por lo que el mismo código es compatible en cualquier plataforma (Windows, macOS, Linux) sin hacer nada.

Por lo general se puede hacer desarrollos en Python más rápidamente que en otros lenguajes, acortando la duración de los proyectos.

##Preparación del entorno de programación

### Instalación de Python

Para ejecutar un script de python, debe primero, instalar python. Vamos a [descargar](https://www.python.org/) python. Ya con el archivo de instalación solo hay que correrlo con doble click y seguir la secuencia de instalación.

Prueba de funcionamiento de python en windows:

Una vez que Python haya completado el proceso de descarga e instalación, abre Windows **PowerShell** mediante el menú Inicio (icono de Windows de la esquina inferior izquierda). Cuando **PowerShell** esté abierto, escribe `Python --version` para confirmar que Python3 está instalado en la máquina (verás una pequeña leyenda indicando la versión de python que acabas de instalar).

Prueba de funcionamiento de python con macOS:

Abre una ventana de la Terminal en tu Mac.
coloca `python -v` para ver la versión de python instalada en tu equipo (en ocaciones no reconoce el comando `python -v`, en este caso puedes probar utilizando `python3 -v`).

### Instalación de Visual Studio Code

El shell interactivo de Python es bueno para probar pequeños scripts en secuencias de comandos, pero no es funcional para un gran proyecto. En un entorno de trabajo real, los desarrolladores usan diferentes editores de código para el desarrollo de programas. En este curso usaremos Visual Studio Code. Visual Studio Code es un editor de texto de código abierto muy popular, para utilizarlo primero hay que ir a la página oficial y [descargar Visual Studio Code](https://code.visualstudio.com/), si desean utilizar otro editor, adelante.

## Python básico

### Primeros pasos

Primero que nada debemos de entender que python permite trabajar tanto en terminal como en web a través de un sinfín de librerias, esto para mostrar los resultados de los cálculos procesados por un programa o bien un sistema completo, con distintas interfaces.

### Sintaxis de Python

Un script de Python se puede escribir en el shell interactivo de Python o en el editor de código. Un archivo de Python tiene una extensión .py.

### Sangría o identación en Python

Una sangría es un espacio en blanco en un texto. La sangría en muchos idiomas se usa para aumentar la legibilidad del código; sin embargo, Python usa la sangría para crear bloques de códigos. En otros lenguajes de programación, los corchetes se utilizan para crear bloques de códigos en lugar de sangría. Uno de los errores comunes al escribir código python es la sangría incorrecta.

```python
# Ejemplo de identación correcta en una clase

class identadoCorrecto:
  identado = True
  
# Ejemplo de identación incorrecta en una clase

class identadoIncorrecto
identado = False  
```


### Comentarios

Los comentarios son muy importantes para que el código sea más legible y para dejar comentarios en nuestro código. Python no ejecuta partes de comentarios de nuestro código.
Cualquier texto que comience con hash (#) en Python es un comentario.

**Ejemplo: comentario de una sola línea**

```python
    # Este es el primer comentario
    # Este es el segundo comentario
    # Python esta bien chido! no?
```

**Ejemplo: comentario de varias líneas**

Las comillas triples se pueden usar para comentarios de varias líneas si no están asignadas a una variable

```python
"""
Este es un comentario de varias líneas e incluye:

Este comentario,
Este tambien,
y por último,
Python es bien fácil de aprender!
"""
```

### Tipos de datos

En Python hay varios tipos de tipos de datos. Comencemos con los más comunes. Los diferentes tipos de datos se tratarán en detalle en otras secciones. Por el momento, repasemos los diferentes tipos de datos y familiaricémonos con ellos. No tienes que tener una comprensión clara ahora.

#### Número

- Entero: Números enteros (negativos, cero y positivos)
    Ejemplo:
    ... -3, -2, -1, 0, 1, 2, 3...
- Flotante: número decimal
    Ejemplo
    ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5...
- Complejo
    Ejemplo
    1 + j, 2 + 4j

#### Cadena

Una colección de uno o más caracteres bajo comillas simples o dobles. Si una cadena es más de una oración, usamos una comilla triple.

**Ejemplo:**

```python
'Espero que estés disfrutando de tu primer día de curso'
```

#### Booleanos

Un tipo de datos booleano es un valor verdadero o falso. T y F deben estar siempre en mayúsculas.

**Ejemplo:**

```python
    # ¿Está encendida la luz? - Si, está encendida
    luzEncendida = True
    
    # ¿Está encendida la luz? - No, está apagada
    luzEncendida = False
```

#### Lista

La lista de Python es una colección ordenada que permite almacenar diferentes elementos con diferentes tipos de datos. Una lista es similar a una matriz en JavaScript.

**Ejemplo:**

```python
[0, 1, 2, 3, 4, 5] # todos son del mismo tipo de datos - una lista de números
['Plátano', 'Manzana', 'Naranja', 'Mandarina'] # todos son del mismo tipo de datos - una lista de cadenas (frutas)
['Finlandia','Estonia', 'Suecia','Noruega'] # todos son del mismo tipo de datos - una lista de cadenas (países)
['Plátano', 10, False, 9.81] # Aquí hay diferentes tipos de datos dentro de la lista: cadena, entero, booleano y flotante
```

#### Diccionario

Un objeto de diccionario de Python es una colección desordenada de datos en un formato de par de valores clave.

**Ejemplo:**

```python
{
'Nombre':'Alejandro',
'Apellido':'Morgan',
'País':'méxico',
'Edad': 38,
'Habilidades':['JS', 'React', 'Node.js', 'Python']
}
```

#### Tupla

Una tupla es una colección ordenada de diferentes tipos de datos como una lista, pero las tuplas no se pueden modificar una vez que se crean. Son inmutables.

**Ejemplo:**

```python
('Alejandro', 'Pedro', 'María', 'Julia', 'Gabriela', 'Alberto') # Nombres
```

```python
('Tierra', 'Júpiter', 'Neptuno', 'Marte', 'Venus', 'Saturno', 'Urano', 'Mercurio') # planetas
```

#### Conjunto

Un conjunto es una colección de tipos de datos similar a una lista y una tupla. A diferencia de la lista y la tupla, set no es una colección ordenada de elementos. Al igual que en Matemáticas, la configuración en Python almacena solo elementos únicos.

En secciones posteriores, entraremos en detalle sobre todos y cada uno de los tipos de datos de Python.

**Ejemplo:**

```python
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # el orden no es importante en el conjunto
```

### Comprobación de tipos de datos

Para verificar el tipo de datos de ciertos datos/variables, usamos la función **type**.



### Archivos en Python

Primero abra la carpeta de su proyecto, Python_workshop_2023. Si no tiene esta carpeta, cree un nombre de carpeta llamada Python_workshop_2023 o clone este repositorio. Dentro de esta carpeta, crea un archivo llamado holaMundo.py. Dentro de este archivo vamos a desarrollar nuestro primer programa en python.

Para imprimir cadenas en la consola o hacer eco de algunos datos en la salida de la consola, use la función `print()` incorporada de Python. La función `print()` puede tomar diferentes tipos de valores como argumento(s), como cadena, entero, flotante, etc., u objeto de un tipo de clase.

```python
print('Hola mundo')
```

