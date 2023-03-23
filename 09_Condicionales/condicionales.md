## condiciónales

De forma predeterminada, las declaraciones en el script de Python se ejecutan secuencialmente de arriba a abajo. Si la lógica de procesamiento lo requiere, el flujo secuencial de ejecución se puede alterar de dos formas:

- Ejecución condiciónal: se ejecutará un bloque de una o más sentencias si cierta expresión es verdadera
- Ejecución repetitiva: un bloque de una o más sentencias se ejecutará de forma repetitiva siempre que cierta expresión sea verdadera. En esta sección, cubriremos las declaraciones _if_, _else_, _elif_. Los operadores lógicos y de comparación que aprendimos en las secciones anteriores serán útiles aquí.

### if - Condición

En python y otros lenguajes de programación, la palabra clave _if_ se usa para verificar si una condición es verdadera y ejecutar el código de bloque. Recuerde la sangría después de los dos puntos.

```python
# sintaxis
if condición:
    #esta parte del código se ejecuta para condiciones verdaderas
```

**Ejemplo: 1**

```python
a = 3
if a > 0:
    print('A es un número positivo')
# A es un número positivo
```

Como puede ver en el ejemplo anterior, 3 es mayor que 0. La condición era verdadera y el código del bloque se ejecutó. Sin embargo, si la condición es falsa, no vemos el resultado. Para ver el resultado de la condición falsa, deberíamos tener otro bloque, que va a ser _else_.

### If Else

Si la condición es verdadera, se ejecutará el primer bloque, si no, se ejecutará la otra condición.

```python
# sintaxis
if condición:
    #esta parte del código se ejecuta para condiciones verdaderas
else:
    #esta parte del código se ejecuta para condiciones falsas
```

**Ejemplo: **

```python
a = 3
if a < 0:
    print('A es un número negativo')
else:
    print('A es un número positivo')
```

La condición anterior resulta falsa, por lo que se ejecutó el bloque else. ¿Qué tal si nuestra condición es más de dos? Podríamos usar _elif_.

### if elif else

En nuestra vida diaria, tomamos decisiones a diario. Tomamos decisiones no comprobando una o dos condiciones sino múltiples condiciones. Al igual que la vida, la programación también está llena de condiciones. Usamos _elif_ cuando tenemos múltiples condiciones.

```python
# sintaxis
if condición:
    #código
elif condición:
    #código
else:
    #código

```

**Ejemplo: **

```python
a = 0
if a > 0:
    print('A es un número positivo')
elif a < 0:
    print('A es un número negativo')
else:
    print('A es cero')
```

### Short Hand

```python
# sintaxis
código if condición else código
```

**Ejemplo: **

```python
a = 3
print('A es positivo') if a > 0 else print('A es negativo') # Si se cumple la primer condición, 'A es positivo' se imprime en terminal
```

### condiciones anidadas

Las condiciones pueden ser anidadas 

```python
# sintaxis
if condición:
    código
    if condición:
    código
```

**Ejemplo: **

```python
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A es un número positivo')
elif a == 0:
    print('A is zero')
else:
    print('A es un número negativo')

```

Podemos evitar escribir una condición anidada usando el operador lógico _and_.
### Condición if y el operador lógico and

```python
# sintaxis
if condición and condición:
    código
```

**Ejemplo: **

```python
a = 0
if a > 0 and a % 2 == 0:
        print('A es un número entero par positivo')
elif a > 0 and a % 2 !=  0:
     print('A es un entero')
elif a == 0:
    print('A es cero')
else:
    print('A es negativo')
```

### Condición if y el operador lógico or

```python
# sintaxis
if condición or condición:
    código
```

**Ejemplo: **

```python
usuario = 'Juan'
nivel_de_acceso = 3
if usuario == 'admin' or access_level >= 4:
        print('Acceso concedido!')
else:
    print('Acceso negado!')
```
