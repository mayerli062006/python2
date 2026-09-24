# Creamos la clase CarritoCompras
class CarritoCompras:

    # Constructor de la clase
    def __init__(self):

        # Creamos una lista vacía para almacenar productos
        self.productos = []

    # Método para agregar un producto
    def agregar_producto(self, nombre, precio):

        # Creamos un diccionario con el nombre y el precio
        producto = {"nombre": nombre, "precio": precio}

        # Agregamos el producto a la lista
        self.productos.append(producto)

    # Método para calcular el total
    def total(self):

        # Variable para almacenar la suma
        total = 0

        # Recorremos todos los productos
        for producto in self.productos:

            # Sumamos el precio de cada producto
            total += producto["precio"]

        # Devolvemos el total
        return total


# Creamos un carrito
carrito = CarritoCompras()

# Agregamos productos
carrito.agregar_producto("Camisa", 45000)
carrito.agregar_producto("Pantalón", 89000)
carrito.agregar_producto("Medias", 8000)

# Mostramos el total
print(f"El total de la compra es: ${carrito.total()}")
