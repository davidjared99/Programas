loop = 1

while (loop < 10):

    # Todas las preguntas que se le realiza al usuario para que las conteste
    nombre = input("escribe tu nombre: ")
    sustantivo_plural = input("escribe un sustantivo en plural: ")
    numero = input("escribe una cantidad ")
    lugar= input("escribe tu lugar favorito: ")
    


    # Muestra historia basada en las entradas del usuario
    print ("------------------------------------------")
    print ("Esta es la historia de ",nombre,)
    print ("le gustaba coleccionar ", sustantivo_plural,",")
    print ("un día se encontro ", numero, "monedas en ",lugar,)
    print ("muy contento regreso ", nombre, "a su casa,")
    print ("pensando cuantos" ,sustantivo_plural, "agregaría a su colección.")
    print ("------------------------------------------")
    loop = loop + 1