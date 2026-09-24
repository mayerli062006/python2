# Lista de temperaturas en Celsius
temperaturas = [18, 22, 25, 19, 30]

# Convertimos cada temperatura a Fahrenheit
# utilizando una list comprehension
temperaturas_fahrenheit = [temperatura * 9 / 5 + 32 for temperatura in temperaturas]

# Mostramos las temperaturas convertidas
print(temperaturas_fahrenheit)
