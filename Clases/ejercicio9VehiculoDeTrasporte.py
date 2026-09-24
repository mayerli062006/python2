# Creamos la clase Vehiculo
class Vehiculo:

    # Constructor
    def __init__(self, placa, conductor, disponible):

        # Guardamos la placa
        self.placa = placa

        # Guardamos el nombre del conductor
        self.conductor = conductor

        # Guardamos si está disponible
        self.disponible = disponible


    # Método para cambiar el estado
    def cambiar_estado(self):

        # El operador not invierte el valor
        # True se convierte en False
        # False se convierte en True
        self.disponible = not self.disponible


# Creamos un vehículo disponible
vehiculo1 = Vehiculo("ABC123", "Carlos", True)

# Mostramos su estado inicial
print(f"Disponible: {vehiculo1.disponible}")

# Cambiamos el estado
vehiculo1.cambiar_estado()

# Mostramos el nuevo estado
print(f"Disponible: {vehiculo1.disponible}")