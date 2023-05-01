# variable del texto sobre el que se van a contar las palabras
text = 'Este es un ejemplo de tipo texto del cual se va a contar el numero de palabras del que se compone'

# separador de cada palabra 
result = len(text.split())
#resultado
print("En esta cadena de texto hay: " + str(result) + " palabras")