#Desarrolle un programa que registre el consumo energético de cuatro edificios del campus
#niversitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en
#tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y
#generar el promedio semanal correspondiente.

edificios = 4
estudiantes = 0
turnos = 3
Dias = 7
promedio_semanal = 0
consumo_total = 0

for edificio in range(edificios):
    print(f"edificio {edificio + 1}")
    for dia in range(7):
        print(f"dia {dia + 1}")
        for turno in range(turnos):
            print(f"turno {turno + 1}")
            consumo_total = 0
            consumo = int(input("Ingrese el consumo de kilovatios: "))
            consumo_total += consumo
            promedio_semanal += consumo_total
    promedio_semanal = promedio_semanal / Dias
    print(f"El promedio semanal del edificio {edificio + 1} es: {promedio_semanal}")
    promedio_semanal = 0
    consumo_total = 0
    print("")
    print("--------------------------------------------------")
    