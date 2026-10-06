
# Tienes la agenda: ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
# Realiza: (1) Agregar "Pedro Ruiz", (2) Buscar "Carlos Díaz" y mostrar posición, (3) Modificar "Luis Torres" por "Luis Mendoza", (4) Eliminar "Ana
# García".

agenda=["Ana Garcia","Luis Torres","Carlos Diaz","Maria Lopez"]

agenda.append("Pedro Ruiz")
agenda[1]="Luis Mendoza"
agenda.remove("Ana Garcia")

def buscar_lineal(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
         return i # retorna índice
    return -1



pos = buscar_lineal(agenda,"Carlos Diaz")
print(agenda)
print("Carlos Diaz esta en la posicion :",pos)