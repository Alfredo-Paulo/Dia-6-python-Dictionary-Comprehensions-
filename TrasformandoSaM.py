# Se tiene una lista con la cantidad de segundos que demoraron algunos procesos.
# Se necesita una función para transformar todos los datos a minutos, (se requiere
# sólo la parte entera, la parte decimal se puede ignorar).
# seconds = [100, 50, 1000, 5000, 1000, 500]

def seconds_to_minutes(seconds):
    minutes = []
    for sec in seconds:
        minutes.append(sec // 60)  # Dividir entre 60 para obtener los minutos (parte entera)
    return minutes

# Ejemplo de uso
seconds = [100, 50, 1000, 5000, 1000, 500]
minutes = seconds_to_minutes(seconds)
print(minutes)
