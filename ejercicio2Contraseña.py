# funcion que recibe una contraseña
def es_valida(contraseña):
    # len ()cuenta cuantos caracteres tiene la contraseña
    if len(contraseña) >= 8:
        # si tiene 8 o mas caracteres, devolvemos true
        return True
    else:
        # si tiene menos de 8 caracteres , devolvemos false
        return False
    # creamos una contraseña para probar


contraseña = "python123"
# llamamos a la funcion
resultado = es_valida(contraseña)
# mostramos el resultado
print(f"¿la contraseña es valida?: {resultado}")

