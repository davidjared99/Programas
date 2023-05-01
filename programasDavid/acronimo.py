
#cadena de texto para el acronimo
cadena = "Facultad Contaduria Administración"
#separa cada palabra que compone la cadena de texto
palabras = cadena.split()
#aqui se guardara el acronimo
nueva_cadena = ""
#Se obtiene el primer elemento de cada palabra
for p in palabras:
    nueva_cadena = nueva_cadena + p[0]
#imprime el acronimo
print(nueva_cadena)

