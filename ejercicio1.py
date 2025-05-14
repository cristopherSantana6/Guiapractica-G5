#Ejercicio 1: Registro de asistencia académica Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por sección, así como el total general de la semana.

secciones = ['A', 'B', 'C']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

asistencias = {sec: [int(input(f"Asistencias {sec} - {dia}: ")) for dia in dias] for sec in secciones}

print("\nResumen de asistencias:")
total_general = 0
for sec in secciones:
    total = sum(asistencias[sec])
    total_general += total
    print(f"Sección {sec}: {total} asistencias")
print(f"Total general: {total_general}")
