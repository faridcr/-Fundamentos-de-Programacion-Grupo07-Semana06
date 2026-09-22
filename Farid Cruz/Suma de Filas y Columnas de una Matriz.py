# Dada la matriz 3×3: [[1,2,3],[4,5,6],[7,8,9]] — Calcular y mostrar la suma de cada fila y la suma de cada columna.
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

filas = len(matriz)
cols = len(matriz[0])

# Calcular e imprimir la suma de cada fila, una por una
print("Suma de filas:")
sumas_filas = []
for i in range(filas):
    suma_fila = sum(matriz[i])
    sumas_filas.append(suma_fila)
    print(f"Suma fila {i}: {suma_fila}")

# Calcular e imprimir la suma de cada columna, una por una
print("\nSuma de columnas:")
sumas_columnas = []
for j in range(cols):
    suma_columna = 0
    for i in range(filas):
        suma_columna += matriz[i][j]
    sumas_columnas.append(suma_columna)
    print(f"Suma col {j}: {suma_columna}")