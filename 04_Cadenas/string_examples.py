# Cadenas

letra = 'P' # Una cadena puede ser un solo carácter o un montón de texto
print ("1.-",letra) # Ya conocemos esta linea - Imprime: P
print("2.-",len(letra)) # len() mide una cadena por su numero de caracteres - Imprime: 1
saludo = '¡Hola, mundo!' # La cadena puede ser una comilla simple, doble, triple simple o triple doble
print("3.-",saludo) # ¡Hola, Mundo!
print("4.-",len(saludo)) # 13
frase = "Taller de introducción al análisis de datos con python"
print ("5.-",frase) # Taller de introducción al análisis de datos con python

# Cadena multilínea
cadena_multilinea = '''Nos encontramos en el taller de
introducción al análisis de datos con python - Este párrafo es una
cadena que tiene multiples lineas y esta encerrada entre comillas simples'''
print ("6.-",cadena_multilinea) # El resultado es una cadena de multiples lineas:
'''
Nos encontramos en el taller de
introducción al análisis de datos con python - Este párrafo es una
cadena que tiene multiples lineas y esta encerrada entre comillas simples
'''

# Otra forma de hacer lo mismo
cadena_multilinea = """Nos encontramos en el taller de
introducción al análisis de datos con python - Este párrafo es una
cadena que tiene multiples lineas y esta encerrada entre comillas simples"""
print ("7.-",cadena_multilinea) # El resultado es una cadena de multiples lineas:
'''
Nos encontramos en el taller de
introducción al análisis de datos con python - Este párrafo es una
cadena que tiene multiples lineas y esta encerrada entre comillas simples
'''

# Concatenación de cadenas
nombre = 'Alejandro'
apellido = 'Morgan'
espacio = ' '
nombre_completo = nombre + espacio + apellido
print("8.-",nombre_completo) # Alejandro Morgan
# Verificando la longitud de una cadena usando la función incorporada len()
print ("9.-",len (nombre)) # 9
print ("10.-",len (apellido)) # 6
print("11.-",len(nombre) > len(apellido)) # True
print("12.-",len(nombre_completo)) # 16

#### Descomprimiendo caracteres
lenguaje = 'Python'
a,b,c,d,e,f = lenguaje # desempaquetar caracteres de secuencia en variables
print ("13.-",a) # P
print ("14.-",b) # y
print ("15.-",c) # t
print ("16.-",d) # h
print ("17.-",e) # o
print ("18.-",f) # n

# Acceder a caracteres en cadenas por índice
lenguaje = 'Python'
primera_letra = lenguaje[0]
print ("19.-",primera_letra) # P
segunda_letra = lenguaje[1]
print ("20.-",segunda_letra) # y
ultimo_indice = len(lenguaje) - 1
ultima_letra = lenguaje[ultimo_indice]
print ("21.-",ultima_letra) # n

# Si queremos comenzar desde el extremo derecho, podemos usar la indexación negativa. -1 es el último índice
lenguaje = 'Python'
ultima_letra = lenguaje[-1]
print ("22.-",ultima_letra) # n
segundo_ultimo = lenguaje[-2]
print ("23.-",segundo_ultimo) # o

# Split

lenguaje = 'Python'
primeros_tres = lenguaje[0:3] # comienza en cero el índice y hasta 3
ultimos_tres = lenguaje[3:6]
print ("24.-",ultimos_tres) # hon
# De otra manera
ultimos_tres = lenguaje[-3:]
print ("25.-",ultimos_tres) # hon
ultimos_tres = lenguaje[3:]
print ("26.-",ultimos_tres) # hon

# Saltar caracteres al dividir cadenas de Python
idioma = 'Python'
po = idioma[0:6:3] 
print("27.-",po) #Po

# Secuencia de escape
print("28.-",'Este fin de semana es para perderse en una cabaña en una isla privada. \n ¿si o no?') # salto de línea
print("29.-",'Días\tTemas\tEjercicios') #Tabulación
print("30.-",'Día 1\t3\t5')
print("31.-",'Día 2\t3\t5')
print("32.-",'Día 3\t3\t5')
print("33.-",'Día 4\t3\t5')
print("34.-",'Este es un símbolo de barra invertida (\\)') # Para escribir una barra invertida
print("35.-",'En todos los lenguajes de programación comienza con \"¡Hola, mundo!\"') #Para escribir comillas dobles dentro de comillas simples

## Métodos de cadena
# capitalize(): Convierte el primer carácter de la cadena a Mayúscula

taller = 'introducción al análisis de datos con python'
print("36.-",taller.capitalize()) # 'Introducción al análisis de datos con python'

# count(): devuelve ocurrencias de subcadena en cadena, count(subcadena, inicio=.., final=..)

taller = 'introducción al análisis de datos con python'
print("37.-",taller.count('y')) # 1
print("38.-",taller.count('y', 7, 14)) # 0
print("39.-",taller.count('th')) # 1

# endswith (): verifica si una cadena termina con un final específico y devuelve un bool (True/False)

taller = 'introducción al análisis de datos con python'
print("40.-",taller.endswith('on')) # True
print("41.-",taller.endswith('ción')) # False

# expandtabs (): reemplaza el carácter de tabulación con espacios, el tamaño de tabulación predeterminado es 8. Toma el argumento de tamaño de tabulación

taller = 'introducción\tal\tanálisis\tde\tdatos\tcon\tpython'
print("42.-",taller.expandtabs())   # introducción    al      análisis        de      datos   con     python
print("43.-",taller.expandtabs(10)) # introducción        al        análisis  de        datos     con       python

# find(): Devuelve el índice de la primera aparición de la subcadena

taller = 'introducción al análisis de datos con python'
print ("44.-",taller.find ('o')) # 4
print ("45.-",taller.find ('th')) # 40

# format() formatea la cadena en una salida más agradable
nombre = 'Alejandro'
apellido = 'Morgan'
trabajo = 'Estudiante de Doctorado'
pais = 'México'
oracion = 'Soy {} {}. Soy un {}. Vivo en {}.'.format(nombre, apellido, trabajo, pais)
print("46.-",oracion) # Soy Alejandro Morgan. Soy un Estudiante de Doctorado. Vivo en México.
radius = 10
pi = 3.14
area = pi * (radius ** 2)
resultado = 'El área del círculo con {} de radius es {}'.format(str(radius), str(area))
print("47.-",resultado) # El área del círculo con 10 de radius es 314.0

# index(): Devuelve el índice de la subcadena
taller = 'introducción al análisis de datos con python'
print("48.-",taller.find('y')) # 39
print("49.-",taller.find('th')) # 40

# isalnum(): Comprueba caracteres alfanuméricos

taller = 'IntroducciónAlAnálisisDeDatosConPython'
print("50.-",taller.isalnum()) # True

taller = 'IntroducciónAlAnálisisDeDatosConPython2023'
print("51.-",taller.isalnum()) # True

taller = 'introducción al análisis de datos con python'
print("52.-",taller.isalnum()) # False

taller = 'introducción al análisis de datos con python'
print("53.-",taller.isalnum()) # False

# isalpha(): Comprueba si todos los caracteres son alfabetos

taller = 'introducción al análisis de datos con python'
print("54.-",taller.isalpha()) # False
numero = '123'
print("55.-",numero.isalpha()) # False

# isdecimal(): Comprueba los caracteres decimales

taller = 'introducción al análisis de datos con python'
print("56.-",taller.find('o')) # 4
print("57.-",taller.find('th')) # 40

# isdigit(): Comprueba los caracteres de los dígitos

taller = 'Treinta'
print("58.-",taller.isdigit()) # False
taller = '30'
print("59.-",taller.isdigit()) # True

# isdecimal(): Comprueba los caracteres decimales

numero = '10'
print("60.-",numero.isdecimal()) # True
numero = '10.5'
print("61.-",numero.isdecimal()) # False


# isidentifier(): comprueba si hay un identificador válido, lo que significa que comprueba si una cadena es un nombre de variable válido

taller = '1ntroducciónAlAnálisisDeDatosConPython'
print("62.-",taller.isidentifier()) # False, porque comienza con un numero
taller = 'introducción_al_análisis_de_datos_con_python'
print("63.-",taller.isidentifier()) # True


# islower(): Comprueba si todos los alfabetos en una cadena están en minúsculas

taller = 'introducción al análisis de datos con python'
print("64.-",taller.islower()) # True
taller = 'Introducción al análisis de datos con python'
print("65.-",taller.islower()) # False

# isupper(): devuelve si todos los caracteres están en mayúsculas

taller = 'introducción al análisis de datos con python'
print("66.-",taller.isupper()) # False
taller = 'introducción al análisis de datos con python'
print("67.-",taller.isupper()) # False


# isnumeric(): Comprueba los caracteres numéricos

numero = '10'
print("68.-",numero.isnumeric()) # True
print("69.-",'diez'.isnumeric()) # False

# join(): Devuelve una cadena concatenada

tecnologia_web = ['HTML', 'CSS', 'JavaScript', 'React']
resultado = '#, '.join(tecnologia_web)
print ("70.-",resultado) # HTML# CSS# JavaScript# React
# strip(): elimina los caracteres iniciales y finales

taller = 'introducción al análisis de datos con python'
print("71.-",taller.strip('i')) # ntroducción al análisis de datos con python

# replace (): reemplaza la subcadena dentro

taller = 'introducción al análisis de datos con python'
print("72.-",taller.replace('python', 'codificación en python')) # introducción al análisis de datos con codificación en python

# split(): Divide la cadena desde la izquierda

taller = 'introducción al análisis de datos con python'
print("73.-",taller.split()) # ['introducción', 'al', 'análisis', 'de', 'datos', 'con', 'python']

# title(): devuelve una cadena de título en mayúsculas y minúsculas

taller = 'introducción al análisis de datos con python'
print("74.-",taller.title()) # Introducción Al Análisis De Datos Con Python

# swapcase(): Cambia de mayuscula a minuscula y viceversa
  
taller = 'introducción al análisis de datos con python'
print("75.-",taller.swapcase()) # INTRODUCCIÓN AL ANÁLISIS DE DATOS CON PYTHON
taller = 'introdUcción aL análIsis de daTos con pYthon'
print("76.-",taller.swapcase()) # INTRODuCCIÓN Al ANÁLiSIS DE DAtOS CON PyTHON

# startswith(): verifica si la cadena comienza con la cadena especificada

taller = 'introducción al análisis de datos con python'
print("77.-",taller.startswith('introducción')) # True
taller = 'introducción al análisis de datos con python'
print("78.-",taller.startswith('análisis')) # False