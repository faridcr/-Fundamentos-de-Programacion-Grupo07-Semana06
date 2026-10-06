
# notas:[]   15 , 18, 12, 9, 17, 14, 20, 11, 16, 13
nota=[15,18,12,9,17,14,20,11,16,13]

total=sum(nota)/ len (nota)
alto=max(nota)
minimo=min(nota)
def aprobados(nota):
    apro=0
    for n in nota:
        if n>= 11:
             apro+=1
    return apro
        

print("el promedio de las notas es : ",total)
print("la nota mas alta es :",alto)
print("la nota mas baja es :",minimo)
print("aprobados",aprobados(nota))
    

