#Ejercicios de tuplas

mixed_type = ('C',0,0,'K',1,'E')

for i in mixed_type:
    print(i,":",type(i))

################################

#Listas contra tuplas

#Agregar un elemento a una tupla
numbers_tuple = (1,2,3,4,5)

'''
La línea siguiente de código va a provocar un error. 

Comentar la siguiente línea para continuar la ejecución 
del código sin errores.
'''
#numbers_tuple.append(6)
print('Esto es una tupla: ',numbers_tuple)

#Agregar un elemento a una lista
numbers_list = [1,2,3,4,5]
numbers_list.append(6)
numbers_list.append(7)
numbers_list.append(8)
numbers_list.remove(7)
print('Esto es una lista: ',numbers_list)

'''
Pero, ¿por qué usarías tuplas si son inmutables?

Bueno, no solo brindan acceso de "solo lectura" 
a los valores de los datos, sino que también son más 
rápidos que las listas. Considere las siguientes piezas 
de código:
'''
import timeit

#Tiempo de ejecución de una tupla
print('Tiempo de ejecución de la tupla x=(1,2,3,4,5,6,7,8,9) es: ',timeit.timeit('x=(1,2,3,4,5,6,7,8,9)', number=100000))

#Tiempo de ejecución de una lista
print('Tiempo de ejecución de la lista x=[1,2,3,4,5,6,7,8,9] es: ',timeit.timeit('x=[1,2,3,4,5,6,7,8,9]', number=100000))


################################



