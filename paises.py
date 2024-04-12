# Tenemos un listado de países y la cantidad de usuarios por cada país en la
# siguiente tabla:
# País Cantidad de usuarios
# México 70
# Chile 50
# Argentina 55
# 1. Convertir la tabla mostrada en un diccionario.
# 2. Filtrar los países con menos de 60 usuarios.

usuarios_por_pais = {
    "México": 70,
    "Chile": 50,
    "Argentina": 55
}

paises_con_menos_de_60_usuarios = {pais: usuarios for pais, usuarios in usuarios_por_pais.items() if usuarios < 60}

print("Diccionario original:")
print(usuarios_por_pais)
print("\nPaises con menos de 60 usuarios:")
print(paises_con_menos_de_60_usuarios)