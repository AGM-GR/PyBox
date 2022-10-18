igual, aux = 0, 0
texto = input("Palabra para comprobar: ")
for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1
if len(texto) == igual:
  print("Si es palindromo")
else:
  print("Lo siento. El texto no es palindromo")
