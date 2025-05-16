# Cantidad de días, stands y productos
# Programa para registrar ventas en una feria estudiantil de la UAM

# Constantes para días, stands y productos
DIAS = 3
STANDS_POR_DIA = 4
PRODUCTOS_POR_STAND = 3

total_general = 0 # Variables para almacenar los totales

for dia in range(1, DIAS + 1):  # Bucle por cada día
    print(f"\n--- Día {dia} ---")
    total_dia = 0

    for stand in range(1, STANDS_POR_DIA + 1):  # Bucle por cada stand del día
        print(f"\nStand {stand}")
        total_stand = 0

        for producto in range(1, PRODUCTOS_POR_STAND + 1):  # Bucle por cada producto del stand
            while True:
                entrada = input(f"Ingrese venta del producto {producto}: ")
                try:
                    venta = float(entrada)
                    if venta < 0:
                        print("Por favor, ingrese un número positivo.")
                    else:
                        break
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido.")
            total_stand += venta

        # Mostrar resumen por stand
        print(f"Total vendido en el Stand {stand}: ${total_stand:.2f}")
        total_dia += total_stand

    print(f"\nTotal vendido en el Día {dia}: ${total_dia:.2f}")    # Mostrar resumen por día
    total_general += total_dia

print(f"\n=== Total General de la Feria ===")   # Mostrar total general
print(f"${total_general:.2f}")