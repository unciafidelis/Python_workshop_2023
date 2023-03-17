# Expresiones y Operadores

#Expresiones.
"""
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
"""

### Operador +.


a = 7 + 3
print('Operador +: a=7+3 # Resultado: ',a)                                      # 10
print('Operador +: a=7+3 # Tipo: ',type(a),'\n')                                # <class 'int'>
a = 5
b = 3
c = a + b
print('Operador +: a = 5 b = 3 c = a + b #',c)                                  # 8
print('Operador +: a = 5 b = 3 c = a + b # Tipo: ', type(c),'\n')               # <class 'int'>
print('Operador +: 3+4 # Resultado: ',3+4)                                      # 7
print('Operador +: 3+4 # Tipo: ',type(3+4),'\n')                                # <class 'int'>


### Operador -.


a = 6 - 2
print('Operador -: 6 - 2 # Resultado: ', a)                                     # 4
print('Operador -: 6 - 2 # Tipo: ', type(a),'\n')                               # <class 'int'>
a = 5
b = 3
c = a - b
print('Operador -: a = 5 b = 3 c = a - b # Resultado: ',c)                      # 2
print('Operador -: a = 5 b = 3 c = a - b # Tipo: ',type(c),'\n')                # <class 'int'>
print('Operador -: 2-6 # Resultado: ',2-6)                                      # -4
print('Operador -: 2-6 # Tipo: ',type(2-6),'\n')                                # <class 'int'>



### Operador *.


a = 3 * 4
print('Operador *: a = 3 * 4 # Resultado: ',a)                                  # 12
print('Operador *: a = 3 * 4 # Tipo: ',type(a),'\n')                            # <class 'int'>
a = 6
b = 3
c = a * b
print('Operador *: a = 6 b = 3 c = a * b  # Resultado: ',c)                     # 18
print('Operador *: a = 6 b = 3 c = a * b  # Tipo: ',type(c),'\n')               # <class 'int'>
print('Operador *: 5*7 # Resultado: ',5*7)                                      # 35
print('Operador *: 5*7 # Tipo: ',type(5*7),'\n')                                # <class 'int'>



### Operador /.


a = 6 / 2
print('Operador /: a = 6 / 2 # Resultado: ',a)                                  # 3.0
print('Operador /: a = 6 / 2 # Tipo: ',type(a),'\n')                            # <class 'float'>
a = 5
b = 3
c = a / b
print('Operador /: a = 5 b = 3 c = a / b # Resultado: ',c)                      # 1.6666666666666667
print('Operador /: a = 5 b = 3 c = a / b # Tipo: ',type(c),'\n')                # <class 'float'>
print('Operador /: 10/3 # Resultado: ',10/3)                                    # 3.3333333333333335
print('Operador /: 10/3 # Tipo: ',type(10/3),'\n')                              # <class 'float'>

### Operador %.


a = 8 % 4
print('Operador %: a = 8 % 4 # Resultado: ',a)                                  # 0
print('Operador %: a = 8 % 4 # Tipo: ',type(a),'\n')                            # <class 'int'>
a = 9
b = 2
c = a % b
print('Operador %: a = 9 b = 2 c = a % b # Resultado: ',c)                      # 1
print('Operador %: c # Tipo: ',type(c),'\n')                                    # <class 'int'>
print('Operador %: 6%3 # Resultado: ',6%3)                                      # 0
print('Operador %: 6%3 # Tipo: ',type(6%3),'\n')                                # <class 'int'>


### Operador **.


a = 3 ** 3
print('Operador **: a = 3 ** 3 # Resultado: ',a)                                # 27
print('Operador **: a = 3 ** 3 # Tipo: ',type(a),'\n')                          # <class 'int'>
a = 2 
b = 4
c = a ** b
print('Operador **: a = 2 b = 4 c = a ** b # Resultado: ',c)                    # 16
print('Operador **: a = 2 b = 4 c = a ** b # Tipo: ',type(c),'\n')              # <class 'int'>
print('Operador **: 4**3 # Resultado: ',4**3)                                   # 64
print('Operador **: 4**3 # Tipo: ',type(4**3),'\n')                             # <class 'int'>


# Expresiones relacionales
"""
* `<` - Este es el operador de menor que, y se utiliza en las expresiones relacionales para saber si un operando es menor a otro operando.
* `>` - Este es el operador de mayor que, y se utiliza en las expresiones relacionales para saber si un operando es mayor a otro operando.
* `==` - Este es el operador de igual que, y se utiliza en las expresiones relacionales para saber si un operando es igual a otro operando.
* `!=` - Este es el operador desigual que, y se utiliza en las expresiones relacionales para saber si un operando es diferente a otro operando.
* `<=` - Este es el operador de menor igual que, y se utiliza en las expresiones relacionales para saber si un operando es menor o igual a otro operando.
* `>=` Este es el operador de mayor igual que, y se utiliza en las expresiones relacionales para saber si un operando es mayor igual a otro operando.

NOTA: Como resultado de la aplicación de las expresiones relacionales, se obtendrá como resultado una salida booleana, es decir `TRUE` o `FALSE`.

A continuación se presentan algunos ejemplos de las expresiones relacionales en código Python.
"""

### Operador <.


a = 3 < 3
print('Operador <: a = 3 < 3 # Resultado: ',a)                                  # False
print('Operador <: a = 3 < 3 # Tipo: ',type(a),'\n')                            # <class 'bool'>
a = 2
b = 4
c = a < b
print('Operador <: a = 2 b = 4 c = a < b # Resultado: ',c)                      # True
print('Operador <: a = 2 b = 4 c = a < b # Tipo: ',type(c),'\n')                # <class 'bool'>
print('Operador <: 4 < 3 # Resultado: ',4<3)                                    # False
print('Operador <: 4 < 3 # Tipo: ',type(4<3),'\n')                              # <class 'bool'>


### Operador >.


a = 4 > 2
print('Operador >: a = 4 > 2 # Resultado: ',a)                                  # True
print('Operador >: a = 4 > 2 # Tipo: ',type(a),'\n')                            # <class 'bool'>
a = 5
b = 7
c = a > b
print('Operador >: a = 5 b = 7 c = a > b # Tipo: ',c)                           # False
print(type(c),'\n')                                                             # <class 'bool'>
print('Operador >: 9>2 # Resultado: ',9>2)                                      # True
print('Operador >: 9>2 # Tipo: ', type(9>2),'\n')                               # <class 'bool'>


### Operador ==.


a = 5 == 5
print('Operador ==: a = 5 == 5 # Resultado: ',a)                                # True
print('Operador ==: a = 5 == 5 # Tipo: ',type(a),'\n')                          # <class 'bool'>
a = 6
b = 9
c = a == b
print('Operador -: a = 6 b = 9 c = a == b # Resultado: ',c)                     # False
print('Operador -: a = 6 b = 9 c = a == b # Tipo: ',type(c),'\n')               # <class 'bool'>
print('Operador -: 6==2 # Resultado: ',6==2)                                    # False
print('Operador -: 6==2 # Tipo: ',type(6==2),'\n')                              # <class 'bool'>


### Operador !=.


a = 4 != 2
print('Operador !=: a = 4 != 2 # Resultado: ',a)                                # True
print('Operador !=: a = 4 != 2 # Tipo: ',type(a),'\n')                          # <class 'bool'>
a = 5
b = 3
c = a != b
print('Operador !=: a = 5 b = 3 c = a != b # Resultado: ',c)                    # True
print('Operador !=: a = 5 b = 3 c = a != b # Tipo: ',type(c),'\n')              # <class 'bool'>
print('Operador !=: 8!=8 # Resultado: ',8!=8)                                   # False
print('Operador !=: 8!=8 # Tipo: ',type(8!=8),'\n')                             # <class 'bool'>

### Operador <=.



a = 5 <= 3
print('Operador <=: a = 5 <= 3 # Resultado: ',a)                                # False
print('Operador <=: a = 5 <= 3 # Tipo: ',type(a),'\n')                          # <class 'bool'>
x = 7
y = 5
z = x <= y
print('Operador <=: x = 7 y = 5 z = x <= y # Resultado: ',z)                    # False
print('Operador <=: x = 7 y = 5 z = x <= y # Tipo: ',type(z),'\n')              # <class 'bool'>
print('Operador <=: 9<=4 # Resultado: ',9<=4)                                   # False
print('Operador <=: 9<=4 # Tipo: ',type(9<=4),'\n')                             # <class 'bool'>

### Operador >=.


a = 2 >= 8
print('Operador >=: a = 2 >= 8 # Resultado: ',a)                                # False
print('Operador >=: a = 2 >= 8 # Tipo: ',type(a),'\n')                          # <class 'bool'>
a = 3
b = 4
c = a >= b
print('Operador >=: a = 3 b = 4 c = a >= b # Resultado: ',c)                    # False
print('Operador >=: a = 3 b = 4 c = a >= b # Tipo: ',type(c),'\n')              # <class 'bool'>
print('Operador >=: 7>=3 # Resultado: ',7>=3)                                   # True
print('Operador >=: 7>=3 # Tipo: ',type(7>=3),'\n')                             # <class 'bool'>


## Expresiones lógicas.

"""
* `not` - Este es el operador lógico para realizar una negación, si el operando no se encuentra en el otro operando, la expresión se cumple y resulta en True, caso contrario, si la expresión no se cumple el resultado es False.
* `and` - Este es el operador lógico para realizar una conjugación, si cualquiera de los operandos presentes no se cumple en la expresión lógica, esta resulta en False, caso contrario, si toda la expresión lógica de conjugación se cumple el resultado es True.
* `or` - Este es el operador lógico para realizar una conjugación, si cualquiera de los operandos presentes no se cumple en la expresión lógica, esta resulta en False, caso contrario, si toda la expresión lógica de conjugación se cumple el resultado es True.
"""

### Operador and.


print('Operador and: 4-1==3 and 5>6 # Resultado: ', 4-1==3 and 5>6)             # False
print('Operador and: 4-1==3 and 5>6 # Tipo: ',type(4-1==3 and 5>6),'\n')        # <class 'bool'>
print('Operador and: 6+7 > 11 and 3==3 # Resultado: ',6+7 > 11 and 3==3)        # True
print('Operador and: 6+7 > 11 and 3==3 # Tipo: ',type(6+7 > 11 and 3==3),'\n')  # <class 'bool'>

### Operador or.


print('Operador or: 4-1==3 or 5>6 # Resultado: ',4-1==3 or 5>6)                 # True
print('Operador or: 4-1==3 or 5>6 # Tipo: ',type(4-1==3 or 5>6),'\n')           # <class 'bool'>
print('Operador or: 6+7 > 11 or 3==3 # Resultado: ',6+7 > 11 or 3==3)           # True
print('Operador or: 6+7 > 11 or 3==3 # Tipo: ',type(6+7 > 11 or 3==3),'\n')     # <class 'bool'>

### Operador not.


print('Operador not: not 5>6 # Resultado: ',not 5>6)                            # True
print('Operador not: not 5>6 # Tipo: ',type(not 5>6),'\n')                      # <class 'bool'>
print('Operador not: not 5>4 # Resultado: ',not 5>4)                            # False
print('Operador not: not 5>4 # Tipo: ',type(not 5>4),'\n')                      # <class 'bool'>

## Expresiones de carácter
"""
A diferencia de las demás expresiones no existe un operador estático sino una búsqueda de secuencias, números o caracteres dentro de una variable.

Estas expresiones de búsqueda comúnmente llamadas expresiones regulares, sirven para captar ciertos elementos o patrones dentro de un valor.

Ejemplo:
"""

import re
frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+' #Esta es una expresión regular
print('Expresión de caracter # Resultado: ', re.findall(patron, frase))         # ['2', '15', '11']
print('Expresión de caracter # Tipo: ',type(re.findall(patron, frase)),'\n')    # <class 'list'> 