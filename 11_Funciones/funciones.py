# # # # # # def generar_nombre_completo ():
# # # # # #     nombre = 'Alejandro'
# # # # # #     apellido = 'Morgan'
# # # # # #     espacio = ' '
# # # # # #     nombre_completo = nombre + espacio + apellido
# # # # # #     print(nombre_completo)

# # # # # # generar_nombre_completo () # Llamar la función

# # # # # # def agregar_dos_numeros ():
# # # # # #     numero_uno = 2
# # # # # #     numero_dos = 3
# # # # # #     total = numero_uno + numero_dos
# # # # # #     print(total)

# # # # # # ###########################

# # # # # # def generar_nombre_completo ():
# # # # # #     nombre = 'Alejandro'
# # # # # #     apellido = 'Morgan'
# # # # # #     espacio = ' '
# # # # # #     nombre_completo = nombre + espacio + apellido
# # # # # #     return nombre_completo

# # # # # # print(generar_nombre_completo())

# # # # # # def agregar_dos_numeros ():
# # # # # #     numero_uno = 2
# # # # # #     numero_dos = 3
# # # # # #     total = numero_uno + numero_dos
# # # # # #     return total

# # # # # # print(agregar_dos_numeros())

# # # # # ###################################

# # # # # def saludo (nombre):
# # # # #     mensaje = str(nombre) + ', bienvenido al taller de python!'
# # # # #     return mensaje

# # # # # print(saludo(2239572965398.355624574))
# # # # # print('############################')

# # # # # def agrega_diez(numero):
# # # # #     diez = 10
# # # # #     return numero + diez
# # # # # print(agrega_diez(90))

# # # # # def numero_al_cuadrado(x):
# # # # #     return x * x

# # # # # print(numero_al_cuadrado(2))

# # # # # def area_del_circulo (r):
# # # # #     PI = 3.14
# # # # #     area = PI * r ** 2
# # # # #     return area
# # # # # print(area_del_circulo(10))

# # # # # def suma_de_numeros(n):
# # # # #     total = 0
# # # # #     for i in range(n+1):
# # # # #         total+=i
# # # # #     return total
# # # # # print(suma_de_numeros(10)) # 55
# # # # # print(suma_de_numeros(100)) # 5050

# # # # def generar_nombre_completo (nombre, apellido):
# # # #     espacio = ' '
# # # #     nombre_completo = nombre + espacio + apellido
# # # #     return nombre_completo
# # # # print('Nombre completo: ', generar_nombre_completo('Alejandro','Morgan'))

# # # # def suma_dos_numeros (numero_uno, numero_dos):
# # # #     suma = numero_uno + numero_dos
# # # #     return suma
# # # # print('Suma de dos numeros: ', suma_dos_numeros(1, 9))

# # # # def calcular_edad (año_actual, año_nacimiento):
# # # #     edad = año_actual - año_nacimiento
# # # #     return edad

# # # # print('Edad: ', calcular_edad(2021, 1819))

# # # # def peso_de_objeto (masa, gavedad):
# # # #     peso = str(masa * gavedad)+ ' N' # el valor tiene que ser cambiado a una cadena primero
# # # #     return peso
# # # # print('Peso de un objeto en Newtons: ', peso_de_objeto(100, 9.81))

# # # def encuentra_numeros_iguales(n):
# # #     iguales = []
# # #     for i in range(n + 1):
# # #         if i > 0 and i % 2 == 0:
# # #             iguales.append(i)
# # #     return iguales
# # # print(encuentra_numeros_iguales(100))

# # def peso_de_objeto (masa=0, gavedad = 9.81):
# #     peso = str(masa * gavedad)+ ' N' # el valor tiene que ser cambiado a cadena primero
# #     return peso
# # print('peso de un objeto en newtons: ', peso_de_objeto()) # 9.81 - promedio de gavedad en la superficie de la Tierra
# # print('peso de un objeto en newtons: ', peso_de_objeto(100, 888)) # gravedad en la superficie de la Luna

# # x = 443

# def suma_todos_los_numeros(*numeros):
#     total = 0
#     for numero in numeros:
#         total += numero     # igual que total = total + num
#     return total
# print(suma_todos_los_numeros(2, 3, 5,1,23,43,4,45,5,4,3,3,4,3,3,3,3)) # 10

#Puedes pasar funciones como parametros

def numero_al_cuadrado (n):
    return n * n

def hacer_algo(f, x):
    return f(x)
print(hacer_algo(numero_al_cuadrado, 3)) # 9
