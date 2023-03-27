## Funciones

Hasta ahora hemos visto muchas funciones integradas de Python. En esta sección, nos centraremos en las funciones personalizadas. ¿Qué es una función? Antes de comenzar a hacer funciones, aprendamos qué es una función y por qué las necesitamos.

### Definiendo una función

Una función es un bloque reutilizable de código o declaraciones de programación diseñadas para realizar una determinada tarea. Para definir o declarar una función, Python proporciona la palabra clave _def_. La siguiente es la sintaxis para definir una función. El bloque de función de código se ejecuta solo si se llama o invoca la función.

### Declarar y llamar a una función

Cuando hacemos una función, la llamamos declarar una función. Cuando comenzamos a usarlo, lo llamamos *llamar* o *invocar* una función. La función se puede declarar con o sin parámetros.

```python
# sintaxis
# Declarar la función
def nombre_de_funcion():
    #code
# Llamar la función
nombre_de_funcion()
```

### función sin parámetros

Las funciones pueden ser declaradas sin parámetros.

**Ejemplo:**

```python
def generar_nombre_completo ():
    nombre = 'Alejandro'
    apellido = 'Morgan'
    espacio = ' '
    nombre_completo = nombre + espacio + apellido
    print(nombre_completo)
generar_nombre_completo () # Llamar la función

def agregar_dos_numeros ():
    numero_uno = 2
    numero_dos = 3
    total = numero_uno + numero_dos
    print(total)
agregar_dos_numeros()
```

### Funciones que regresan un valor - Parte 1

Las funciones también puede devolver valores, si una función no tiene una declaración de retorno, el valor de la función es Ninguno. Reescribamos las funciones anteriores usando return. De ahora en adelante, obtenemos un valor de una función cuando la llamamos y la imprimimos.

```python
def generar_nombre_completo ():
    nombre = 'Alejandro'
    apellido = 'Morgan'
    espacio = ' '
    nombre_completo = nombre + espacio + apellido
    return nombre_completo
print(generar_nombre_completo())

def agregar_dos_numeros ():
    numero_uno = 2
    numero_dos = 3
    total = numero_uno + numero_dos
    return total
print(agregar_dos_numeros())
```

### Función con Parámetros

En una función podemos pasar diferentes tipos de datos (número, cadena, booleano, lista, tupla, diccionario o conjunto) como parámetro

- Parámetro único: si nuestra función toma un parámetro, debemos llamar a nuestra función con un argumentoo

```python
  # sintaxis
  # Declarar la función
  def nombre_de_funcion(parametro):
    codigo
  # Llamar la función
  print(nombre_de_funcion(argumento))
```

**Ejemplo:**

```python
def saludo (nombre):
    mensaje = nombre + ', bienvenido al taller de python!'
    return mensaje

print(saludo('Alejandro'))

def agrega_diez(numero):
    diez = 10
    return numero + diez
print(agrega_diez(90))

def numero_al_cuadrado(x):
    return x * x
print(numero_al_cuadrado(2))

def area_del_circulo (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_del_circulo(10))

def suma_de_numeros(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(suma_de_numeros(10)) # 55
print(suma_de_numeros(100)) # 5050
```

- Dos parametros: Una funcion puede tener o no parametro o parametros. Una función también puede tener dos o más parámetros. Si nuestra funcion toma parametros deberiamos llamarla con argumentos. Comprobemos una función con dos parámetros:

```python
  # sintaxis
  # Declarar la función
  def nombre_de_funcion(para1, para2):
    codigo
  # Llamar la función
  print(nombre_de_funcion(arg1, arg2))
```

**Ejemplo:**

```python
def generar_nombre_completo (nombre, apellido):
    espacio = ' '
      nombre_completo = nombre + espacio + apellido
      return nombre_completo
print('Nombre completo: ', generar_nombre_completo('Alejandro','Morgan'))

def suma_dos_numeros (numero_uno, numero_dos):
    suma = numero_uno + numero_dos
    return suma
print('Suma de dos numeros: ', suma_dos_numeros(1, 9))

def calcular_edad (año_actual, año_nacimiento):
    edad = año_actual - año_nacimiento
    return edad

print('Edad: ', calcular_edad(2021, 1819))

def peso_de_objeto (masa, gavedad):
    peso = str(masa * gavedad)+ ' N' # el valor tiene que ser cambiado a una cadena primero
    return peso
print('Peso de un objeto en Newtons: ', peso_de_objeto(100, 9.81))
```

### Pasar argumentos con clave y valor

Si pasamos los argumentos con clave y valor, el orden de los argumentos no importa.

```python
# sintaxis
# Declarar la función
def nombre_de_funcion(para1, para2):
    codigo
# Llamar la función
print(nombre_de_funcion(para1 = 'John', para2 = 'Doe')) # aquí no importa el orden de los argumentos
```

**Ejemplo:**

```python
def imprime_nombre_completo(nombre, apellido):
    espacio = ' '
    nombre_completo = nombre  + espacio + apellido
    print(nombre_completo)
print(imprime_nombre_completo(nombre = 'Alejandro', apellido = 'Morgan'))

def agregar_dos_numeros (numero1, numero2):
    total = numero1 + numero2
    print(total)
print(agregar_dos_numeros(numero2 = 3, numero1 = 2)) # El orden no importa
```

### Funciones que regresan un valor - Parte 2

Si no devolvemos un valor con una función, entonces nuestra función devuelve _None_ por defecto. Para devolver un valor con una función usamos la palabra clave _return_ seguida de la variable que estamos devolviendo. Podemos devolver cualquier tipo de tipo de datos desde una función.

- Devolviendo una cadena:
**Ejemplo:**

```python
def print_nombre(nombre):
    return nombre
print_nombre('Alejandro') # Alejandro

def imprimir_nombre_completo(nombre, apellido):
    espacio = ' '
    nombre_completo = nombre  + espacio + apellido
    return nombre_completo
imprimir_nombre_completo(nombre='Alejandro', apellido='Morgan')
```

- Regresando un numero:

**Ejemplo:**

```python
def agregar_dos_numeros (numero1, numero2):
    total = numero1 + numero2
    return total
print(agregar_dos_numeros(2, 3))

def calcular_edad (año_actual, año_nacimiento):
    edad = año_actual - año_nacimiento
    return edad
print('edad: ', calcular_edad(2019, 1819))
```

- Regresando un buleano:
  **Ejemplo:**

```python
def es_igual (n):
    if n % 2 == 0:
        print('igual')
        return True    # return detiene la ejecución de la función, similar a break 
    return False
print(es_igual(10)) # True
print(es_igual(7)) # False
```

- Regresando una lista:
  **Ejemplo:**

```python
def encuentra_numeros_iguales(n):
    iguales = []
    for i in range(n + 1):
        if i % 2 == 0:
            iguales.append(i)
    return iguales
print(encuentra_numeros_iguales(10))
```

### Funciones con parametros por defecto

A veces pasamos valores predeterminados a parámetros, cuando invocamos la función. Si no pasamos argumentos al llamar a la función, se utilizarán sus valores por defecto.

```python
# sintaxis
# Declarar la función
def nombre_de_funcion(parametro = valor):
    codigo
# Llamar la función
nombre_de_funcion()
nombre_de_funcion(arg)
```

**Ejemplo:**

```python
def saludo (nombre = 'Juan'):
    mensaje = nombre + ', bienvenido a python!'
    return mensaje
print(saludo())
print(saludo('Alejandro'))

def generar_nombre_completo (nombre = 'Alejandro', apellido = 'Morgan'):
    espacio = ' '
    nombre_completo = nombre + espacio + apellido
    return nombre_completo

print(generar_nombre_completo())
print(generar_nombre_completo('David','Martinez'))

def calcular_edad (año_nacimiento,año_actual = 2021):
    edad = año_actual - año_nacimiento
    return edad
print('edad: ', calcular_edad(1821))

def peso_de_objeto (masa, gavedad = 9.81):
    peso = str(masa * gavedad)+ ' N' # el valor tiene que ser cambiado a cadena primero
    return peso
print('peso de un objeto en newtons: ', peso_de_objeto(100)) # 9.81 - promedio de gavedad en la superficie de la Tierra
print('peso de un objeto en newtons: ', peso_de_objeto(100, 1.62)) # gravedad en la superficie de la Luna
```

### Número arbitrario de argumentos

Si no sabemos el número de argumentos que le pasamos a nuestra función, podemos crear una función que pueda tomar un número arbitrario de argumentos agregando \* antes del parámetro nombre.

```python
# sintaxis
# Declarar la función
def nombre_de_funcion(*args):
    codigo
# Llamar la función
nombre_de_funcion(param1, param2, param3,..)
```

**Ejemplo:**

```python
def suma_todos_los_numeros(*numeros):
    total = 0
    for numero in numeros:
        total += numero     # igual que total = total + num
    return total
print(suma_todos_los_numeros(2, 3, 5)) # 10
```

### Número predeterminado y arbitrario de parámetros en funciones

```python
def generar_grupos (equipo,*args):
    print(equipo)
    for i in args:
        print(i)
print(generar_grupos('Equipo-1','Alejandro','Brook','David','Eyob'))
```

### Función como parametro de otra función

```python
#Puedes pasar funciones como parametros
def numero_al_cuadrado (n):
    return n * n
def hacer_algo(f, x):
    return f(x)
print(hacer_algo(numero_al_cuadrado, 3)) # 27
```