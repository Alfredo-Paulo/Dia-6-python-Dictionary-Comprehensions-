import random
import sys

buscar = int(sys.argv[1])

lista = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista)

print(f'La lista mezclada es: {lista}')

for position, elemento in enumerate(lista):
    if elemento == buscar:
        print("Elemento encontrado")
        break
    else:
        print("Elemento no encontrado")

print("Ha terminado el ciclo")
print(f'El elemento {buscar} se encontró en la posición {position}')