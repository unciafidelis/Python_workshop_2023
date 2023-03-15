# Subrutinas

Una función o subrutina es un conjunto de instrucciones de programa que realizan una tarea, encapsuladas como una unidad. Toda función tiene un nombre, y puede ser llamada o invocada durante la ejecución del programa.

# Palabras reservadas.

Las palabras reservadas (keywords) en son palabras que no podemos utilizar para nombrar variables, ni funciones, ni ningún otro identificador, ya que las reserva internamente el lenguaje de programación para su funcionamiento.

“Por ejemplo, no podemos llamar a una función o una variable True, y si intentamos hacerlo, tendremos un SyntaxError. Esto es lógico ya que Python usa internamente True para representar el tipo booleano.”

En Python para poder acceder a las palabras reservadas (keywords), se teclea `help()`. Posteriormente, dentro de la ayuda, tecleamos keywords para ver el listado:


Otra manera de acceder a la lista de keywords de Python por código es de la siguiente manera.

```python
import keyword
print(keyword.kwlist)

#Respuesta
# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']
```


A continuación, vamos a ver rápidamente qué hace cada una de las palabras reservadas más comunes:

`False` – Valor booleano, resultado de operaciones de comparación u operaciones lógicas en Python.

`None` – Representa a un valor nulo.

`True` – Valor booleano, igual que false, resultado de operaciones de comparación u operaciones lógicas en Python.

`__peg_parser__` – Llamado huevo de pascua, relacionado con el lanzamiento del nuevo analizador PEG no está definido aún.

`and` – Operador lógico.

`as` – Se utiliza para crear un alias al importar un módulo.

`assert` – Se utiliza con fines de depuración.

`async` – Proporcionada por la biblioteca `asyncio` en Python. Se utiliza para escribir código concurrente en Python.

`await` – Proporcionada por la biblioteca `asyncio` en Python. Se utiliza para escribir código concurrente en Python.

`break` – Se utiliza en el interior de los bucles for y while para alterar su comportamiento normal.

`class` – Se usa para definir una nueva clase definida por el usuario.

`continue` – Se utiliza en el interior de los bucles for y while para alterar su comportamiento normal.

`def` – se usa para definir una función definida por el usuario.

`del` – Para eliminar un objeto.

`elif` – Se usa en declaraciones condicionales, igual `else` e `if`.

`else` – Se usa en declaraciones condicionales, igual `elif` e `if`.

`except` – Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que `raise` y `try`.

`finally` – Su uso garantiza que el bloque de código dentro de él se ejecute incluso si hay una excepción no controlada.

`for` – Utilizado para hacer bucles. Generalmente lo usamos cuando sabemos la cantidad de veces que queremos que se ejecute ese bucle.

`from` – Para importar partes específicas de un módulo.

`global` – Para declarar una variable global.

`if` – Se usa en declaraciones condicionales, igual `else` y `elif`.

`import` – Para importar un módulo.

`in` – Para comprobar si un valor está presente en una lista, tupla, etc. Devuelve True si el valor está presente, de lo contrario devuelve False.

`is` – Se usa para probar si las dos variables se refieren al mismo objeto. Devuelve True si los objetos son idénticos y False si no.

`lambda` – Para crear una función anónima.

`nonlocal` – Para declarar una variable no local.

`not` – Operador lógico.

`or` – Operador lógico.

`pass` – Es una declaración nula en Python. No pasa nada cuando se ejecuta. Se utiliza como marcador de posición.

`raise` – Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que `except` y `try`.

`return` – Se usa dentro de una función para salir y devolver un valor. 

`try` – Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que `raise` y ‘except.

`while` – Se usa para realizar bucles.

`with` – Se usa para simplificar el manejo de excepciones.

`yield` – Se usa dentro de una función al igual que `return`, salvo que `yield` devuelve un generador.
