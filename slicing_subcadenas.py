# la forma de indicar subcadenas es texto[inicio:fin:paso] sin incluir el caracter de fin
# tambien se pueden usar indices negativos para contar desde el final de la cadena

texto = "PROGRAMACION"

# Basico [inicio:fin]
print(texto[0:4])  # Imprime "PROG"

# Atajo desde el inicio [:fin]
print(texto[:4])  # Imprime "PROG"

# Atajo hasta el final [inicio:]
print(texto[4:])  # Imprime "RAMACION"

#  indices negativos
print(texto[-3:])  # Imprime "ION"

# Pasos [::paso] (invertir la cadena)
print(texto[::-1])  # Imprime "NOICAMARGORP"

