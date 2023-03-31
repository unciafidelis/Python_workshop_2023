# Programación Orientada a Objetos 

Antes de nada, empecemos con una introducción básica a la Programación Orientada a Objetos *POO* o *OOP* en inglés. Se trata de un paradigma de programación introducido en los años 1970s, pero que no se hizo popular hasta años más tarde.

Este modo o paradigma de programación nos permite organizar el código de una manera que se asemeja bastante a como pensamos en la vida real, utilizando las famosas *clases*. Estas nos permiten agrupar un conjunto de variables y funciones que veremos a continuación.

Cosas de lo más cotidianas como un coche o una persona pueden ser representadas con clases. Estas clases tienen diferentes características, que en el caso del coche podrían ser el modelo, la marca o el color. Llamaremos a estas características, atributos.

Por otro lado, las clases tienen un conjunto de funcionalidades o cosas que pueden hacer. En el caso del coche podría ser encender o acelerar. Llamaremos a estas funcionalidades métodos.

Por último, pueden existir diferentes tipos de coche. Podemos tener uno que sea marca Toyota o el coche del vecino que sea uno marca nissan. Llamaremos a estos diferentes tipos de coche objetos. Es decir, el concepto abstracto de coche es la clase, pero Toyota o cualquier otro coche particular será el objeto.

La programación orientada a objetos está basada en 6 principios o pilares básicos:

* Herencia
* Cohesión
* Abstracción
* Polimorfismo
* Acoplamiento
* Encapsulamiento

## Herencia

La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, compartiendo sus métodos y atributos. Además de ello, una clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos.

**Ejemplo:**

Definimos una clase padre:

```python
class Animal:
    pass
```

Creamos una clase hija que hereda de la padre:

```python
class Perro(Animal):
    pass
```
De hecho podemos ver como efectivamente la clase Perro es la hija de Animal usando __bases__
```python
print(Perro.__bases__)
# (<class '__main__.Animal'>,)
```

De manera similar podemos ver que clases descienden de una en concreto con __subclasses__.

```python
print(Animal.__subclasses__())
# [<class '__main__.Perro'>]
```

**Ejemplo2:**

```python
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

# Perro hereda de Animal
class Perro(Animal):
    pass

mi_perro = Perro('mamífero', 10)
mi_perro.describeme()
# Soy un Animal del tipo Perro

class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")
    def otra(self):
    	print("jalara?")

mi_perro = Perro('mamífero', 10)
mi_perro.otra()

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

mi_vaca = Vaca('mamífero', 10)
mi_vaca.describeme()
mi_vaca.hablar()

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")



```

## Cohesión

La cohesión hace referencia al grado de relación entre los elementos de un módulo. En el diseño de una función, es importante pensar bien la tarea que va a realizar, intentando que sea única y bien definida. Cuantas más cosas diferentes haga una función sin relación entre sí, más complicado será el código de entender. Existen por lo tanto dos tipos de cohesión:

* Por un lado tenemos la cohesión débil que indica que la relación entre los elementos es baja. Es decir, no pertenecen a una única funcionalidad.

* Por otro la cohesión fuerte, que debe ser nuestro objetivo al diseñar programas. 

La cohesión fuerte indica que existe una alta relación entre los elementos existentes dentro del módulo.

**Ejemplo:**

```python
# Mal. Cohesión débil
def suma():
    num1 = float(input("Dame primer número"))
    num2 = float(input("Dame segundo número"))
    suma = num1 + num2
    print(suma)

suma()
```
---

```python
# Bien. Cohesión fuerte
def suma(numeros):
    total = 0
    for i in numeros:
        total = total + i
    return total
```

## Abstracción

La abstracción es un termino que hace referencia a la ocultación de la complejidad intrínseca de una aplicación al exterior, centrándose sólo en como puede ser usada, lo que se conoce como interfaz. Si has oído hablar del enfoque caja negra, es un concepto muy relacionado. Dicho en otras palabras, la abstracción consiste en ocultar toda la complejidad que algo puede tener por dentro, ofreciéndonos unas funciones de alto nivel, por lo general sencillas de usar, que pueden ser usadas para interactuar con la aplicación sin tener conocimiento de lo que hay dentro.

Una analogía del mundo real podría ser la televisión. Se trata de un dispositivo muy complejo donde han trabajado gran cantidad de ingenieros de diversas disciplinas como telecomunicaciones o electrónica. ¿Os imagináis que para cambiar de canal tuviéramos que saber todos los entresijos del aparato?. Pues bien, se nos ofrece una abstracción de la televisión, un mando a distancia. El mando nos abstrae por completo de la complejidad de los circuitos y señales, y nos da una interfaz sencilla que con unos pocos botones podemos usar.

Algo muy parecido sucede en la programación orientada a objetos. Si tuviéramos una clase Televisor, en su interior podría haber líneas y líneas de código super complejas, pero una buena abstracción sería la que simplemente ofreciera los métodos encender(), apagar() y cambiar_canal() al exterior.

Un concepto relacionado con la abstracción, serían las clases abstractas o más bien los métodos abstractos. Se define como clase abstracta la que contiene métodos abstractos, y se define como método abstracto a un método que ha sido declarado pero no implementado. Es decir, que no tiene código.

Es posible crear métodos abstractos en Python con decoradores como @absttractmethod

A continuación veremos el decorador @property, que viene por defecto con Python, y puede ser usado para modificar un método para que sea un atributo o propiedad. 

El decorador puede ser usado sobre un método, que hará que actúe como si fuera un atributo.

**Ejemplo:**

```python
class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        return self.__mi_atributo
```

Como si de un atributo normal se tratase, podemos acceder a el con el objeto. y nombre.

```python
mi_clase = Clase("valor_atributo")
mi_clase.mi_atributo
# 'valor_atributo'
```

## Polimorfismo

El polimorfismo es uno de los pilares básicos en la programación orientada a objetos, por lo que para entenderlo es importante tener las bases de la POO y la herencia bien asentadas.

**Ejemplo:**

```python
class Animal:
    def hablar(self):
        pass
```

Por otro lado tenemos otras dos clases, Perro, Gato que heredan de la anterior. Además, implementan el método hablar() de una forma distinta.

```python
class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")
```

A continuación creamos un objeto de cada clase y llamamos al método hablar(). Podemos observar que cada animal se comporta de manera distinta al usar hablar().

```python
for animal in Perro(), Gato():
    animal.hablar()

# Guau!
# Miau!
```

En el caso anterior, la variable animal ha ido “tomando las formas” de Perro y Gato. Sin embargo, nótese que al tener tipado dinámico este ejemplo hubiera funcionado igual sin que existiera herencia entre Perro y Gato.

## Acoplamiento

El acoplamiento en programación (denominado coupling en Inglés) es un concepto que mide la dependencia entre dos módulos distintos de software, como pueden ser por ejemplo las clases. El acoplamiento puede ser de dos tipos:

* Acoplamiento débil, que indica que no existe dependencia de un módulo con otros. Esto debería ser la meta de nuestro software.

* Acoplamiento fuerte, que por lo contrario indica que un módulo tiene dependencias internas con otros.

**Ejemplo:**

```python
class Clase1:
    x = True
    pass

class Clase2:
    def mi_metodo(self, valor):
        if Clase1.x:
            self.valor = valor

mi_clase = Clase2()
mi_clase.mi_metodo("Hola")
mi_clase.valor
```

## Encapsulamiento

El encapsulamiento o encapsulación en programación es un concepto relacionado con la programación orientada a objetos, y hace referencia al ocultamiento de los estado internos de una clase al exterior. Dicho de otra manera, encapsular consiste en hacer que los atributos o métodos internos a una clase no se puedan acceder ni modificar desde fuera, sino que tan solo el propio objeto pueda acceder a ellos.

**Ejemplo:**

```python
class Clase:
    atributo_clase = "Hola"
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

mi_clase = Clase("Que tal")
mi_clase.atributo_clase
mi_clase.atributo_instancia
# 'Hola'
# 'Que tal'
```

Ambos atributos son perfectamente accesibles desde el exterior. Sin embargo esto es algo que tal vez no queramos. Hay ciertos métodos o atributos que queremos que pertenezcan sólo a la clase o al objeto, y que sólo puedan ser accedidos por los mismos. Para ello podemos usar la doble __ para nombrar a un atributo o método. Esto hará que Python los interprete como “privados”, de manera que no podrán ser accedidos desde el exterior.

```python
class Clase:
    atributo_clase = "Hola"   # Accesible desde el exterior
    __atributo_clase = "Hola" # No accesible

    # No accesible desde el exterior
    def __mi_metodo(self):
        print("Haz algo")
        self.__variable = 0

    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__mi_metodo()

mi_clase = Clase()
#mi_clase.__atributo_clase  # Error! El atributo no es accesible
#mi_clase.__mi_metodo()     # Error! El método no es accesible
mi_clase.atributo_clase     # Ok!
mi_clase.metodo_normal()    # Ok!
```
