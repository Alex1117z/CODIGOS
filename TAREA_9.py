print("-------------CONTROL DE CALIDAD DE COMPONENTES-------------")
print("---------Bienvenido al sistema de inspección de piezas------")

# Tupla global con los componentes válidos
COMPONENTES_VALIDOS = ("Motor", "Sensor", "Batería", "Chasis")

# Diccionario principal donde se almacenan las piezas
base_de_partes = {}

# ----------- FUNCIONES -----------

def registrar_parte():
    print("\n--- REGISTRO DE NUEVA PIEZA ---")
    sn = input("Ingresa el número de serie (ej: SN-1001): ").strip()
    if sn in base_de_partes:
        print("Error: Ese número de serie ya está registrado.")
        return

    tipo = input("Tipo de componente (Motor/Sensor/Batería/Chasis): ").capitalize()
    if tipo not in COMPONENTES_VALIDOS:
        print("Error: Tipo de componente no válido.")
        return

    resultados = []
    for i in range(3):
        while True:
            try:
                valor = float(input(f"Ingrese el resultado de la prueba {i+1} (0-100): "))
                if 0 <= valor <= 100:
                    resultados.append(valor)
                    break
                else:
                    print("El valor debe estar entre 0 y 100.")
            except ValueError:
                print("Error: Ingresa un número válido.")

    base_de_partes[sn] = {
        "tipo_componente": tipo,
        "resultados_pruebas": resultados,
        "estado": "Pendiente"
    }

    print("Pieza registrada exitosamente :)")

def buscar_parte():
    print("\n--- BÚSQUEDA DE PIEZA ---")
    sn = input("Ingresa el número de serie a buscar: ").strip()
    if sn in base_de_partes:
        parte = base_de_partes[sn]
        print(f"Número de Serie: {sn}")
        print(f"Tipo: {parte['tipo_componente']}")
        print(f"Resultados: {parte['resultados_pruebas']}")
        print(f"Estado: {parte['estado']}")
    else:
        print("No se encontró ninguna pieza con ese número de serie.")

def evaluar_parte():
    print("\n--- EVALUACIÓN DE PIEZA ---")
    sn = input("Ingresa el número de serie a evaluar: ").strip()
    if sn not in base_de_partes:
        print("Error: No se encontró esa pieza.")
        return

    parte = base_de_partes[sn]
    promedio = sum(parte["resultados_pruebas"]) / 3

    if promedio >= 90.0:
        parte["estado"] = "Aprobado"
    else:
        parte["estado"] = "Rechazado"

    print(f"Pieza evaluada. Promedio: {promedio:.2f} -> Estado: {parte['estado']}")

def ver_inventario():
    print("\n--- INVENTARIO DE PIEZAS ---")
    if not base_de_partes:
        print("No hay piezas registradas aún.")
        return
    for sn, parte in base_de_partes.items():
        print(f"S/N: {sn} - Tipo: {parte['tipo_componente']} - Estado: {parte['estado']}")

# Función recursiva para contar componentes de cierto tipo
def contar_componentes(lista_partes, tipo):
    if not lista_partes:
        return 0
    primera = lista_partes[0]
    resto = lista_partes[1:]
    if primera["tipo_componente"] == tipo:
        return 1 + contar_componentes(resto, tipo)
    else:
        return contar_componentes(resto, tipo)

def conteo():
    print("\n--- CONTEO DE COMPONENTES POR TIPO ---")
    tipo = input("Escribe el tipo de componente a contar: ").capitalize()
    if tipo not in COMPONENTES_VALIDOS:
        print("Error: Tipo no válido.")
        return
    total = contar_componentes(list(base_de_partes.values()), tipo)
    print(f"Total de piezas tipo {tipo}: {total}")

# ----------- BUCLE PRINCIPAL -----------
while True:
    print("\nOpciones disponibles:")
    print("registrar / buscar / evaluar / ver_inventario / conteo / salir")

    opcion = input("¿Qué deseas hacer?: ").lower().strip()

    if opcion == "registrar":
        registrar_parte()
    elif opcion == "buscar":
        buscar_parte()
    elif opcion == "evaluar":
        evaluar_parte()
    elif opcion == "ver_inventario":
        ver_inventario()
    elif opcion == "conteo":
        conteo()
    elif opcion == "salir":
        print("Cerrando sistema de QC... Gracias por usar :D")
        print("By Alex1217z")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")
