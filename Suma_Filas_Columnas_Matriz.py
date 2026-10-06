matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Suma de cada fila
print("Suma de filas:")
for i in range(len(matriz)):
    suma_fila = 0
    for numero in matriz[i]:
        suma_fila += numero
    print(f"  Fila {i}: {suma_fila}")

# Suma de cada columna
print("Suma de columnas:")
for col in range(3):  # 3 columnas
    suma_columna = 0
    for fila in range(3):  # recorremos las 3 filas
        suma_columna += matriz[fila][col]
    print(f"  Columna {col}: {suma_columna}")