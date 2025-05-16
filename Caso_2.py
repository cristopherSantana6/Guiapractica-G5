# Simulación del uso de computadoras en dos laboratorios
# Cada laboratorio tiene 5 filas y 4 columnas de computadoras = 20 computadoras por laboratorio

#  Contadores para el primer laboratorio 
ocupadas1 = 0  # Contador de computadoras ocupadas en laboratorio 1
libres1 = 0    # Contador de computadoras libres en laboratorio 1

print("Estado del Laboratorio 1:")

# Bucle para recorrer cada fila (5 filas)
for fila in range(5):
    # Bucle para recorrer cada columna (4 columnas por fila)
    for columna in range(4):
        # Validación de entrada: solo se aceptan 0 (libre) o 1 (ocupada)
        while True:
            entrada = input(f"Ingrese el estado de la computadora ({fila+1},{columna+1}) [1=ocupada, 0=libre]: ")
            if entrada == "0" or entrada == "1":
                estado = int(entrada)  # Convertimos a número solo si es válido
                break  # Salimos del bucle while si la entrada es correcta
            else:
                print("Entrada inválida. Por favor, ingrese solo 1 o 0.")  # Mensaje de error

        # Lógica para contar e imprimir estado
        if estado == 1:
            ocupadas1 += 1
            print("O", end=" ")  # Imprime 'O' para ocupada
        else:
            libres1 += 1
            print("L", end=" ")  # Imprime 'L' para libre
    print()  # Nueva línea después de cada fila

# --- Contadores para el segundo laboratorio ---
ocupadas2 = 0  # Contador de computadoras ocupadas en laboratorio 2
libres2 = 0    # Contador de computadoras libres en laboratorio 2

print("\nEstado del Laboratorio 2:")

# Repetimos el mismo proceso para el segundo laboratorio
for fila in range(5):
    for columna in range(4):
        # Validación de entrada para asegurar 0 o 1
        while True:
            entrada = input(f"Ingrese el estado de la computadora ({fila+1},{columna+1}) [1=ocupada, 0=libre]: ")
            if entrada == "0" or entrada == "1":
                estado = int(entrada)
                break
            else:
                print("Entrada inválida. Por favor, ingrese solo 1 o 0.")

        # Lógica de conteo e impresión visual
        if estado == 1:
            ocupadas2 += 1
            print("O", end=" ")
        else:
            libres2 += 1
            print("L", end=" ")
    print()

# --- Resumen final ---
print("\nResumen de uso:")
print("Laboratorio 1 - Ocupadas:", ocupadas1, ", Libres:", libres1)
print("Laboratorio 2 - Ocupadas:", ocupadas2, ", Libres:", libres2)
