# Definimos la lista de notas según el enunciado
notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]

# Calculamos las estadísticas solicitadas
promedio = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)
aprobados = sum(1 for nota in notas if nota >= 11)

# Mostramos los resultados en pantalla con el formato exacto de la salida
print("--- REPORTE DE ESTADÍSTICAS ---")
print(f"• Promedio de notas : {promedio}")
print(f"• Calificación más alta: {nota_maxima}")
print(f"• Calificación más baja: {nota_minima}")
print(f"• Total de aprobados   : {aprobados}")
print("-------------------------------")