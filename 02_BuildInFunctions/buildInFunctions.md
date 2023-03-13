# Build In Functions

En esta lección hablaremos sobre las funciones con las que cuenta Python, comunmente llamadas palabras reservadas, las Build In Functions hacen que todo procesamiento y funcionalidad dentro de un programa se compile y se ejecute.

### abs(x)
Devuelve el valor absoluto de un número `x`. El argumento puede ser un número entero, un número de punto flotante o un objeto que implemente `__abs__()`. Si el argumento es un número complejo, se devuelve su magnitud.

ej.

```python
print(abs(10))
print(abs(10.2))
print(abs(10j))
```

### all(iterable)
Retorna `True` si todos los elementos del iterable son verdaderos (o si el iterable está vacío). Equivalente a:

```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

### any(iterable)
Retorna `True` si algún elemento del iterable es verdadero. Si el iterable está vacío, devuelve `False`. Equivalente a:

```python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

### ascii(object)
Como `repr()`, devuelve una cadena que contiene una representación imprimible de un objeto, pero escapa los caracteres que no son ASCII en la cadena devuelta por `repr()` usando escapes \x, \u o \U.
ej.

```python
print(ascii(x))
```

### bin(x)
Convierta un número entero en una cadena binaria con el prefijo "0b". El resultado es una expresión de Python válida. Si x no es un objeto int de Python, debe definir un método `__index__()` que devuelva un número entero. 
ej.

```python
bin(2)
```
Si desea o no el prefijo “0b”, puede usar cualquiera de las siguientes formas.
ej.

```python
format(14, '#b') 
format(14, 'b')
f'{14:#b}', f'{14:b}'
```

Consulte también `format()` para obtener más información.

### class bool([x])

Devuelve un valor booleano, es decir, uno de `True` o `False`. `x` se convierte usando el procedimiento de prueba de verdad estándar. Si `x` es `False` o se omite, devuelve `False`; de lo contrario, devuelve `True`. La clase bool es una subclase de int (consulte Tipos numéricos: int, float, complex). No se puede subclasificar más. Sus únicas instancias son `False` y `True` (consulte Valores booleanos).

Cambiado en la versión 3.7: `x` ahora es un parámetro solo posicional.

### breakpoint(*args, **kws)
Esta función lo lleva al depurador en el sitio de la llamada. Específicamente, llama a `sys.breakpointhook()`, pasando `args` y `kws` directamente. De forma predeterminada, `sys.breakpointhook()` llama a `pdb.set_trace()` sin esperar argumentos. En este caso, es puramente una función de conveniencia, por lo que no tiene que importar `pdb` explícitamente ni escribir tanto código para ingresar al depurador. Sin embargo, `sys.breakpointhook()` se puede configurar para alguna otra función y `breakpoint()` la llamará automáticamente, lo que le permitirá acceder al depurador de su elección.

Genera un evento de auditoría builtins.breakpoint con argumento breakpointhook.

Nuevo en la versión 3.7.

### class bytearray([source[, encoding[, errors]]])
Devuelve una nueva matriz de bytes. La clase `bytearray` es una secuencia mutable de enteros en el rango `0 <= x < 256`. Tiene la mayoría de los métodos habituales de secuencias mutables, descritos en Tipos de secuencias mutables, así como la mayoría de los métodos que tiene el tipo bytes, consulte Bytes y Operaciones bytearray.

El parámetro de fuente opcional se puede usar para inicializar la matriz de diferentes maneras:

Si es una cadena o `String`, también debe proporcionar los parámetros de codificación (y, opcionalmente, errores); `bytearray()` luego convierte la cadena en bytes usando `str.encode()`.

Si es un número entero o `int`, la matriz tendrá ese tamaño y se inicializará con bytes nulos.

Si es un objeto que se ajusta a la interfaz del búfer, se utilizará un búfer de solo lectura del objeto para inicializar la matriz de bytes.

Si es un iterable, debe ser un iterable de enteros en el rango `0 <= x < 256`, que se utilizan como contenido inicial de la matriz.

Sin un argumento, se crea una matriz de tamaño 0.

Consulte también Tipos de secuencias binarias: `bytes`, `bytearray`, `memoryview` y `Bytearray` Objects.

###class bytes([source[, encoding[, errors]]])
Devuelve un nuevo objeto de "bytes", que es una secuencia inmutable de enteros en el rango `0 <= x < 256`. bytes es una versión inmutable de `bytearray`: tiene los mismos métodos de no mutación y el mismo comportamiento de indexación y división.

En consecuencia, los argumentos del constructor se interpretan como `bytearray()`.

Los objetos de bytes también se pueden crear con literales, consulte Literales de cadena y bytes.

Consulte también Tipos de secuencias binarias: `bytes`, `bytearray`, `memoryview`, `Bytes Objects y Bytes` and `Bytearray Operations`.

### callable(object)
Devuelva `True` si el argumento del objeto parece invocable, `False` si no. Si esto devuelve `True`, aún es posible que una llamada falle, pero si es `False`, el objeto que llama nunca tendrá éxito. Tenga en cuenta que las clases son invocables (llamar a una clase devuelve una nueva instancia); las instancias son invocables si su clase tiene un método `__call__()`.

Nuevo en la versión 3.2: esta función se eliminó por primera vez en Python 3.0 y luego se recuperó en Python 3.2.

### chr(i)
Devuelve la cadena que representa un carácter cuyo punto de código Unicode es el entero `i`. Por ejemplo, `chr(97)` devuelve la cadena 'a', mientras que `chr(8364)` devuelve la cadena '€'. Este es el inverso de `ord()`.

El rango válido para el argumento es de 0 a 1 114 111 (0x10FFFF en base 16). `ValueError` se generará si i está fuera de ese rango.

```python
print(chr(97))
print(chr(8364))
```

### @classmethod
Transforma un método en un método de clase.

Un método de clase recibe la clase como primer argumento implícito, al igual que un método de instancia recibe la instancia. Para declarar un método de clase, usa este modismo:

clase C:
```python
    @classmethod
    def f(cls, arg1, arg2):
        return cls
```
El formulario `@classmethod` es un decorador de funciones; consulte Definiciones de funciones para obtener más detalles.

Se puede llamar a un método de clase en la clase (como `C.f()`) o en una instancia (como `C().f()`). La instancia se ignora excepto por su clase. Si se llama a un método de clase para una clase derivada, el objeto de la clase derivada se pasa como el primer argumento implícito.

Los métodos de clase son diferentes a los métodos estáticos de C++ o Java. Si los quiere, consulte `staticmethod()` en esta sección. Para obtener más información sobre los métodos de clase, consulte La jerarquía de tipos estándar.

Cambiado en la versión 3.9: los métodos de clase ahora pueden envolver otros descriptores como `property()`.

### compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
Compila la fuente en un código o un objeto `AST`. Los objetos de código se pueden ejecutar mediante `exec()` o `eval()`. fuente puede ser una cadena normal, una cadena de bytes o un objeto `AST`. Consulte la documentación del módulo ast para obtener información sobre cómo trabajar con objetos `AST`.

El argumento del nombre de archivo debe proporcionar el archivo del que se leyó el código; pasar algún valor reconocible si no se leyó de un archivo (comúnmente se usa `'<string>'`).

El argumento de modo específica qué tipo de código se debe compilar; puede ser `'exec'` si la fuente consta de una secuencia de sentencias, `'eval'` si consta de una sola expresión o `'single'` si consta de una única sentencia interactiva (en el último caso, sentencias de expresión que se evalúan como algo que no sea Ninguno se imprimirá).

Los indicadores de argumentos opcionales y `dont_inherit` controlan qué opciones del compilador deben activarse y qué características futuras deben permitirse. Si ninguno está presente (o ambos son cero), el código se compila con las mismas `flags` que afectan al código que está llamando a `compile()`. Si se da el argumento `flags` y `dont_inherit` no (o es cero), entonces las opciones del compilador y las declaraciones futuras especificadas por el argumento flags se usan además de las que se usarían de todos modos. Si `dont_inherit` es un número entero distinto de cero, entonces el argumento de las `flags` es `–` las `flags` (características futuras y opciones del compilador) en el código circundante se ignoran.

Las opciones del compilador y las declaraciones futuras se especifican mediante bits que se pueden combinar con OR para especificar varias opciones. El campo de bits necesario para especificar una función futura dada se puede encontrar como el atributo `compiler_flag` en `_Feature instance in the __future__ module`. Los indicadores del compilador se pueden encontrar en el módulo ast, con el prefijo `PyCF_`.

El argumento optimizar especifica el nivel de optimización del compilador; el valor predeterminado de `-1` selecciona el nivel de optimización del intérprete dado por las opciones `-O`. Los niveles explícitos son 0 (sin optimización; `__debug__` es verdadero), 1 (se eliminan las afirmaciones, `__debug__` es falso) o 2 (también se eliminan las cadenas de documentación).

Esta función genera `SyntaxError` si la fuente compilada no es válida y `ValueError` si la fuente contiene bytes nulos.

Si desea analizar el código de Python en su representación `AST`, consulte `ast.parse()`.

Genera una compilación de eventos de auditoría con fuente de argumentos y nombre de archivo. Este evento también puede generarse mediante una compilación implícita.

Nota Al compilar una cadena con código de varias líneas en modo `'single'` o `'eval'`, la entrada debe terminar con al menos un carácter de nueva línea. Esto es para facilitar la detección de declaraciones incompletas y completas en el módulo de código.
Advertencia Es posible bloquear el intérprete de Python con una cadena lo suficientemente grande/compleja al compilar en un objeto AST debido a las limitaciones de profundidad de pila en el compilador AST de Python.

Modificado en la versión 3.2: uso permitido de líneas nuevas de Windows y Mac. Además, la entrada en el modo `'exec'` ya no tiene que terminar en una nueva línea. Se agregó el parámetro de optimización.

Modificado en la versión 3.5: Anteriormente, se generaba `TypeError` cuando se encontraban bytes nulos en el origen.

Nuevo en la versión 3.8: `ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` ahora se puede pasar en `flags` para habilitar el soporte para `top-level await`, `async for`, y `async with`.

### class complex([real[, imag]])
Devuelve un número complejo con el valor `real + imag*1j` o convierte una cadena o número en un número complejo. Si el primer parámetro es una cadena, se interpretará como un número complejo y la función debe llamarse sin un segundo parámetro. El segundo parámetro nunca puede ser una cadena. Cada argumento puede ser de cualquier tipo numérico (incluido el complejo). Si se omite imag, el valor predeterminado es cero y el constructor sirve como una conversión numérica como `int` y `float`. Si se omiten ambos argumentos, devuelve `0j`.

Para un Python general `object x`, `complex(x)` delegados a `x.__complex__()`. `If __complex__()` no está definido entonces vuelve a `__float__()`. `If __float__()` no está definido entonces vuelve a `__index__()`.

Nota al convertir un`string`, el `string` no debe contener espacios en blanco alrededor del operador `+` o `-`. Por ejemplo, `complex('1+2j')` está bien, pero `complex('1 + 2j')` da un `ValueError`.

El tipo `complex` se describe en Tipos numéricos — `int`, `float`, `complex`.

Modificado en la versión 3.6: se permite agrupar dígitos con guiones bajos como en los literales de código.
Cambiado en la versión 3.8: recurre a `__index__()` si `__complex__()` y `__float__()` no están definidos.

### delattr(object, name)
Este es un pariente de `setattr()`. Los argumentos son un objeto y una cadena. La cadena debe ser el nombre de uno de los atributos del objeto. La función elimina el atributo nombrado, siempre que el objeto lo permita. Por ejemplo, `delattr(x, 'foobar')` es equivalente a del `x.foobar`.

### class dict(**kwarg)

`class dict(mapping, **kwarg)`
`class dict(iterable, **kwarg)`

Crear un nuevo diccionario. El objeto `dict` es la clase de diccionario. Consulte `dict` y `Mapping Types — dict` para obtener documentación sobre esta clase.

Para otros contenedores, consulte las clases integradas de `list`, `set` y `tuple`, así como el módulo de colecciones.

### dir([object])
Sin argumentos, devuelve la lista de nombres en el ámbito local actual. Con un argumento, intente devolver una lista de atributos válidos para ese objeto.

Si el objeto tiene un método llamado `__dir__()`, se llamará a este método y debe devolver la lista de atributos. Esto permite que los objetos que implementan una función personalizada `__getattr__()` o `__getattribute__()` personalicen la forma en que `dir()` informa sus atributos.

Si el objeto no proporciona `__dir__()`, la función hace todo lo posible para recopilar información del atributo `__dict__` del objeto, si está definido, y de su tipo de objeto. La lista resultante no está necesariamente completa y puede ser inexacta cuando el objeto tiene un `__getattr__()` personalizado.

El mecanismo predeterminado `dir()` se comporta de manera diferente con diferentes tipos de objetos, ya que intenta producir la información más relevante, en lugar de completa:

Si el objeto es un objeto de módulo, la lista contiene los nombres de los atributos del módulo.

Si el objeto es un objeto de tipo o clase, la lista contiene los nombres de sus atributos y recursivamente de los atributos de sus bases.

De lo contrario, la lista contiene los nombres de los atributos del objeto, los nombres de los atributos de su clase y, recursivamente, los atributos de las clases base de su clase.

La lista resultante se ordena alfabéticamente. Por ejemplo:

```python
import struct
dir()   # mostrar los nombres en el espacio de nombres del módulo
['__builtins__', '__name__', 'struct']
dir(struct)   # mostrar los nombres en el módulo struct
['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
 '__initializing__', '__loader__', '__name__', '__package__',
 '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']
class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']
s = Shape()
dir(s)
```

**Nota**: Debido a que `dir()` se proporciona principalmente como una conveniencia para su uso en un aviso interactivo, intenta proporcionar un conjunto interesante de nombres más que un conjunto de nombres definidos de manera rigurosa o consistente, y su comportamiento detallado puede cambiar entre versiones. Por ejemplo, los atributos de la metaclase no están en la lista de resultados cuando el argumento es una clase.

### divmod(a, b)
Toma dos números (no complejos) como argumentos y devuelve un par de números que consisten en su cociente y resto al usar la división de enteros. Con tipos de operandos mixtos, se aplican las reglas para los operadores aritméticos binarios. Para números enteros, el resultado es el mismo que (`a // b, a % b`). Para números de punto flotante, el resultado es (`q, a % b`), donde q suele ser math.floor (a / b), pero puede ser 1 menos que eso. En cualquier caso q * b + a % b está muy cerca de a, si a % b es distinto de cero tiene el mismo signo que b, y 0 <= abs(a % b) < abs(b).

### enumerate(iterable, start=0)
Devuelve un objeto de enumeración. iterable debe ser una secuencia, un iterador o algún otro objeto que soporte la iteración. El método `__next__()` del iterador devuelto por enumerate() devuelve una tupla que contiene un recuento (desde el inicio, que por defecto es 0) y los valores obtenidos al iterar sobre iterable.

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
Equivalent to:

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
eval(expression[, globals[, locals]])
```

Los argumentos son una cadena y globales y locales opcionales. Si se proporciona, los valores globales deben ser un diccionario. Si se proporcionan, los locales pueden ser cualquier objeto de mapeo.

El argumento de la expresión se analiza y evalúa como una expresión de Python (técnicamente hablando, una lista de condiciones) utilizando los diccionarios globales y locales como espacio de nombres global y local. Si el diccionario global está presente y no contiene un valor para la clave `__builtins__`, se inserta una referencia al diccionario de los integrados del módulo integrado debajo de esa clave antes de que se analice la expresión. Esto significa que la expresión normalmente tiene acceso completo al módulo integrado estándar y se propagan entornos restringidos. Si se omite el diccionario local, el valor predeterminado es el diccionario global. Si se omiten ambos diccionarios, la expresión se ejecuta con los globales y los locales en el entorno donde se llama a `eval()`. Tenga en cuenta que `eval()` no tiene acceso a los ámbitos anidados (no locales) en el entorno adjunto.

El valor de retorno es el resultado de la expresión evaluada. Los errores de sintaxis se notifican como excepciones. Ejemplo:

```python
x = 1
eval('x+1')
```

Esta función también se puede usar para ejecutar objetos de código arbitrario (como los creados por `compile()`). En este caso, pase un objeto de código en lugar de una cadena. Si el objeto de código se ha compilado con `'exec'` como argumento de modo, el valor de retorno de `eval()` será Ninguno.

Sugerencias: la función `exec()` admite la ejecución dinámica de sentencias. Las funciones `globals()` y `locals()` devuelven el diccionario global y local actual, respectivamente, que puede ser útil para pasar a `eval()` o `exec()`.

Consulte `ast.literal_eval()` para ver una función que puede evaluar de forma segura cadenas con expresiones que contienen solo literales.

Genera un evento de auditoría exec con el objeto de código como argumento. También se pueden generar eventos de compilación de código.

### exec(object[, globals[, locals]])
Esta función admite la ejecución dinámica del código de Python. El objeto debe ser una cadena o un objeto de código. Si es una cadena, la cadena se analiza como un conjunto de declaraciones de Python que luego se ejecuta (a menos que ocurra un error de sintaxis). 1 Si es un objeto de código, simplemente se ejecuta. En todos los casos, se espera que el código que se ejecuta sea válido como entrada de archivo (consulte la sección Entrada de archivo en el Manual de referencia). Tenga en cuenta que las declaraciones nonlocal, yield y return no se pueden usar fuera de las definiciones de funciones, incluso dentro del contexto del código pasado a la función exec(). El valor de retorno es Ninguno.

En todos los casos, si se omiten las partes opcionales, el código se ejecuta en el ámbito actual. Si solo se proporcionan variables globales, debe ser un diccionario (y no una subclase de diccionario), que se utilizará tanto para las variables globales como para las locales. Si se dan valores globales y locales, se utilizan para las variables globales y locales, respectivamente. Si se proporcionan, los locales pueden ser cualquier objeto de mapeo. Recuerde que a nivel de módulo, globales y locales son el mismo diccionario. Si exec obtiene dos objetos separados como globales y locales, el código se ejecutará como si estuviera incrustado en una definición de clase.

Si el diccionario global no contiene un valor para la clave `__builtins__`, se inserta una referencia al diccionario de los componentes integrados del módulo debajo de esa clave. De esa manera, puede controlar qué funciones integradas están disponibles para el código ejecutado insertando su propio diccionario de `__builtins__` en los globales antes de pasarlo a `exec()`.

Genera un evento de auditoría exec con el objeto de código como argumento. También se pueden generar eventos de compilación de código.

Nota Las funciones integradas `globals()` y `locals()` devuelven el diccionario global y local actual, respectivamente, que puede ser útil para pasar como segundo y tercer argumento a `exec()`.
Nota Los locales predeterminados actúan como se describe para la función locals() a continuación: no se deben intentar modificaciones en el diccionario de locales predeterminados. Pase un diccionario local explícito si necesita ver los efectos del código en los locales después de que regrese la función `exec()`.

### filter(function, iterable)
Construya un iterador a partir de esos elementos de iterable para los cuales la función devuelve verdadero. iterable puede ser una secuencia, un contenedor que admita la iteración o un iterador. Si function es None, se asume la función de identidad, es decir, se eliminan todos los elementos de iterable que son falsos.

Tenga en cuenta que `filter(function, iterable)` es equivalente a la expresión del generador (`item for item in iterable if function(item)`) si la función no es None y (`item for item in iterable if item`) si la función es None.

Ver `itertools.filterfalse()` para la función complementaria que devuelve elementos de iterable para los cuales la función devuelve falso.

### class float([x])
Devuelve un número de punto flotante construido a partir de un número o cadena x.

Si el argumento es una cadena, debe contener un número decimal, opcionalmente precedido por un signo y opcionalmente incrustado en un espacio en blanco. El signo opcional puede ser '+' o '-'; un signo '+' no tiene efecto sobre el valor producido. El argumento también puede ser una cadena que represente un NaN (no un número) o un infinito positivo o negativo. Más precisamente, la entrada debe ajustarse a la siguiente gramática después de eliminar los espacios en blanco iniciales y finales:

```
sign           ::=  "+" | "-"
infinity       ::=  "Infinity" | "inf"
nan            ::=  "nan"
numeric_value  ::=  floatnumber | infinity | nan
numeric_string ::=  [sign] numeric_value
```

Aquí floatnumber es la forma de un literal de punto flotante de Python, descrito en Literales de punto flotante. El uso de mayúsculas y minúsculas no es significativo, por lo que, por ejemplo, "inf", "Inf", "INFINITY" e "iNfINity" son grafías aceptables para infinito positivo.

De lo contrario, si el argumento es un número entero o de punto flotante, se devuelve un número de punto flotante con el mismo valor (dentro de la precisión de punto flotante de Python). Si el argumento está fuera del rango de un flotante de Python, se generará un OverflowError.

Para un objeto Python general x, float(x) delega a x.`__float__()`. Si `__float__()` no está definido, recurre a `__index__()`.

Si no se da ningún argumento, se devuelve 0.0.

Ejemplos:

```python
print(float('+1.23'))
print(float('   -12345\n'))
print(float('1e-003'))
print(float('+1E6'))
print(float('-Infinity'))
```

El tipo flotante se describe en Tipos numéricos: int, float, complex.

Modificado en la versión 3.6: se permite agrupar dígitos con guiones bajos como en los literales de código.

Cambiado en la versión 3.7: x ahora es un parámetro solo posicional.

Cambiado en la versión 3.8: recurre a `__index__()` si `__float__()` no está definido.

### format(value[, format_spec])
Convierte un valor en una representación "formateada", según lo controlado por `format_spec`. La interpretación de `format_spec` dependerá del tipo de argumento de valor; sin embargo, existe una sintaxis de formato estándar que utilizan la mayoría de los tipos integrados: minilenguaje de especificación de formato.

El format_spec predeterminado es una cadena vacía que generalmente da el mismo efecto que llamar a str(value).

Una llamada a `format(value, format_spec)` se traduce a `type(value)`.`__format__(value, format_spec)` que omite el diccionario de instancias cuando busca el método `__format__()` del valor. Se genera una excepción **TypeError** si la búsqueda del método alcanza el objeto y `format_spec` no está vacío, o si format_spec o el valor de retorno no son cadenas.

Cambiado en la versión 3.4: `object()`.`__format__(format_spec)` muestra un **TypeError** si `format_spec` no es una cadena vacía.

### class frozenset([iterable])
Devuelve un nuevo objeto `frozenset`, opcionalmente con elementos tomados de iterable. `frozenset` es una clase integrada. Consulte `frozenset` y `Set Types — set`, frozenset para obtener documentación sobre esta clase.

Para otros contenedores, consulte las clases integradas `set`, `list`, `tuple` y `dict`, así como el módulo de colecciones.

### getattr(object, name[, default])
Devuelve el valor del atributo nombrado del objeto. El nombre debe ser una cadena. Si la cadena es el nombre de uno de los atributos del objeto, el resultado es el valor de ese atributo. Por ejemplo, `getattr(x, 'foobar')` es equivalente a `x.foobar`. Si el atributo nombrado no existe, se devuelve el valor predeterminado si se proporciona; de lo contrario, se genera **AttributeError**.

Nota Dado que la manipulación de nombres privados ocurre en el momento de la compilación, uno debe manipular manualmente el nombre de un atributo privado (atributos con dos guiones bajos al principio) para recuperarlo con `getattr()`.

### globals()
Devuelve el diccionario que implementa el espacio de nombres del módulo actual. Para el código dentro de las funciones, esto se establece cuando se define la función y permanece igual independientemente de dónde se llame a la función.

### hasattr(object, name)
Los argumentos son un objeto y una cadena. El resultado es True si la cadena es el nombre de uno de los atributos del objeto, False si no lo es. (Esto se implementa llamando a `getattr(objet, name)` y viendo si genera un **AttributeError** o no).

### hash(object)
Devuelve el valor hash del objeto (si lo tiene). Los valores hash son números enteros. Se utilizan para comparar rápidamente las claves del diccionario durante una búsqueda en el diccionario. Los valores numéricos que se comparan iguales tienen el mismo valor hash (incluso si son de diferentes tipos, como es el caso de 1 y 1.0).

Nota Para los objetos con métodos `__hash__()` personalizados, tenga en cuenta que `hash()` trunca el valor devuelto en función del ancho de bits de la máquina host. Ver `__hash__()` para más detalles.

### help([object])
Invocar el sistema de ayuda integrado. (Esta función está diseñada para uso interactivo). Si no se proporciona ningún argumento, el sistema de ayuda interactivo se inicia en la consola del intérprete. Si el argumento es una cadena, la cadena se busca como el nombre de un módulo, función, clase, método, palabra clave o tema de documentación, y se imprime una página de ayuda en la consola. Si el argumento es cualquier otro tipo de objeto, se genera una página de ayuda sobre el objeto.

Tenga en cuenta que si aparece una barra slash(/) en la lista de parámetros de una función, al invocar `help()`, significa que los parámetros anteriores a la barra inclinada son solo posicionales. Para obtener más información, consulte la entrada de preguntas frecuentes sobre parámetros solo posicionales.

El módulo del sitio agrega esta función al espacio de nombres integrado.

Modificado en la versión 3.4: los cambios en `pydoc` e inspeccionar significan que las firmas informadas para los invocables ahora son más completas y consistentes.

### hex(x)
Convierta un número entero en una cadena hexadecimal en minúsculas con el prefijo "0x". Si x no es un objeto int de Python, tiene que definir un método `__index__()` que devuelva un número entero. Algunos ejemplos:

```python
print(hex(255))
print(hex(-42))
```

Si desea convertir un número entero en una cadena hexadecimal en mayúsculas o minúsculas con prefijo o no, puede usar cualquiera de las siguientes formas:

```python
'%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')
format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')
f'{255:#x}', f'{255:x}', f'{255:X}'
('0xff', 'ff', 'FF')
```

Ver también `format()` para más información.

Consulte también `int()` para convertir una cadena hexadecimal en un número entero usando una base de 16.

Nota Para obtener una representación de cadena hexadecimal para un flotante, use el método `float.hex()`.

### id(object)
Devuelve la “identity” de un objeto. Este es un número entero que se garantiza que es único y constante para este objeto durante su vida útil. Dos objetos con tiempos de vida no superpuestos pueden tener el mismo valor `id()`.

Detalle de implementación de CPython: esta es la dirección del objeto en la memoria.

Genera un evento de auditoría builtins.id con id de argumento.

### input([prompt])
Si el argumento de solicitud está presente, se escribe en la salida estándar sin una nueva línea al final. Luego, la función lee una línea de la entrada, la convierte en una cadena (eliminando una nueva línea final) y la devuelve. Cuando se lee **EOF**, se genera **EOFError**. Ejemplo:

```python
s = input('--> ') 
s  
```
Si se cargó el módulo readline, entonces `input()` lo usará para proporcionar funciones elaboradas de edición de línea e historial.

Genera un evento de auditoría `builtins.input` con solicitud de argumento antes de leer la entrada

Genera un evento de auditoría `builtins.input/result` con el resultado después de leer correctamente la entrada.

### class int([x])
```python
class int(x, base=10)
```
Devuelve un objeto entero construido a partir de un número o cadena `x`, o devuelve 0 si no se proporcionan argumentos. Si `x` define `__int__()`, `int(x)` devuelve `x.__int__()`. Si x define `__index__()`, devuelve `x.__index__()`. Si x define `__trunc__()`, devuelve `x.__trunc__()`. Para números de punto flotante, esto se trunca hacia cero.

Si x no es un número o si se proporciona la base, entonces x debe ser una instancia de cadena, bytes o bytearray que represente un literal entero en base radix. Opcionalmente, el literal puede estar precedido por + o - (sin espacios intermedios) y rodeado por espacios en blanco. Un literal de base-n consiste en los dígitos 0 a n-1, con a a z (o A a Z) con valores de 10 a 35. La base predeterminada es 10. Los valores permitidos son 0 y 2–36. Los literales Base-2, -8 y -16 pueden tener el prefijo opcional 0b/0B, 0o/0O o 0x/0X, como con los literales enteros en el código. Base 0 significa interpretar exactamente como un código literal, de modo que la base real sea 2, 8, 10 o 16, y que int('010', 0) no sea legal, mientras que int('010') sí lo es, así como int('010', 8).

El tipo entero se describe en Tipos numéricos: int, float, complex.

Modificado en la versión 3.4: si base no es una instancia de int y el objeto base tiene un método `base.__index__`, se llama a ese método para obtener un número entero para la base. Las versiones anteriores usaban base.`__int__` en lugar de `base.__index__`.

Modificado en la versión 3.6: se permite agrupar dígitos con guiones bajos como en los literales de código.

Cambiado en la versión 3.7: x ahora es un parámetro solo posicional.

Cambiado en la versión 3.8: recurre a `__index__()` si `__int__()` no está definido.

Modificado en la versión 3.9.14: las entradas de cadena int y las representaciones de cadena se pueden limitar para ayudar a evitar ataques de denegación de servicio. Se genera un ValueError cuando se excede el límite al convertir una cadena x en un int o cuando convertir un int en una cadena excedería el límite. Consulte la documentación de limitación de longitud de conversión de cadena entera.

### isinstance(object, classinfo)
Retorna **True** si el argumento del objeto es una instancia del argumento classinfo, o de una subclase (directa, indirecta o virtual) del mismo. Si el objeto no es un objeto del tipo dado, la función siempre devuelve **False**. Si `classinfo` es una tupla de objetos de tipo (o recursivamente, otras tuplas similares), devuelva True si el objeto es una instancia de cualquiera de los tipos. Si `classinfo` no es un tipo o una tupla de tipos y tales tuplas, se genera una excepción **TypeError**.

### issubclass(class, classinfo)
Retorna **True** si class es una subclase (directa, indirecta o virtual) de`classinfo`. Una clase se considera una subclase de sí misma. `classinfo` puede ser una tupla de objetos de clase (o recursivamente, otras tuplas similares), en cuyo caso devuelve **True** si class es una subclase de cualquier entrada en `classinfo`. En cualquier otro caso, se genera una excepción **TypeError**.

### iter(object[, sentinel])
Devuelve un objeto iterador. El primer argumento se interpreta de manera muy diferente dependiendo de la presencia del segundo argumento. Sin un segundo argumento, el objeto debe ser un objeto de colección que admita el protocolo de iteración (el método `__iter__()`), o debe admitir el protocolo de secuencia (el método `__getitem__()` con argumentos enteros que comienzan en 0). Si no es compatible con ninguno de esos protocolos, se genera TypeError. Si se proporciona el segundo argumento, centinela, entonces el objeto debe ser un objeto invocable. El iterador creado en este caso llamará al objeto sin argumentos para cada llamada a su método `__next__()`; si el valor devuelto es igual a centinela, se generará **StopIteration**; de lo contrario, se devolverá el valor.

Consulte también Tipos de iteradores.

Una aplicación útil de la segunda forma de `iter()` es construir un lector de bloques. Por ejemplo, leer bloques de ancho fijo de un archivo de base de datos binaria hasta que se alcance el final del archivo:

```python
from functools import partial
with open('mydata.db', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        process_block(block)
```

### len(s)
Devuelve la longitud (el número de elementos) de un objeto. El argumento `s` puede ser una secuencia (como un `string`, `bytes`, `tuple`, `list`, or `range`) o una colección (como `dictionary`, `set`, o `frozen set`).

Detalle de implementación de **CPython**: len genera **OverflowError** en longitudes mayores que `sys.maxsize`, como `range(2 ** 100)`.

### class list([iterable])
En lugar de ser una función, la lista es en realidad un tipo de secuencia mutable, como se documenta en tipos de secuencia — `list`, `tuple`, `range`.

### locals()
Actualice y devuelva un diccionario que represente la tabla de símbolos local actual. Las variables libres son devueltas por `locals()` cuando se llaman en bloques de función, pero no en bloques de clase. Tenga en cuenta que a nivel de módulo, `locals()` y `globals()` son el mismo diccionario.

Nota El contenido de este diccionario no debe modificarse; los cambios pueden no afectar los valores de las variables locales y libres utilizadas por el intérprete.

### map(function, iterable, ...)
Devuelve un iterador que aplica la función a cada elemento de iterable, arrojando los resultados. Si se pasan argumentos iterables adicionales, la función debe tomar esa cantidad de argumentos y se aplica a los elementos de todos los iterables en paralelo. Con múltiples iterables, el iterador se detiene cuando se agota el iterable más corto. Para los casos en los que las entradas de la función ya están organizadas en tuplas de argumentos, consulte itertools.`starmap()`.

### max(iterable, *[, key, default])

```python
max(arg1, arg2, *args[, key])
```

Devuelve el elemento más grande en un iterable o el más grande de dos o más argumentos.

Si se proporciona un argumento posicional, debe ser iterable. Se devuelve el elemento más grande del iterable. Si se proporcionan dos o más argumentos posicionales, se devuelve el mayor de los argumentos posicionales.

Hay dos argumentos opcionales de solo palabras clave. El argumento clave especifica una función de ordenación de un argumento como la utilizada para `list.sort()`. El argumento predeterminado especifica un objeto para devolver si el iterable proporcionado está vacío. Si el iterable está vacío y no se proporciona el valor predeterminado, se genera un **ValueError**.

Si varios elementos son máximos, la función devuelve el primero encontrado. Esto es consistente con otras herramientas que preservan la estabilidad de clasificación, como `sorted(iterable, key=keyfunc, reverse=True)[0]` y `heapq.nlargest(1, iterable, key=keyfunc)`.

Nuevo en la versión 3.4: el argumento predeterminado de solo palabra clave.

Cambiado en la versión 3.8: La clave puede ser Ninguna.

### class memoryview(object)
Devuelve un objeto de "memory view" creado a partir del argumento dado. Consulte `memory view` para obtener más información.

### min(iterable, *[, key, default])
```python
min(arg1, arg2, *args[, key])
```

Devuelve el elemento más pequeño en un iterable o el más pequeño de dos o más argumentos.

Si se proporciona un argumento posicional, debe ser iterable. Se devuelve el elemento más pequeño del iterable. Si se proporcionan dos o más argumentos posicionales, se devuelve el menor de los argumentos posicionales.

Hay dos argumentos opcionales de solo palabras clave. El argumento clave especifica una función de ordenación de un argumento como la que se usa para `list.sort()`. El argumento predeterminado especifica un objeto para devolver si el iterable proporcionado está vacío. Si el iterable está vacío y no se proporciona el valor predeterminado, se genera un **ValueError**.

Si varios elementos son mínimos, la función devuelve el primero encontrado. Esto es coherente con otras herramientas que preservan la estabilidad de clasificación, como `sorted(iterable, key=keyfunc)[0]` y `heapq.nsmallest(1, iterable, key=keyfunc)`.

Nuevo en la versión 3.4: el argumento predeterminado de solo palabra clave.

Cambiado en la versión 3.8: La clave puede ser **None**.

### next(iterator[, default])
Recupere el siguiente elemento del iterador llamando a su método `__next__()`. Si se proporciona el valor predeterminado, se devuelve si se agota el iterador; de lo contrario, se genera **StopIteration**.

## class object
Return a new featureless object. object is a base for all classes. It has the methods that are common to all instances of Python classes. This function does not accept any arguments.

Note object does not have a `__dict__`, so you can’t assign arbitrary attributes to an instance of the object class.

### oct(x)
Convierta un número entero en una cadena octal con el prefijo "0o". El resultado es una expresión de Python válida. Si x no es un objeto int de Python, tiene que definir un método `__index__()` que devuelva un número entero. Por ejemplo:

```python
print(oct(8))
print(oct(-56))
```
Si desea convertir un número entero en una cadena octal con el prefijo "0o" o no, puede usar cualquiera de las siguientes formas.

```python
'%#o' % 10, '%o' % 10
format(10, '#o'), format(10, 'o')
f'{10:#o}', f'{10:o}'
```

Ver `format()` para más información.

### open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
Abrir archivo y devolver un objeto de archivo correspondiente. Si no se puede abrir el archivo, se genera un OSError. Consulte Lectura y escritura de archivos para obtener más ejemplos de cómo utilizar esta función.

file es un objeto similar a una ruta que proporciona la ruta (absoluta o relativa al directorio de trabajo actual) del archivo que se abrirá o un descriptor de archivo entero del archivo que se empaquetará. (Si se proporciona un descriptor de archivo, se cierra cuando se cierra el objeto de E/S devuelto, a menos que closefd se establezca en False).

mode es una cadena opcional que especifica el modo en que se abre el archivo. El valor predeterminado es 'r', lo que significa que está abierto para leer en modo texto. Otros valores comunes son 'w' para escribir (truncar el archivo si ya existe), 'x' para creación exclusiva y 'a' para agregar (que en algunos sistemas Unix significa que todas las escrituras se agregan al final del archivo independientemente de la posición de búsqueda actual). En el modo de texto, si no se especifica la codificación, la codificación utilizada depende de la plataforma: se llama `locale.getpreferredencoding(False)` para obtener la codificación local actual. (Para leer y escribir bytes sin procesar, use el modo binario y deje la codificación sin especificar). Los modos disponibles son:

'r' - Abrir para leer (predeterminado)

'w' - Abrir para escribir, trunca el archivo primero

'x' - Abrir para creación exclusiva, fallando si el archivo ya existe

'a' - Abrir para escritura, agregando al final del archivo si existe

'b' - Modo binario

't' - Modo de texto (predeterminado)

'+' - Abrir para actualización (lectura y escritura)

### ord(c)
Dada una cadena que representa un carácter Unicode, devuelve un entero que representa el punto de código Unicode de ese carácter. Por ejemplo, `ord('a')` devuelve el número entero 97 y `ord('€')` (símbolo del euro) devuelve 8364. Este es el inverso de `chr()`.

### pow(base, exp[, mod])
Regrese la base a la potencia `exp`; si mod está presente, regrese la base a la potencia `exp`, módulo mod (calculado más eficientemente que `pow(base, exp) % mod`). La forma de dos argumentos `pow(base, exp)` es equivalente a usar el operador de potencia: `base**exp`.

Los argumentos deben tener tipos numéricos. Con tipos de operandos mixtos, se aplican las reglas de coerción para operadores aritméticos binarios. Para los operandos int, el resultado tiene el mismo tipo que los operandos (después de la coerción) a menos que el segundo argumento sea negativo; en ese caso, todos los argumentos se convierten en flotantes y se entrega un resultado flotante. Por ejemplo, `pow(10, 2)` devuelve 100, pero `pow(10, -2)` devuelve 0,01. Para una base negativa de tipo int o float y un exponente no integral, se obtiene un resultado complejo. Por ejemplo, `pow(-9, 0.5)` devuelve un valor cercano a 3j.

Para los operandos `int base` y `exp`, si `mod` está presente, `mod` también debe ser de tipo entero y `mod` debe ser distinto de cero. Si `mod` está presente y exp es negativa, la base debe ser relativamente prima para `mod`. En ese caso, se devuelve `pow(inv_base, -exp, mod)`, donde `inv_base` es un `mod` de módulo inverso al base.

Aquí hay un ejemplo de calcular un inverso para 38 módulo 97:

```python
print(pow(38, -1, mod=97))
print(23 * 38 % 97 == 1)
```

Cambiado en la versión 3.8: para los operandos int, la forma de tres argumentos de pow ahora permite que el segundo argumento sea negativo, lo que permite el cálculo de inversas modulares.

Cambiado en la versión 3.8: Permitir argumentos de palabras clave. Anteriormente, solo se admitían argumentos posicionales.

### print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

Imprime objetos en el archivo de flujo de texto, separados por `sep` y seguidos por `end`. `sep`, `end`, `file` y `flush`, si están presentes, deben proporcionarse como argumentos de palabras clave.

Todos los argumentos que no son palabras clave se convierten en cadenas como lo hace `str()` y se escriben en la transmisión, separados por sep y seguidos por end. Tanto sep como end deben ser cadenas; también pueden ser Ninguno, lo que significa utilizar los valores predeterminados. Si no se dan objetos, `print()` simplemente escribirá fin.

El argumento del archivo debe ser un objeto con un método `write(string)`; si no está presente o Ninguno, se utilizará `sys.stdout`. Dado que los argumentos impresos se convierten en cadenas de texto, `print()` no se puede usar con objetos de archivo en modo binario. Para estos, use `file.write(...)` en su lugar.

El archivo generalmente determina si la salida se almacena en búfer, pero si el argumento de la palabra clave de descarga es verdadero, la secuencia se descarga a la fuerza.

Cambiado en la versión 3.3: Se agregó el argumento de palabra clave de descarga.

### class property(fget=None, fset=None, fdel=None, doc=None)
Devuelve un atributo de propiedad.

fget es una función para obtener un valor de atributo. fset es una función para establecer un valor de atributo. fdel es una función para eliminar un valor de atributo. Y doc crea una cadena de documentación para el atributo.

Un uso típico es definir un atributo gestionado x:
```python
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
```
Si `c` es una instancia de `C`, `c.x` invocará al getter, `c.x = value` invocará al setter y del `c.x` al eliminador.

Si se proporciona, doc será la `docstring` del atributo de propiedad. De lo contrario, la propiedad copiará la `docstring` de fget (si existe). Esto hace posible crear fácilmente propiedades de solo lectura usando `property()` como decorador:

```python
class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Obtener el voltaje actual"""
        return self._voltage
```
El decorador `@property` convierte el método `voltage()` en un "captador" para un atributo de solo lectura con el mismo nombre, y establece la `docstring` para el voltaje en "Obtener el voltaje actual".

Un objeto de propiedad tiene métodos getter, setter y deleter que se pueden usar como decoradores que crean una copia de la propiedad con la función de acceso correspondiente establecida en la función decorada. Esto se explica mejor con un ejemplo:

```python
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```
Este código es exactamente equivalente al primer ejemplo. Asegúrese de dar a las funciones adicionales el mismo nombre que la propiedad original (x en este caso).

El objeto de propiedad devuelto también tiene los atributos fget, fset y fdel correspondientes a los argumentos del constructor.

Cambiado en la versión 3.5: Las cadenas de documentación de los objetos de propiedad ahora se pueden escribir.

### class range(stop)

```python
class range(start, stop[, step])
```

En lugar de ser una función, el rango es en realidad un tipo de secuencia inmutable, como se documenta en Rangos y tipos de secuencia — list, tuple, range.

### repr(object)

Devuelve una cadena que contiene una representación imprimible de un objeto. Para muchos tipos, esta función intenta devolver una cadena que produciría un objeto con el mismo valor cuando se pasa a `eval()`, de lo contrario, la representación es una cadena encerrada entre corchetes angulares que contiene el nombre del tipo del objeto junto con información adicional que a menudo incluye el nombre y la dirección del objeto. Una clase puede controlar lo que devuelve esta función para sus instancias definiendo un método `__repr__()`.

### reversed(seq)

Devuelve un iterador inverso. seq debe ser un objeto que tenga un método `__reversed__()` o admita el protocolo de secuencia (el método `__len__()` y el método `__getitem__()` con argumentos enteros que comienzan en 0).

### round(number[, ndigits])
Devuelve el número redondeado a la precisión de los dígitos después del punto decimal. Si se omite ndigits o es None, devuelve el entero más cercano a su entrada.

Para los tipos incorporados que admiten `round()`, los valores se redondean al múltiplo de 10 más cercano a la potencia menos los dígitos; si dos múltiplos son igualmente cercanos, el redondeo se realiza hacia la opción par (por ejemplo, tanto `round(0.5)` como `round(-0.5)` son 0, y `round(1.5)` es 2). Cualquier valor entero es válido para dígitos (positivo, cero o negativo). El valor de retorno es un número entero si se omite ndigits o Ninguno. De lo contrario, el valor de retorno tiene el mismo tipo que el número.

Para un número de objeto de Python general, redondee los delegados a `number.__round__`.

Nota El comportamiento de `round()` para flotantes puede ser sorprendente: por ejemplo, `round(2.675, 2)` da 2.67 en lugar del esperado 2.68. Esto no es un error: es el resultado del hecho de que la mayoría de las fracciones decimales no se pueden representar exactamente como un flotante. Consulte Aritmética de coma flotante: problemas y limitaciones para obtener más información.

### class set([iterable])
Devuelve un nuevo objeto establecido, opcionalmente con elementos tomados de iterable. set es una clase incorporada. Consulte `set` y Set Types — `set`, `frozenset` para obtener documentación sobre esta clase.

Para otros contenedores, consulte las clases integradas `frozenset`, `list`, `tuple` y `dict`, así como el módulo de colecciones.

### setattr(object, name, value)
Esta es la contrapartida de `getattr()`. Los argumentos son un objeto, una cadena y un valor arbitrario. La cadena puede nombrar un atributo existente o un atributo nuevo. La función asigna el valor al atributo, siempre que el objeto lo permita. Por ejemplo, `setattr(x, 'foobar', 123)` es equivalente a `x.foobar = 123`.

Nota Dado que la manipulación de nombres privados ocurre en el momento de la compilación, uno debe manipular manualmente el nombre de un atributo privado (atributos con dos guiones bajos al principio) para configurarlo con `setattr()`.

### class slice(stop)

```python
class slice(start, stop[, step])
```

Devuelve un objeto de segmento que representa el conjunto de índices especificados por `range(start, stop, step)`. Los argumentos `start` and `step` estan en None de manera predeterminada. Los objetos Slice tienen atributos de solo lectura en `start`, `stop` and `step` que simplemente devuelven los valores del argumento (o su valor predeterminado). No tienen otra funcionalidad explícita; sin embargo, son utilizados por `NumPy` y otros paquetes de terceros. Los objetos de división también se generan cuando se usa la sintaxis de indexación extendida. Por ejemplo: `a[start:stop:step]` or `a[start:stop, i]`. See `itertools.islice()` para una versión alternativa que devuelve un iterador.

### sorted(iterable, /, *, key=None, reverse=False)

Devuelve una nueva lista ordenada de los elementos en iterable.

Tiene dos argumentos opcionales que deben especificarse como argumentos de palabra clave.

key especifica una función de un argumento que se usa para extraer una clave de comparación de cada elemento en iterable (por ejemplo, `key=str.lower`). El valor predeterminado es Ninguno (compare los elementos directamente).

reverse es un valor booleano. Si se establece en True, los elementos de la lista se ordenan como si cada comparación se invirtiera.

Use `functools.cmp_to_key()` para convertir una función cmp de estilo antiguo en una función clave.

Se garantiza que la función `incorporada sorted()` es estable. Una ordenación es estable si garantiza que no cambiará el orden relativo de los elementos que se comparan iguales; esto es útil para ordenar en varias pasadas (por ejemplo, ordenar por departamento y luego por grado salarial).

El algoritmo de clasificación usa solo < comparaciones entre elementos. Si bien definir un método `__lt__()` será suficiente para clasificar, PEP 8 recomienda que se implementen las seis comparaciones enriquecidas. Esto ayudará a evitar errores al usar los mismos datos con otras herramientas de pedido como `max()` que se basan en un método subyacente diferente. La implementación de las seis comparaciones también ayuda a evitar confusiones con las comparaciones de tipos mixtos que pueden llamar al método `__gt__()` reflejado.

Para ver ejemplos de clasificación y un breve tutorial de clasificación, consulte Cómo clasificar.

### @staticmethod
Transformar un método en un método estático.

Un método estático no recibe un primer argumento implícito. Para declarar un método estático, usa este modismo:

```python
class C:
    @staticmethod
    def f(arg1, arg2, ...): ...
```

El formulario `@staticmethod` es un decorador de funciones; consulte Definiciones de funciones para obtener más detalles.

Se puede llamar a un método estático en la clase (como `C.f()`) o en una instancia (como `C().f()`).

Los métodos estáticos en Python son similares a los que se encuentran en Java o C++. Consulte también `classmethod()` para ver una variante que es útil para crear constructores de clases alternativos.

Como todos los decoradores, también es posible llamar a staticmethod como una función regular y hacer algo con su resultado. Esto es necesario en algunos casos en los que necesita una referencia a una función de un cuerpo de clase y desea evitar el método de transformación automática a instancia. Para estos casos, utilice este modismo:

```python
class C:
    builtin_open = staticmethod(open)
```

For more information on static methods, see The standard type hierarchy.

```python
class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')
```

Devuelve una versión str del objeto. Ver `str()` para más detalles.

str es la clase de cadena incorporada. Para obtener información general sobre las cadenas, consulte Tipo de secuencia de texto — `str`.

### sum(iterable, /, start=0)
Suma el inicio y los elementos de un iterable de izquierda a derecha y devuelve el total. Los elementos del iterable son normalmente números, y no se permite que el valor inicial sea una cadena.

Para algunos casos de uso, existen buenas alternativas a `sum()`. La forma preferida y rápida de concatenar una secuencia de cadenas es llamando a `''.join(sequence)`. Para agregar valores de coma flotante con mayor precisión, consulte `math.fsum()`. Para concatenar una serie de iterables, considere usar `itertools.chain()`.

Modificado en la versión 3.8: el parámetro de inicio se puede especificar como un argumento de palabra clave.

### super([type[, object-or-type]])
Devuelve un objeto proxy que delega llamadas de método a una clase de tipo padre o hermano. Esto es útil para acceder a métodos heredados que han sido anulados en una clase.

El objeto o tipo determina el orden de resolución del método que se buscará. La búsqueda comienza desde la clase justo después del tipo.

Por ejemplo, si `__mro__` de objeto o tipo es D -> B -> C -> A -> objeto y el valor de tipo es B, entonces `super()` busca C -> A -> objeto.

El atributo `__mro__` del objeto o tipo enumera el orden de búsqueda de resolución del método utilizado tanto por `getattr()` como por `super()`. El atributo es dinámico y puede cambiar siempre que se actualice la jerarquía de herencia.

Si se omite el segundo argumento, el superobjeto devuelto no está vinculado. Si el segundo argumento es un objeto, isinstance(obj, type) debe ser verdadero. Si el segundo argumento es un tipo, `issubclass(type2, type)` debe ser verdadero (esto es útil para los métodos de clase).

Hay dos casos de uso típicos para super. En una jerarquía de clases con herencia única, se puede usar super para hacer referencia a las clases principales sin nombrarlas explícitamente, lo que hace que el código sea más fácil de mantener. Este uso es muy similar al uso de super en otros lenguajes de programación.

El segundo caso de uso es admitir la herencia múltiple cooperativa en un entorno de ejecución dinámico. Este caso de uso es exclusivo de Python y no se encuentra en lenguajes compilados estáticamente o lenguajes que solo admiten herencia única. Esto hace posible implementar "diagramas de diamantes" donde múltiples clases base implementan el mismo método. Un buen diseño dicta que dichas implementaciones tengan la misma firma de llamada en todos los casos (porque el orden de las llamadas se determina en el tiempo de ejecución, porque ese orden se adapta a los cambios en la jerarquía de clases y porque ese orden puede incluir clases hermanas que se desconocen antes del tiempo de ejecución ).

Para ambos casos de uso, una llamada de superclase típica se ve así:
```python
class C(B):
    def method(self, arg):
        super().method(arg)    # This does the same thing as:
                               # super(C, self).method(arg)
```

Además de las búsquedas de métodos, super() también funciona para las búsquedas de atributos. Un posible caso de uso para esto es llamar a los descriptores en una clase principal o hermana.

Tenga en cuenta que `super()` se implementa como parte del proceso de vinculación para búsquedas explícitas de atributos con puntos, como `super().__getitem__(name)`. Lo hace implementando su propio método `__getattribute__()` para buscar clases en un orden predecible que admite la herencia múltiple cooperativa. En consecuencia, `super()` no está definido para búsquedas implícitas que utilizan instrucciones u operadores como `super()[name]`.

También tenga en cuenta que, aparte de la forma de argumento cero, super() no se limita al uso de métodos internos. La forma de dos argumentos especifica exactamente los argumentos y hace las referencias apropiadas. La forma de argumento cero solo funciona dentro de una definición de clase, ya que el compilador completa los detalles necesarios para recuperar correctamente la clase que se está definiendo, además de acceder a la instancia actual para los métodos ordinarios.

Para sugerencias prácticas sobre cómo diseñar clases cooperativas usando `super()`, consulte la guía para usar `super()`.

### class tuple([iterable])
En lugar de ser una función, la tupla es en realidad un tipo de secuencia inmutable, como se documenta en Tuplas y tipos de secuencia — list, tuple, range.

### class type(object)
```python
class type(name, bases, dict, **kwds)
```

Con un argumento, devuelve el tipo de un objeto. El valor de retorno es un objeto de tipo y generalmente el mismo objeto que devuelve object.`__class__`.

Se recomienda la función integrada `isinstance()` para probar el tipo de un objeto, porque tiene en cuenta las subclases.

Con tres argumentos, devuelve un nuevo tipo de objeto. Esta es esencialmente una forma dinámica de la declaración de clase. La cadena de nombre es el nombre de la clase y se convierte en el atributo `__name__`. La tupla bases contiene las clases base y se convierte en el atributo `__bases__`; si está vacío, se añade el objeto, la base última de todas las clases. El diccionario dict contiene definiciones de atributos y métodos para el cuerpo de la clase; se puede copiar o ajustar antes de convertirse en el atributo `__dict__`. Las siguientes dos sentencias crean objetos de tipo idéntico:

```python
class X:
    a = 1

X = type('X', (), dict(a=1))
```

Consulte también Tipo de objetos.

Los argumentos de palabras clave proporcionados a la forma de tres argumentos se pasan a la maquinaria de la metaclase apropiada (generalmente `__init_subclass__()`) de la misma manera que lo harían las palabras clave en una definición de clase (además de la metaclase).

Consulte también Personalización de la creación de clases.

Modificado en la versión 3.6: las subclases de tipo que no anulan type.`__new__` ya no pueden usar la forma de un argumento para obtener el tipo de un objeto.

### vars([object])
Devuelve el atributo `__dict__` para un módulo, clase, instancia o cualquier otro objeto con un atributo `__dict__`.

Los objetos como módulos e instancias tienen un atributo `__dict__` actualizable; sin embargo, otros objetos pueden tener restricciones de escritura en sus atributos `__dict__` (por ejemplo, las clases usan tipos.MappingProxyType para evitar actualizaciones directas del diccionario).

Sin un argumento, vars() actúa como `locals()`. Tenga en cuenta que el diccionario local solo es útil para las lecturas, ya que se ignoran las actualizaciones del diccionario local.

Se genera una excepción `TypeError` si se especifica un objeto pero no tiene un atributo `__dict__` (por ejemplo, si su clase define el atributo `__slots__`).

### zip(*iterables)
Cree un iterador que agregue elementos de cada uno de los iterables.

Devuelve un iterador de tuplas, donde la i-ésima tupla contiene el i-ésimo elemento de cada una de las secuencias de argumentos o iterables. El iterador se detiene cuando se agota el iterable de entrada más corto. Con un único argumento iterable, devuelve un iterador de 1 tupla. Sin argumentos, devuelve un iterador vacío. Equivalente a:

```python
def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
```
El orden de evaluación de izquierda a derecha de los iterables está garantizado. Esto hace posible un modismo para agrupar una serie de datos en grupos de n longitudes usando zip(*[iter(s)]*n). Esto repite el mismo iterador n veces para que cada tupla de salida tenga el resultado de n llamadas al iterador. Esto tiene el efecto de dividir la entrada en fragmentos de n longitud.

`zip()` solo debe usarse con entradas de longitud desigual cuando no le importan los valores finales no coincidentes de los iterables más largos. Si esos valores son importantes, use `itertools.zip_longest()` en su lugar.

Se puede usar `zip()` junto con el operador * para descomprimir una lista:

```python
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)
[(1, 4), (2, 5), (3, 6)]
x2, y2 = zip(*zip(x, y))
x == list(x2) and y == list(y2)
```
### __import__(name, globals=None, locals=None, fromlist=(), level=0)
Nota Esta es una función avanzada que no se necesita en la programación Python diaria, a diferencia de `importlib.import_module()`.
Esta función es invocada por la declaración de importación. Se puede reemplazar (importando el módulo incorporado y asignándolo a `builtins.__import__`) para cambiar la semántica de la declaración de importación, pero se desaconseja encarecidamente hacerlo, ya que generalmente es más simple usar ganchos de importación (ver PEP 302) para lograr los mismos objetivos y no causa problemas con el código que asume que se está utilizando la implementación de importación predeterminada. También se desaconseja el uso directo de `__import__()` en favor de `importlib.import_module()`.

La función importa el nombre del módulo, potencialmente usando los globales y locales dados para determinar cómo interpretar el nombre en un contexto de paquete. La fromlist proporciona los nombres de los objetos o submódulos que deben importarse desde el módulo dado por nombre. La implementación estándar no usa su argumento local en absoluto, y usa sus globales solo para determinar el contexto del paquete de la declaración de importación.

level especifica si usar importaciones absolutas o relativas. 0 (el valor predeterminado) significa que solo realiza importaciones absolutas. Los valores positivos para el nivel indican el número de directorios principales para buscar en relación con el directorio del módulo que llama `__import__()` (ver PEP 328 para más detalles).

Cuando la variable de nombre tiene la forma paquete.módulo, normalmente se devuelve el paquete de nivel superior (el nombre hasta el primer punto), no el módulo nombrado por nombre. Sin embargo, cuando se proporciona un argumento fromlist no vacío, se devuelve el módulo nombrado por nombre.

Por ejemplo, la declaración import spam da como resultado un código de bytes similar al código siguiente:

```python
spam = __import__('spam', globals(), locals(), [], 0)
```
La instrucción import `spam.ham` da como resultado esta llamada:

```python
spam = __import__('spam.ham', globals(), locals(), [], 0)
```
Observe cómo `__import__()` devuelve el módulo de nivel superior aquí porque este es el objeto que está vinculado a un nombre por la declaración de importación.

Por otro lado, la declaración de `spam.ham` importa huevos, salchichas como salchichas da como resultado

```python
_temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
eggs = _temp.eggs
saus = _temp.sausage
```

Aquí, el módulo `spam.ham` se devuelve desde `__import__()`. Desde este objeto se recuperan los nombres a importar y se asignan a sus respectivos nombres.

Si simplemente desea importar un módulo (potencialmente dentro de un paquete) por nombre, use `importlib.import_module()`.

Modificado en la versión 3.3: ya no se admiten los valores negativos para el nivel (que también cambia el valor predeterminado a 0).

Modificado en la versión 3.9: cuando se utilizan las opciones de la línea de comandos -E o -I, ahora se ignora la variable de entorno `PYTHONCASEOK`.