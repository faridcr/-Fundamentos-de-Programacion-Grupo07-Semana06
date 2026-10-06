
# Dado el siguiente arreglo de notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
# Escribir un programa que calcule: promedio, nota más alta, nota más baja y cuántos aprobaron (nota ≥ 11)

notas=[]

def agregar_nota(n):
    notas.append(n)
    
def promedio_notas(notas):
    total=sum(notas)/len(notas)
    return total

def nota_max(notas):
    return max(notas)
    
def nota_min(notas):
   return min(notas)
    

def aprobados(notas):
    return sum(1 for n in notas if n >= 11)

cantidad=int(input("ingrese la cantidad de notas a evaluar : "))
for i in range (cantidad):
    while True:
        n=float(input("ingrese las notas : "))
        if 0<=n<=20:
            agregar_nota(n)
            break   
        else :
            print("ingrese una nota valida entre 0 y 20 ") 
        
    

    
print ("notas ingresadas ",notas)
print("el promedio de las notas es : " , promedio_notas(notas))
print("la nota maxima es :",nota_max(notas))
print("la nota minima es :",nota_min(notas))
print("aprobaron ",aprobados(notas))
    
    