# Lista de edades de las personas
edades = [16, 20, 15, 30, 12, 25]

# Recorremos cada edad
for edad in edades:

    # Verificamos si la persona es mayor de 18
    if edad > 18:

        # Si cumple la condición, puede entrar
        print(f"Edad {edad}: Acceso permitido")

    else:

        # Si no cumple la condición, no puede entrar
        print(f"Edad {edad}: Acceso denegado")
