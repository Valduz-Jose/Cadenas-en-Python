# Ejemplo de concatenacion de cadenas

# Operador +
nombre = "Juan"
apellido = "Valduz"
nombre_completo = nombre+" "+apellido
print(nombre_completo)

# usando el metodo print
edad = 28
print("Usando comas:", "Nombre",nombre_completo, "Edad", edad)

# f-strings
ciudad = "Tachira"
pais = "Venezuela"
profesion = "Ingeniero"
presentacion = f"Hola, mi nombre es {nombre_completo}, tengo {edad} años, soy {profesion} y vivo en {ciudad}, {pais}."
print(presentacion)
# incluso se pueden hacer operaciones dentro de las llaves
