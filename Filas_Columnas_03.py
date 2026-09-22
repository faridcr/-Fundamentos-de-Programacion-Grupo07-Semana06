# Definimos la matriz 3x3 según el enunciado[cite: 3]
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Calculamos la suma de cada fila
sumas_filas = [sum(fila) for fila in matriz]

# Calculamos la suma de cada columna
num_filas = len(matriz)
num_cols = len(matriz[0])
sumas_cols = [
    sum(matriz[f][c] for f in range(num_filas)) for c in range(num_cols)
]

# Construimos el formato de salida requerido
texto_filas = " | ".join([f"fila {i}: {sumas_filas[i]}" for i in range(num_filas)])
texto_cols = " | ".join([f"col {i}: {sumas_cols[i]}" for i in range(num_cols)])

# Imprimimos el resultado final
print(f"Suma {texto_filas} || Suma {texto_cols}")