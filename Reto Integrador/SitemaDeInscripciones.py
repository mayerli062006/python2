# Creamos la clase Curso
class Curso:

    # Constructor de la clase
    def __init__(self):

        # Creamos una lista vacía
        # Aquí vamos a guardar los estudiantes
        self.estudiantes = []

    # Método para inscribir estudiantes
    def inscribir(self, nombre, edad):

        # Verificamos que el estudiante sea mayor de 15 años
        if edad > 15:

            # Creamos un diccionario con los datos
            estudiante = {"nombre": nombre, "edad": edad}

            # Agregamos el estudiante a la lista
            self.estudiantes.append(estudiante)

            # Informamos que fue inscrito
            print(f"{nombre} fue inscrito correctamente.")

        else:

            # Si tiene 15 años o menos, no puede inscribirse
            print(f"{nombre} no puede inscribirse porque debe ser mayor de 15 años.")

    # Método para listar los estudiantes mayores de edad
    def listar_mayores_edad(self):

        # List comprehension
        # Recorremos la lista de estudiantes
        # y obtenemos solamente los nombres
        # de quienes tienen más de 18 años
        mayores = [
            estudiante["nombre"]
            for estudiante in self.estudiantes
            if estudiante["edad"] > 18
        ]

        # Devolvemos la lista
        return mayores


# Creamos un objeto de la clase Curso
curso = Curso()


# Inscribimos varios estudiantes
curso.inscribir("Mayerli", 20)
curso.inscribir("Carlos", 17)
curso.inscribir("Ana", 15)
curso.inscribir("Luis", 25)
curso.inscribir("Sofia", 18)


# Obtenemos los estudiantes mayores de 18 años
mayores = curso.listar_mayores_edad()


# Mostramos los estudiantes mayores de edad
print("Estudiantes mayores de 18 años:")

for nombre in mayores:
    print(nombre)
