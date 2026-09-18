# Dado el siguiente arreglo de notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
# Escribir un programa que calcule: promedio, nota más alta, nota más baja y cuántos aprobaron (nota ≥ 11).

def calcular_estadisticas(notas):
    promedio = sum(notas) / len(notas)
    nota_alta = max(notas)
    nota_baja = min(notas)
    aprobados = 0
    for nota in notas:
        if nota >= 11:
         aprobados += 1
    desaprobados = 0
    for nota in notas:
        if nota < 11:
         desaprobados += 1

    return promedio, nota_alta, nota_baja, aprobados, desaprobados

notas_alumnos = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
promedio, nota_alta, nota_baja, aprobados = calcular_estadisticas(notas_alumnos)

print("\n========== Estadísticas de Notas ==========")
print(f"Notas: {notas_alumnos}")
print(f"Promedio: {promedio:.2f}")
print("-" * 45)
print(f"Nota más alta: {nota_alta}")
print(f"Nota más baja: {nota_baja}")
print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")
print() 