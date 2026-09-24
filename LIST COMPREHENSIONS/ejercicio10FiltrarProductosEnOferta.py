# Lista de productos
productos = [
    {"nombre": "Camisa", "precio": 45000},
    {"nombre": "Pantalón", "precio": 89000},
    {"nombre": "Media", "precio": 8000},
]

# List comprehension
# Recorremos cada producto
# y solamente guardamos el nombre
# cuando el precio sea menor a 50.000
productos_oferta = [
    producto["nombre"] for producto in productos if producto["precio"] < 50000
]

# Mostramos el resultado
print(productos_oferta)
