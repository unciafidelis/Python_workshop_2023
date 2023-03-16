import re
frase = "juanito@hotmail.com.mx"
patron = '[0-9]+' #Esta es una expresión regular
exp_final = re.findall(patron, frase)
print(exp_final)
print(type(exp_final))
