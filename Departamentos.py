ventas_totales = [
    ["Mes", "Departamento", "Ventas"],
    ["Agosto", "Ropa", 3000],
    ["Agosto", "Deportes", 1000],
    ["Agosto", "Jugueteria", 4000],
    ["Septiembre", "Ropa", 4000],
    ["Septiembre", "Deportes", 3000],
    ["Septiembre", "Jugueteria", 8000],
    ["Octubre", "Ropa", 2500],
    ["Octubre", "Deportes", 1500],
    ["Octubre", "Jugueteria", 4500],
    ["Noviembre", "Ropa", 3200],
    ["Noviembre", "Deportes", 1200],
    ["Noviembre", "Jugueteria", 1200],
    ["Diciembre", "Ropa", 5000],
    ["Diciembre", "Deportes", 2300],
    ["Diciembre", "Jugueteria", 2300],
    ["Enero", "Ropa", 4700],
    ["Enero", "Deportes", 2700],
    ["Enero", "Jugueteria", 6700],
    ["Febrero", "Ropa", 3400],
    ["Febrero", "Deportes", 1200],
    ["Febrero", "Jugueteria", 4400],
    ["Marzo", "Ropa", 2300],
    ["Marzo", "Deportes", 2100],
    ["Marzo", "Jugueteria", 2500],
    ["Abril", "Ropa", 4500],
    ["Abril", "Deportes", 4500],
    ["Abril", "Jugueteria", 2300],
    ["Mayo", "Ropa", 3670],
    ["Mayo", "Deportes", 7670],
    ["Mayo", "Jugueteria", 3670],
    ["Junio", "Ropa", 5300],
    ["Junio", "Deportes", 9300],
    ["Junio", "Jugueteria", 5600],
    ["Julio", "Ropa", 2000],
    ["Julio", "Deportes", 8000],
    ["Julio", "Jugueteria", 2300]
]

# Vaciar ventas de un departamento
departamento_a_vaciar = input("¿Qué departamento deseas vaciar? (Jugueteria, Ropa, Deportes): ")
for registro in ventas_totales[1:]:
    if registro[1] == departamento_a_vaciar:
        registro[2] = 0
print("\nVentas después de vaciar el departamento:")
for registro in ventas_totales:
    print(f"{registro[0]:<12} {registro[1]:<12} {registro[2]:<7}")

# agregar datos
mes_nuevo = input("\nIngresa el mes para el nuevo registro: ")
departamento_nuevo = input("Ingresa el departamento para el nuevo registro (Jugueteria, Ropa, Deportes): ")
ventas_nuevas = int(input("Ingresa las ventas para el nuevo registro: "))

ventas_totales.append([mes_nuevo, departamento_nuevo, ventas_nuevas])

# registros actualizados
print("\nVentas actualizadas:")
for registro in ventas_totales:
    print(f"{registro[0]:<12} {registro[1]:<12} {registro[2]:<7}")
