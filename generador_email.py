# apartir de un nombre de usuario -> normalizamos 
# se debe normalizar el nombre de la empresa 
print("***Generador de Emails***")

# Nombre de usuario
nombre_completo = "Jose Alejandro Valduz"
print("Nombre completo:", nombre_completo)

# Normalizamos
# quitar espacios en blanco inicio y final
nombre_usuario = nombre_completo.strip()

# remplazar espacios por puntos
nombre_usuario = nombre_usuario.replace(" ", ".")

# convertir a minusculas
nombre_usuario = nombre_usuario.lower()
print("Nombre de usuario normalizado:", nombre_usuario)

# Datos empresa
nombre_empresa = "Valduzcorp"
print("Nombre de la empresa:", nombre_empresa)
extension_dominio = ".com.ve"

# Normalicemos el nombre de la empresa
nombre_empresa_normalizado = nombre_empresa.replace(" ", "").lower()
dominio_email_normalizado = f"@{nombre_empresa_normalizado}{extension_dominio}"
print("Dominio de email normalizado:", dominio_email_normalizado)

# creamos el email
email = f"{nombre_usuario}{dominio_email_normalizado}"
print("\nEmail generado:", email)