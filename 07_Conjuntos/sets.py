# lista = [1,1]
# tupla = (1,1)
#sets = set('1')
# frutas = {'plátano', 'plátano', 'naranja', 'mango', 'limón'}
#sets = {'item1', 'item2', 'item3', 'item4'}
#sets = set('1',1)
# sets = {1,1,2,1,1,0,False,2,True}
# sets
# print(sets)
# sintaxis

# st = {'item1', 'item2', 'item3', 'item4'}
# print("El conjunto st contiene item3? ", 'item3' in st) # El conjunto st contiene item3? True
# # sintaxis
# st = {'item1', 'item2', 'item3', 'item4'}
#st.add('item5')
# print(st)
# sintaxis
# st = {'item1', 'item2', 'item3', 'item4'}
# lista = ['item6','item7','item8']
# st.update(lista)
# print(st)
# sintaxis
# st.remove('item2')
# print(st)
# x = st.pop()  # elimina un elemento aleatorio del conjunto
# y = st.pop() 
# print(y,x)

# # sintaxis
# st = {'item1', 'item2', 'item3', 'item4'}
# st.clear()
# print(st)

# # sintaxis
# st = {'item1', 'item2', 'item3', 'item4'}
# del st

# print(st)

# # sintaxis
# # lst = ['item1', 'item2', 'item3', 'item4', 'item1']
# # st = set(lst) 
# # print(st)

# # sintaxis
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item5', 'item6', 'item7', 'item8'}
# st3 = st1.union(st2)
# print(st3)

# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item3', 'item2'}
# x = st1.intersection(st2) # {'item3', 'item2'}
# print(x)

# # sintaxis
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item1', 'item2','item3','item4','item5'}
# print(st2.issubset(st1)) # True
# print(st2.issuperset(st1)) # True

# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item2','item6'}
# significa (A\B)∪(B\A)
x = st2.difference(st1)
print(x)
y=st2.symmetric_difference(st1)
print(y) # {'item1', 'item4'}

# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item8'}
print(st2.isdisjoint(st1)) # False
