import random
#variable que ocultara un numero aleatorio asignado  
n=random.randrange(10)
#preguntamos al usuario por un numero
nu=int(input('Escribe el posible nuemro oculto: '))
#miestras no adivine el numero, seguira preguntando
while nu!=n:
    if nu>n:
        nu=int(input('El número es mas pequeño'))
    elif nu<n:
        nu=int(input('El número es mas grande'))
print('Haz encontrado el numero, el cual era: ',n)