print("-----Análisis de calificaciones-----")
alumnos = int(input("ingreses la cantidad de alumnos: ")) 
#Listas
Nombres = []
Calificaciones= []
for alumno in range(alumnos):
    nombre = input(f"\nNombre del alumno {alumno+1}: ")
    calificacion = float(input(f"Calificación de {nombre}: "))
    Nombres.append(nombre)
    Calificaciones.append(calificacion)
Aprobados=[]
Reprobados=[]
Excelentes= []
suma_calificaciones = 0.0  # acumulador
for calificacion in Calificaciones:
    suma_calificaciones = suma_calificaciones + calificacion
promedio_grupo= suma_calificaciones / len(Calificaciones)
#clasificación de alumnos por calif
for a in range(alumnos):
    if Calificaciones[a]<5:
        Reprobados.append(Nombres[a])
    elif Calificaciones[a]>= 6 and Calificaciones [a]<10:
        Aprobados.append(Nombres[a])
    elif Calificaciones [a] == 10:
        Excelentes.append(Nombres[a])
print("\n-----Reporte de calificaciones-----")
print("Número total de estudiantes: ", alumnos)
print("Promedio del salón: ", promedio_grupo)
print("Calificación mas baja: ", min(Calificaciones)) 
#honestamente estos dos de min y max los investigue 
print("Calificación mas alta: ",max(Calificaciones))
print("Lista de Excelentes: ", Excelentes)
print("Lista de Aprobados: ", Aprobados)
print("Lista de Reprobados: ", Reprobados)
print("Gracias por ejecutar ^^")
print("By Alex1217z")
