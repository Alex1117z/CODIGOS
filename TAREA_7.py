estudiantes = {} #diccionario fachero
materias_validas = (
    "Resistencia de los materiales",
    "Control clásico",
    "Programación avanzada",
    "Circuitos Basicos",
    "Cálculo vectorial",
    "Mecánica"
)

def pedir_calificaciones():
    calificaciones = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Ingrese la calificación {i}: "))
                if 0 <= nota <= 10:
                    calificaciones.append(nota)
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Entrada inválida. Introduzca un número válido.")
    return calificaciones

def registrar_estudiante():
    print("\n--- Resgistro de Estudante ---")
    id_alumno = input("Ingrese el ID del alumno: ").strip()

    if id_alumno in estudiantes:
        print("Error: ese ID ya existe en el sistema.")
        return

    nombre = input("Ingrese el nombre del alumno: ").strip()

    print("\nMaterias válidas:")
    for materia in materias_validas:
        print(f" - {materia}")

    while True:
        materia = input("Ingrese la materia: ").strip()
        if materia in materias_validas:
            break
        else:
            print("Materia inválida. Intente nuevamente.")

    calificaciones = pedir_calificaciones()

    estudiantes[id_alumno] = {
        "nombre": nombre,
        "materia": materia,
        "calificaciones": calificaciones
    }

    print(f"\nAlumno '{nombre}' registrado exitosamente.\n")

def buscar_estudiante():
    print("\n--- Busqueda de Estudiante---")
    id_alumno = input("Ingrese el ID del alumno: ").strip()

    if id_alumno in estudiantes:
        datos = estudiantes[id_alumno]
        print(f"\nID: {id_alumno}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Materia: {datos['materia']}")
        print(f"Calificaciones: {datos['calificaciones']}")
    else:
        print("No se encontró ningún alumno con ese ID.")


def calcular_promedio():
    print("\n--- Cálculo de promedio ---")
    id_alumno = input("Ingrese el ID del alumno: ").strip()

    if id_alumno in estudiantes:
        notas = estudiantes[id_alumno]["calificaciones"]
        promedio = sum(notas) / len(notas)
        print(f"Promedio de {estudiantes[id_alumno]['nombre']}: {promedio:.2f}")
    else:
        print("No se encontró ningún alumno con ese ID.")

def ver_todos():
    print("\n--- Lista de Estudiantes inscritos ---")
    if not estudiantes:
        print("Aún no hay alumnos registrados.")
    else:
        for id_alumno, datos in estudiantes.items():
            print(f"ID: {id_alumno} | Nombre: {datos['nombre']} | Materia: {datos['materia']}")


def cursos_unicos():
    print("\n--- Cursos Únicos ---")
    materias_en_sistema = {datos["materia"] for datos in estudiantes.values()}
    if materias_en_sistema:
        print("Materias encontradas:")
        for materia in materias_en_sistema:
            print(f" - {materia}")
    else:
        print("No hay materias registradas todavía.")

print("Bienvenido al Sistema de Administración de Estudiambres")

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1) registrar")
    print("2) buscar")
    print("3) promedio")
    print("4) ver todos")
    print("5) cursos unicos")
    print("6) salir")

    opcion = input("Seleccione una opción: ").strip().lower()

    if opcion in ("1", "registrar"):
        registrar_estudiante()
    elif opcion in ("2", "buscar"):
        buscar_estudiante()
    elif opcion in ("3", "promedio"):
        calcular_promedio()
    elif opcion in ("4", "ver todos"):
        ver_todos()
    elif opcion in ("5", "cursos unicos"):
        cursos_unicos()
    elif opcion in ("6", "salir"):
        print("\nGracias por usar el sistema :) \n")
        break
    else:
        print("Opción inválida. Intente de nuevo.")





#wiwiwiwi este reto estaba feo
