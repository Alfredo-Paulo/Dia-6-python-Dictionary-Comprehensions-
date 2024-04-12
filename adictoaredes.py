# Se tiene una lista con la cantidad de minutos usados en redes sociales de distintos
# usuarios.
# Se debe retornar una lista que clasifique todos los tiempos menores a 90 minutos
# como 'bien' y todos los tiempos mayores o iguales a 90 como 'mal'.
# El output debería ser algo similar a lo siguiente:
# [120, 50, 600, 30, 90, 10, 200, 0, 500]
# ['mal', 'bien', 'mal', 'bien', 'bien', 'bien', 'mal', 'bien', 'mal']

minutos_usados = [120, 50, 600, 30, 90, 10, 200, 0, 500]
clasificacion = ['mal' if tiempo >= 90 else 'bien' for tiempo in minutos_usados]
print(clasificacion)