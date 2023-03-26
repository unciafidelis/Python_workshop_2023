## Ciclos

La vida está llena de rutinas. En programación también hacemos muchas tareas repetitivas. Para manejar tareas repetitivas, los lenguajes de programación usan ciclos. El lenguaje de programación Python también proporciona los siguientes tipos de dos ciclos:

1. ciclo while
2. ciclo for

### Ciclo while 

Usamos la palabra reservada _while_ para hacer un ciclo while. Se utiliza para ejecutar un bloque de declaraciones repetidamente hasta que se cumpla una condición dada. Cuando la condición se vuelve falsa, las líneas de código después del ciclo continuarán ejecutándose.

```python
  # sintaxis
while condicion:
    #el código va aquí
```

**Ejemplo:**

```python
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1
#prints from 0 to 4
```

En el ciclo while anterior, la condición se vuelve falsa cuando el conteo es 5. Ahí es cuando el ciclo se detiene.
Si estamos interesados ​​en ejecutar un bloque de código una vez que la condición ya no sea cierta, podemos usar _else_.

```python
  # sintaxis
while condicion:
    #el código va aquí
else:
    #el código va aquí
```

**Ejemplo:**

```python
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1
else:
    print(contador)
```

La condición del ciclo anterior será falsa cuando el conteo sea 5 y el ciclo se detenga y la ejecución inicie la instrucción else. Como resultado se imprimirá 5.


### Break y Continue - Parte 1

- Break: Usamos break cuando queremos salir o detener el ciclo.

```python
# sintaxis
while condicion:
    el código va aquí
    if otra_condicion:
        break
```

**Ejemplo:**

```python
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1
    if contador == 3:
        break
```

El ciclo while anterior solo imprime 0, 1, 2, pero cuando llega a 3 se detiene.

- Continue: Con la instrucción continuar podemos omitir la iteración actual y continuar con la siguiente:

```python
  # sintaxis
while condicion:
    #el código va aquí
    if otra_condicion:
        continue
```

**Ejemplo:**

```python
contador = 0
while contador < 5:
    if contador == 3:
        continue
    print(contador)
    contador = contador + 1
```

El ciclo while anterior solo imprime 0, 1, 2 y 4 (se salta 3).

### Ciclo for

Una palabra clave _for_ se usa para hacer un for ciclo, similar a otros lenguajes de programación, pero con algunas diferencias de sintaxis. ciclo se usa para iterar sobre una secuencia (es decir, una lista, una tupla, un diccionario, un conjunto o una cadena).

- Ciclo for con lista

```python
# sintaxis
for iterador in lista:
    #el código va aquí
```

**Ejemplo:**

```python
numeros = [0, 1, 2, 3, 4, 5]
for numero in numeros: # el número es un nombre temporal para referirse a los elementos de la lista, válido solo dentro de este ciclo
    print(numero)       # los números se imprimirán línea por línea, del 0 al 5
```

- Ciclo for con cadenas

```python
# sintaxis
for iterador in cadena:
    el código va aquí
```

**Ejemplo:**

```python
lenguaje = 'Python'
for letra in lenguaje:
    print(letra)


for i in range(len(lenguaje)):
    print(lenguaje[i])
```

- Ciclo for con tuplas

```python
# sintaxis
for iterador in tupla:
    #el código va aquí
```

**Ejemplo:**

```python
numeros = (0, 1, 2, 3, 4, 5)
for numero in numeros:
    print(numero)
```

- Ciclo for con diccionarios
  recorrer un diccionario te da la clave del diccionario.

```python
  # sintaxis
for iterador in diccionario:
    #el código va aquí
```

**Ejemplo:**

```python
persona = {
    'nombre':'Alejandro',
    'apellido':'Morgan',
    'edad':250,
    'pais':'México',
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for llave in persona:
    print(llave)

for llave, valor in persona.items():
    print(llave, valor) # de esta manera obtenemos las claves y los valores impresos
```

- ciclos en conjuntos

```python
# sintaxis
for iterador in st:
    #el código va aquí
```

**Ejemplo:**

```python
empresas_tec = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for empresa in empresas_tec:
    print(empresa)
```

### Break y Continue - Parte 2

Breve recordatorio:
_Break_: Usamos break cuando queremos detener nuestro ciclo antes de que se complete.

```python
# sintaxis
for iterador in secuencia:
    #el código va aquí
    if condicion:
        break
```

**Ejemplo:**

```python
numeros = (0,1,2,3,4,5)
for numero in numeros:
    print(numero)
    if numero == 3:
        break
```

En el ejemplo anterior, el ciclo se detiene cuando llega a 3.

Continue: Usamos continue cuando nos gusta saltarnos algunos de los pasos en la iteración del ciclo.

```python
  # sintaxis
for iterador in secuencia:
    #el código va aquí
    if condicion:
        continue
```

**Ejemplo:**

```python
numeros = (0,1,2,3,4,5)
for numero in numeros:
    print(numero)
    if numero == 3:
        continue
    print('El siguiente número debería de ser ', numero + 1) if numero != 5 else print("final del ciclo") # para las condiciones abreviadas se necesitan declaraciones if y else
print('fuera del ciclo')
```

En el ejemplo anterior, si el número es igual a 3, el paso *después* de la condición (pero dentro del ciclo) se omite y la ejecución del ciclo continúa si quedan iteraciones.

### La función Range

La función _range()_ se usa para listar numeros. El _range(inicio, final, salto)_ toma tres parámetros: inicio, finalización e incremento. De forma predeterminada, comienza desde 0 y el incremento es 1. La secuencia de rango necesita al menos 1 argumento (final).

Creando secuencias usando range

```python
lista = list(range(11)) 
print(lista) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 argumentos indican el inicio y el final de la secuencia, el paso se establece en el valor predeterminado 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lista = list(range(0,11,2))
print(lista) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
```

```python
# sintaxis
for iterador in range(inicio, final, salto):
```

**Ejemplo:**

```python
for numero in range(11):
    print(numero)   # imprime del 0 al 10, sin incluir el 11
```

### Ciclos for anidados

Podemos escribir ciclos dentro de un ciclo.

```python
# sintaxis
for x in y:
    for t in x:
        print(t)
```

**Ejemplo:**

```python
persona = {
    'nombre': 'Alejandro',
    'apellido': 'Morgan',
    'edad': 250,
    'pais': 'México',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for llave in persona:
    if llave == 'skills':
        for skill in persona['skills']:
            print(skill)
```

### for else

Si queremos ejecutar algún mensaje cuando termine el ciclo, usamos else.

```python
# sintaxis
for iterador in range(inicio, final, salto):
    #Haz algo
else:
    print('El ciclo terminó')
```

**Ejemplo:**

```python
for numero in range(11):
    print(numero)   # imprime del 0 al 10, sin incluir el 11
else:
    print('El ciclo para en', numero)
```
