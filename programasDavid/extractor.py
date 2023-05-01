# Pregunta al usuario su correoe elctronico
email = input("Escribe tu correo electronico: ").strip()

# Variable que guarda el nombre de usuario
user_name = email[:email.index("@")]

# Variable que guarda el dominio del correo
domain_name = email[email.index("@")+1:]

# Muestra el usuario y dominio del correo de forma independiente
output = "Tu usuario es '{}' y tu dominio es '{}'".format(user_name,domain_name)

# Mensaje
print(output)