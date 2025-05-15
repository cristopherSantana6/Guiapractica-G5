#Desarrolle un programa que registre el consumo energético de cuatro edificios del campus
#niversitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en
#tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y
#generar el promedio semanal correspondiente.
edificios = 4
turnos = 3
dias = 7

for edificio in range(edificios):
    print(f"Edificio {edificio + 1}")
    consumo_total_edificio = 0

    for dia in range(dias):
        print(f"  Día {dia + 1}")
        consumo_dia = 0

        for turno in range(turnos):
            consumo = float(input(f"    Ingrese el consumo de kilovatios para el turno {turno + 1}: "))
            consumo_dia += consumo
        
        consumo_total_edificio += consumo_dia

    promedio_semanal = consumo_total_edificio / dias
    print(f"\nEl consumo total del edificio {edificio + 1} fue: {consumo_total_edificio:.2f} kWh")
    print(f"El promedio semanal del edificio {edificio + 1} es: {promedio_semanal:.2f} kWh")
    print("--------------------------------------------------\n")
