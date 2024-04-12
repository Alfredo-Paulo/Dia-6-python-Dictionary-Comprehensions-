n = 10

lista_pares = [2*i+2 for i in range(n)]
print(lista_pares)

[print(2*i+2) for i in range(n)]

valores = [0, 4, 5, 6, 7, 8, 9]
divisibles = [f"Divisible{valor}" if valor % 2 == 0 else f"No divisible{valor}" for valor in valores]
print(divisibles)

print(["Divisible" if valor % 2 == 0 else "No divisible" for valor in valores])

lista = ['Lechugas', 'Tomates', 5, 10, True, False, True, 'Papas', 5.1, 45.2, 1, 2, 0]
count_str = sum(1 for elemento in lista if isinstance(elemento, str))
print(count_str)

lista_str = [elemento for elemento in lista if isinstance(elemento, str)]
print(lista_str)
