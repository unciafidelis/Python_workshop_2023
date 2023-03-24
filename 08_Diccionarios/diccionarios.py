# # # # # sintaxis
# # # # diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
# # # # print(diccionario['llave1']) # valor1
# # # # print(diccionario['llave4']) # valor4

# # # # person = {
# # # #     'nombre':'Alejandro',
# # # #     'morgan':'Morgan',
# # # #     'edad':250,
# # # #     'pais':'México',
# # # #     'habilidades':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
# # # #     'direccion':{
# # # #         'calle':'Barrio x',
# # # #         'zipcode':'02210'
# # # #     }
# # # # }
# # # # print(person.get('nombre')) # Alejandro
# # # # print(person.get('pais'))    # México
# # # # print(person.get('habilidades')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
# # # # print(person.get('city'))   # None

# # # person = {
# # #     'nombre':'Alejandro',
# # #     'morgan':'Morgan',
# # #     'edad':250,
# # #     'pais':'México',
# # #     'habilidades':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
# # #     'direccion':{
# # #         'calle':'Barrio x',
# # #         'zipcode':'02210'
# # #         }
# # # }
# # # person['job_title'] = 'Instructor'
# # # person['habilidades'].append('HTML')
# # # person['job_title'] = 1
# # # print(person)

# # # sintaxis
# # diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
# # print('valor1' in diccionario) # True
# # print('llave1' in diccionario) # False

# # # sintaxis
# # diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
# # diccionario.pop('llave1') # remueve el item llave1 
# # diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
# # diccionario['llave1'] = None
# # print(diccionario)
# # diccionario.popitem() # remueve el último item 
# # del diccionario['llave2'] # remueve el item llave2 

# # sintaxis
# diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
# print(diccionario.items()) # dict_items([('llave1', 'valor1'), ('llave2', 'valor2'), ('llave3', 'valor3'), ('llave4', 'valor4')])

# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
llaves = diccionario.keys()
print(llaves) 

# sintaxis
diccionario = {'llave1':'valor1', 'llave2':'valor2', 'llave3':'valor3', 'llave4':'valor4'}
valores = diccionario.values()
print(valores)  