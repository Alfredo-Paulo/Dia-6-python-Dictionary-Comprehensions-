for i in range(10):
    print(i)

for i in range (4,10):
    print(i)

for i in range(4,10,2):
    print(i)

# i=4
# while i < 10
#   print(i)
#   i = i + 2 

# print(range(4,10,5))
# a = [1,5,8,3,4]
# for elemento in a:
#   print(elemntos)
#
# texto = "hola mundo!"
# for caracter in texto:
# print(caracter)

frase = ['hola',' ',"Mundo",'!']
for palabra in frase:
    print(palabra)

sql = "SELECT * FROM tabla WHERE email like \'alfredoqvv@gmail.com' ; '"

diccionario = {"Nombre": "Carlos",
                "Apellido": "Santana",
                "Ocupación": "Guitarrista"
                }
for clave in diccionario.items():
            print(f"Mi {clave} es {valor}")