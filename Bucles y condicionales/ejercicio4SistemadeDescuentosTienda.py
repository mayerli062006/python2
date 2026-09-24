# Lista de precios de los productos
precios = [45000, 120000, 8000, 300000]

# Recorremos cada precio de la lista
for precio in precios:

    # Verificamos si el precio es mayor a 100.000
    if precio > 100000:

        # Calculamos el 15% de descuento
        descuento = precio * 0.15

        # Restamos el descuento al precio original
        precio_final = precio - descuento

    else:

        # Si no supera los 100.000,
        # no se aplica descuento
        precio_final = precio

    # Mostramos el precio final
    print(f"Precio final: ${precio_final}")
