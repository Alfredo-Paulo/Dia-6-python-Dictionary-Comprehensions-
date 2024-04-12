# Dada la información de ventas de 3 meses:
# 1. Convertir la tabla en un diccionario
# 2. Modificar el diccionario para incrementar las ventas en un 10%.
# 3. Hacer un nuevo diccionario pero con las ventas disminuidas un 20%.
# Mes Ventas
# Octubre 65000
# Noviembre 68000
# Diciembre 72000

# 1. Convertir la tabla en un diccionario
ventas = {
    "Octubre": 65000,
    "Noviembre": 68000,
    "Diciembre": 72000
}

# 2. Modificar el diccionario para incrementar las ventas en un 10%
for mes in ventas:
    ventas[mes] *= 1.1

# 3. Hacer un nuevo diccionario pero con las ventas disminuidas un 20%
ventas_disminuidas = {mes: ventas[mes] * 0.8 for mes in ventas}

print("Diccionario de ventas incrementadas en un 10%:")
print(ventas)
print("\nDiccionario de ventas disminuidas en un 20%:")
print(ventas_disminuidas)