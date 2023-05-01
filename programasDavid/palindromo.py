igual, aux = 0, 0
#variable que guarda palabra a evaluar
texto = input("Ingrese la palabra: ")
for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1
if len(texto) == igual:
  print("La palabra es palindromo")
else:
  print("La palabra no es palindromo")