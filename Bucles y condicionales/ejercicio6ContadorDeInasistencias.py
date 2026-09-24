# Lista de asistencias durante una semana
asistencias = [1, 1, 0, 1, 0, 0, 1]

# Variable que utilizaremos para contar las faltas
inasistencias = 0

# Recorremos la lista de asistencias
for asistencia in asistencias:

    # Si el valor es 0 significa que faltó
    if asistencia == 0:

        # Aumentamos el contador de inasistencias
        inasistencias += 1


# Mostramos la cantidad de faltas
print(f"El aprendiz tuvo {inasistencias} inasistencias.")


# Verificamos si tuvo más de 2 faltas
if inasistencias > 2:

    # Mostramos una alerta
    print("ALERTA: El aprendiz tiene demasiadas inasistencias.")

else:

    # Si tiene 2 o menos, no mostramos alerta
    print("El número de inasistencias está dentro del límite.")
