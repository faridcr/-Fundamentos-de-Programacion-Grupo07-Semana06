# Definimos la agenda inicial
agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]

# (1) Agregar "Pedro Ruiz"
agenda.append("Pedro Ruiz")

# (2) Buscar "Carlos Díaz" y mostrar su posición
posicion = agenda.index("Carlos Díaz")
print(f"Posición de Carlos Díaz: {posicion}")

# (3) Modificar "Luis Torres" por "Luis Mendoza"
indice_luis = agenda.index("Luis Torres")
agenda[indice_luis] = "Luis Mendoza"

# (4) Eliminar "Ana García"
agenda.remove("Ana García")

# Mostrar la lista final de contactos
print(agenda)