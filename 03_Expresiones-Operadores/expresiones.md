# Expresiones y Operadores

## Expresiones.

Las expresiones son combinaciones de constantes, variables, símbolos de operación, paréntesis y nombres de funciones especiales.

Una expresión consta de operandos y operadores. Según sea el tipo de objetos que manipulan, las expresiones se clasifican en: 

* aritméticas 
* relacionales
* lógicas
* carácter

El resultado de la expresión aritmética es de tipo numérico; el resultado de la expresión relacional y de una expresión lógica es de tipo lógico; el resultado de una expresión carácter es de tipo carácter.

Las expresiones aritméticas son análogas a las fórmulas matemáticas. Las variables y constantes son numéricas (real o entera) y las operaciones son las aritméticas.

* `+` - Este es el operador de suma y realiza la función de adicionar un operando al otro. 
* `-` - Este es el operador de resta y realiza la función de sustraer un operando de otro.
* `*` - Este es el operador de multiplicación y realiza la función de aumentar un operando en función de otro operando.
* `/` - Este es el operador de división y realiza la función de seccionar un operando en función de otro operando.
* `%` - Este es el operador de módulo y realiza la función de regresar el residuo de una división.
* `**` - Este es el operador de exponencial y permite obtener la potencia de un operando en función de otro operando.

A continuación se presentan algunos ejemplos de los operadores en código Python.

### Operador +.

```python
a = 7 + 3
print(a)
a = 5
b = 3
c = a + b
print(c)
print(3+4)
```


### Operador -.

```python
a = 6 - 2
print(a)
a = 5
b = 3
c = a - b
print(c)
print(2-6)
```


### Operador *.

```python
a = 3 * 4
print(a)
a = 6
b = 3
c = a * b
print(c)
print(5*7)
```


### Operador /.

```python
a = 6 / 2
print(a)
a = 5
b = 3
c = a / b
print(c)
print(10/3)
```

### Operador %.

```python
a = 8 % 4
print(a)
a = 9
b = 2
c = a % b
print(c)
print(6%3)
```

### Operador **.

```python
a = 3 ** 3
print(a)
a = 2
b = 4
c = a ** b
print(c)
print(4**3)
```

Expresiones relacionales

* `<` - Este es el operador de menor que, y se utiliza en las expresiones relacionales para saber si un operando es menor a otro operando.
* `>` - Este es el operador de mayor que, y se utiliza en las expresiones relacionales para saber si un operando es mayor a otro operando.
* `==` - Este es el operador de igual que, y se utiliza en las expresiones relacionales para saber si un operando es igual a otro operando.
* `!=` - Este es el operador desigual que, y se utiliza en las expresiones relacionales para saber si un operando es diferente a otro operando.
* `<=` - Este es el operador de menor igual que, y se utiliza en las expresiones relacionales para saber si un operando es menor o igual a otro operando.
* `>=` Este es el operador de mayor igual que, y se utiliza en las expresiones relacionales para saber si un operando es mayor igual a otro operando.

NOTA: Como resultado de la aplicación de las expresiones relacionales, se obtendrá como resultado una salida booleana, es decir `TRUE` o `FALSE`.

A continuación se presentan algunos ejemplos de las expresiones relacionales en código Python.

### Operador <.

```python
a = 3 < 3
print(a)
a = 2
b = 4
c = a < b
print(c)
print(4<3)
```

### Operador >.

```python
a = 4 > 2
print(a)
a = 5
b = 7
c = a > b
print(c)
print(9>2)
```

### Operador ==.

```python
a = 5 == 5
print(a)
a = 6
b = 9
c = a == b
print(c)
print(6==2)
```

### Operador !=.

```python
a = 4 != 2
print(a)
a = 5
b = 3
c = a != b
print(c)
print(8!=8)
```

### Operador <=.


```python
a = 5 <= 3
print(a)
x = 7
y = 5
z = x <= y
print(z)
print(9<=4)
```

### Operador >=.

```python
a = 2 >= 8
print(a)
a = 3
b = 4
c = a >= b
print(c)
print(7>=3)
```


## Expresiones lógicas.


* `not` - Este es el operador lógico para realizar una negación, si el operando no se encuentra en el otro operando, la expresión se cumple y resulta en True, caso contrario, si la expresión no se cumple el resultado es False.
* `and` - Este es el operador lógico para realizar una conjugación, si cualquiera de los operandos presentes no se cumple en la expresión lógica, esta resulta en False, caso contrario, si toda la expresión lógica de conjugación se cumple el resultado es True.
* `or` - Este es el operador lógico para realizar una conjugación, si cualquiera de los operandos presentes no se cumple en la expresión lógica, esta resulta en False, caso contrario, si toda la expresión lógica de conjugación se cumple el resultado es True.

### Operador and.

```python
print(4-1==3 and 5>6)
print(6+7 > 11 and 3==3)
```

### Operador or.

```python
print(4-1==3 or 5>6)
print(6+7 > 11 or 3==3)
```

### Operador not.

```python
print(not 5>6)
print(not 5>4)
```

## Expresiones de carácter

A diferencia de las demás expresiones no existe un operador estático sino una búsqueda de secuencias, números o caracteres dentro de una variable.

Estas expresiones de búsqueda comúnmente llamadas expresiones regulares, sirven para captar ciertos elementos o patrones dentro de un valor.

Ejemplo:

```python
import re
frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+' #Esta es una expresión regular
re.findall(patron, frase)
```





