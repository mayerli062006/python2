# Función para convertir kilómetros a millas
def km_a_millas(km):

    # Aplicamos la fórmula de conversión
    millas = km * 0.621

    # Devolvemos el resultado
    return millas


# Cantidad de kilómetros que queremos convertir
kilometros = 10

# Llamamos a la función
resultado = km_a_millas(kilometros)

# Mostramos el resultado
print(f"{kilometros} kilómetros equivalen a {resultado} millas")
