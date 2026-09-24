# porcentaje=10 significa que , si no enviamos un porcentaje , se utilizara automaticamente el 10%
def calcular_propina(cuenta, porcentaje=10):
    # calculamos la propina
    propina = cuenta * porcentaje / 100
    # devolvemos  el valor calculado
    return propina


# guardamos el valor de la cuenta
cuenta = 100000
# llamamos a la funcion sin enviar porcentaje  por lo tanto , utilizara el 10% por defecto.
resultado = calcular_propina(cuenta)
# mostramos el resultado
print(f"la propina es : ${resultado}")
