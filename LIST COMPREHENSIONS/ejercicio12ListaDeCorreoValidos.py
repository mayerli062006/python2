# Lista de correos
correos = ["maye@gmail.com", "luis", "carlos@gmail.com", "sena"]

# List comprehension para filtrar los correos
# Solo se guardan los que contienen "@"
correos_validos = [correo for correo in correos if "@" in correo]

# Mostramos los correos válidos
print(correos_validos)
