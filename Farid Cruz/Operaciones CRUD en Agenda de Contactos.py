# Tienes la agenda: ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
# Realiza: (1) Agregar "Pedro Ruiz", (2) Buscar "Carlos Díaz" y mostrar posición, 
# (3) Modificar "Luis Torres" por "Luis Mendoza", (4) Eliminar "Ana García".

agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]

print(f"\nAgenda inicial: {agenda}") #["Ana García", "Luis Torres", "Carlos Díaz", "María López"]

# 1. Agregar "Pedro Ruiz"
agenda.append("Pedro Ruiz")
print(f"\nAgenda después de agregar a Pedro Ruiz: {agenda}") # ['Ana García', 'Luis Torres', 'Carlos Díaz', 'María López', 'Pedro Ruiz']

# 2. Buscar "Carlos Díaz" y mostrar posición
posicion = agenda.index("Carlos Díaz")
print(f"\nCarlos Díaz está en la posición {posicion}") # Carlos Díaz está en la posición 2

# 3. Modificar "Luis Torres" por "Luis Mendoza"
agenda[agenda.index("Luis Torres")] = "Luis Mendoza"
print(f"\nAgenda después de modificar a Luis Torres por Luis Mendoza: {agenda}") # ['Ana García', 'Luis Mendoza', 'Carlos Díaz', 'María López', 'Pedro Ruiz']

# 4. Eliminar "Ana García"
agenda.remove("Ana García") 

print(f"\nAgenda actualizada: {agenda}") # ['Luis Mendoza', 'Carlos Díaz', 'María López', 'Pedro Ruiz']
print()