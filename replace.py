# Sustituir en cadenas de texto
# Sirve para limpiesa de cadenas y plantillas
# texto.replace ("viejo","nuevo",veces)

mensaje = "Hola mundo, mundo"
nuevo = mensaje.replace("mundo", "Python")
print(nuevo)

# remplazar una sola vez
uno_solo = mensaje.replace("mundo", "Python", 1)
print(uno_solo)