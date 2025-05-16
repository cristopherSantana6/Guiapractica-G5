#Ejercicio 1: Registro de asistencia académica Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por sección, así como el total general de la semana.

# Definir las secciones y los días
secciones = ['A', 'B', 'C']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

# Inicializar el diccionario para almacenar las asistencias
asistencias = {seccion: [] for seccion in secciones}

# Registrar asistencias
for seccion in secciones:
    print(f"\nRegistro de asistencias para la Sección {seccion}:")
    for estudiante in range(1, 7):  # 6 estudiantes por sección
        asistencia_estudiante = []
        print(f"\nEstudiante {estudiante}:")
        for dia in dias:
            while True:
                entrada = input(f"  ¿Estuvo presente el {dia}? (1=Sí, 0=No): ")
                if entrada in ('1', '0'):
                    asistencia_estudiante.append(int(entrada))
                    break
                else:
                    print("  Entrada inválida. Por favor, ingrese 1 para presente o 0 para ausente.")
        asistencias[seccion].append(asistencia_estudiante)

# Calcular y mostrar los resultados
total_general = 0
print("\nResumen de asistencias:")
for seccion in secciones:
    print(f"\nSección {seccion}:")
    total_seccion = 0
    for idx, asistencia_estudiante in enumerate(asistencias[seccion], start=1):
        total_estudiante = sum(asistencia_estudiante)
        total_seccion += total_estudiante
        print(f"  Estudiante {idx}: {total_estudiante} días presente")
    print(f"Total de asistencias en la Sección {seccion}: {total_seccion}")
    total_general += total_seccion

print(f"\nTotal general de asistencias en la semana: {total_general}")