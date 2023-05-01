
#variable que guarda la letra de cada cancion
canciones = {
    "1": "Spies: Letra de la canción 1",
    "2": "Everything's Not Lost: Letra de la canción 2",
    "3": "Parachutes: Letra de la canción 3",
    "4": "Yellow: Letra de la canción 4",
    "5": "Sparks: Letra de la canción 5",
    "6": "Shiver: Letra de la canción 6",
    "7": "Trouble: Letra de la canción 7",
    "8": "Don't Panic: Letra de la canción 8",
    "9": "High Speed: Letra de la canción 9",
    "10": "We Never change: Letra de la canción 10",
}

print("Selecciona una cancion de la playlist colocando el numero")
for key, value in canciones.items():
    print(key + ". " + value)
eleccion = input("Ingresa el número de la canción ")

if eleccion in canciones.keys():
    print("\nLetra de la canción seleccionada:\n" + canciones[eleccion])
else:
    print("Elige solo canciones del 1 al 10.")