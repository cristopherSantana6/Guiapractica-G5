# Cantidad de días, stands y productos
# Programa para registrar ventas en una feria estudiantil de la UAM

# Constantes para días, stands y productos
DIAS = 3
STANDS_POR_DIA = 4
PRODUCTOS_POR_STAND = 3

# Variables para almacenar los totales
total_general = 0

# Bucle por cada día
for dia in range(1, DIAS + 1):
    print(f"\n--- Día {dia} ---")
    total_dia = 0

    # Bucle por cada stand del día
    for stand in range(1, STANDS_POR_DIA + 1):
        print(f"\nStand {stand}")
        total_stand = 0

        # Bucle por cada producto del stand
        for producto in range(1, PRODUCTOS_POR_STAND + 1):
            venta = float(input(f"Ingrese venta del producto {producto}: "))
            total_stand += venta

        # Mostrar resumen por stand
        print(f"Total vendido en el Stand {stand}: ${total_stand:.2f}")
        total_dia += total_stand

    # Mostrar resumen por día
    print(f"\nTotal vendido en el Día {dia}: ${total_dia:.2f}")
    total_general += total_dia

# Mostrar total general
print(f"\n=== Total General de la Feria ===")
print(f"${total_general:.2f}")

