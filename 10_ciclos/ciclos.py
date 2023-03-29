# numeros = [1, 1, 2, 3, 4, 5,6,7,8,9,0]
# i = 0
# for i in range(i,len(numeros),2): # el número es un nombre temporal para referirse a los elementos de la lista, válido solo dentro de este ciclo
#         print(numeros[i])

persona = {
    'nombre': 'Alejandro',
    'apellido': 'Morgan',
    'edad': 250,
    'pais': 'México',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print('###############################')
for llave in persona:
    if llave == 'skills':
        for skill in persona['skills']:
            print(skill)
        break
else:
    print("no esta")

