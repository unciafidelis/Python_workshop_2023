## Diccionarios

Un diccionario es una colección de tipos de datos no ordenados, modificables (mutables) emparejados (llave: valor).

### Creación de un diccionario

Para crear un diccionario usamos corchetes, {} o la función integrada *dict()*.

```python
# sintaxis
empty_dict = {}
# Diccionario con valores de datos
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
```

**Ejemplo:**

```python
person = {
    'nombre':'Alejandro',
    'morgan':'Morgan',
    'edad':250,
    'pais':'México',
    'habilidades':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion':{
        'calle':'Barrio x',
        'zipcode':'02220'
    }
    }
```

El diccionario anterior muestra que un valor puede ser cualquier tipo de datos: cadena, lista, tupla, conjunto o un diccionario.

### Longitud del diccionario

Comprueba el número de pares 'llave: valor' en el diccionario.

```python
# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
print(len(diccionario)) # 4
```

**Ejemplo:**

```python
person = {
    'nombre':'Alejandro',
    'morgan':'Morgan',
    'edad':250,
    'pais':'México',
    'habilidades':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion':{
        'calle':'Barrio x',
        'zipcode':'02210'
    }
    }
print(len(person)) # 6

```

### Acceso a elementos del diccionario

Podemos acceder a los elementos del Diccionario haciendo referencia a su nombre llave.

```python
# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
print(diccionario['llave1']) # valor1
print(diccionario['llave4']) # valor4
```

**Ejemplo:**

```python
person = {
    'nombre':'Alejandro',
    'morgan':'Morgan',
    'edad':250,
    'pais':'México',
    'habilidades':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion':{
        'calle':'Barrio x',
        'zipcode':'02210'
    }
    }
print(person['nombre']) # Alejandro
print(person['pais'])    # México
print(person['habilidades'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['habilidades'][0])  # JavaScript
print(person['direccion']['street']) # Space street
```

Acceder a un elemento por nombre de llave genera un error si la llave no existe. Para evitar este error primero tenemos que comprobar si existe una llave o podemos usar el método _get_. El método get devuelve None, que es un tipo de datos de objeto NoneType, si la llave no existe.

```python
person = {
    'nombre':'Alejandro',
    'morgan':'Morgan',
    'edad':250,
    'pais':'México',
    'habilidades':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion':{
        'calle':'Barrio x',
        'zipcode':'02210'
    }
}
print(person.get('nombre')) # Alejandro
print(person.get('pais'))    # México
print(person.get('habilidades')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
```

### Adición de elementos a un diccionario

Podemos agregar nuevos pares llave y valor a un diccionario

```python
# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
diccionario['llave5'] = 'valor5'
```

**Ejemplo:**

```python
person = {
    'nombre':'Alejandro',
    'morgan':'Morgan',
    'edad':250,
    'pais':'México',
    'habilidades':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion':{
        'calle':'Barrio x',
        'zipcode':'02210'
        }
}
person['job_title'] = 'Instructor'
person['habilidades'].append('HTML')
print(person)
```

### Modificación de elementos en un diccionario

Podemos modificar elementos en un diccionario.

```python
# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
diccionario['llave1'] = 'valor-uno'
```

**Ejemplo:**

```python
person = {
    'nombre':'Alejandro',
    'morgan':'Morgan',
    'edad':250,
    'pais':'México',
    'habilidades':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion':{
        'calle':'Barrio x',
        'zipcode':'02210'
    }
    }
person['nombre'] = 'Eyob'
person['edad'] = 252
```

### Comprobación de llaves en un diccionario

Usamos el operador _in_ para verificar si existe una llave en un diccionario

```python
# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
print('llave2' in diccionario) # True
print('llave5' in diccionario) # False
```

### Eliminando los pares llave y valor de un diccionario

- _pop(llave)_: elimina el ítem con la llave especificada:
- _popitem()_: elimina el último elemento
- _del_: elimina un elemento con la llave especificada

```python
# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
diccionario.pop('llave1') # remueve el item llave1 
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
diccionario.popitem() # remueve el último item 
del diccionario['llave2'] # remueve el item llave2 
```

**Ejemplo:**

```python
person = {
    'nombre':'Alejandro',
    'morgan':'Morgan',
    'edad':250,
    'pais':'México',
    'habilidades':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion':{
        'calle':'Barrio x',
        'zipcode':'02210'
    }
    }
person.pop('nombre')        # Removes the firstname item
person.popitem()                # Removes the direccion item
del person['calle']        # Removes calle: 'Barrio x'
```

El métodos _items()_ cambia un diccionario a una lista de tuplas

```python
# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
print(diccionario.items()) # dict_items([('llave1', 'valor1'), ('llave2', 'valor2'), ('llave3', 'valor3'), ('llave4', 'valor4')])
```

### Borrar un diccionario

Si no queremos los elementos en un diccionario, podemos borrarlos usando el método _clear()_

```python
# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
print(diccionario.clear()) # None
```

### Eliminación de un diccionario

Si no usamos el diccionario podemos borrarlo por completo

```python
# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
del diccionario
```

### Copiar un diccionario

Podemos copiar un diccionario usando un método _copy()_. Usando la copia podemos evitar la mutación del diccionario original.

```python
# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
diccionario_copia = diccionario.copy() # {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
```

### Obtener llaves de diccionario como una lista

El método _keys()_ nos da todas las claves de un diccionario a modo de lista.

```python
# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
llaves = diccionario.keys()
print(llaves)     # dict_llaves(['llave1', 'llave2', 'llave3', 'llave4'])
```

### Obtener valores de diccionario como una lista

El método _valors_ nos da todos los valores de un diccionario en forma de lista.

```python
# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
valors = diccionario.valors()
print(valors)     # dict_valors(['valor1', 'valor2', 'valor3', 'valor4'])
```
