print("-------------CUADERNO DE LABORATORIO-------------")
print("---------Bienvenido a tu registro de laboratorio------")

# Tupla global con los tipos válidos
TIPOS_ENTRADA_VALIDOS = ("Observación", "Prueba", "Error", "Mantenimiento")

# Nombre del archivo donde se guardarán los registros
ARCHIVO_LOG = "laboratorio.txt"

# ---------- FUNCIONES ----------

def registrar_entrada():
    print("\n--- NUEVA ENTRADA DE LABORATORIO ---")
    tipo = input("Tipo de entrada (Observación/Prueba/Error/Mantenimiento): ").capitalize()

    if tipo not in TIPOS_ENTRADA_VALIDOS:
        print("Error: Tipo de entrada no válido. Intenta nuevamente.")
        return

    descripcion = input("Descripción de la entrada: ").strip()

    try:
        with open(ARCHIVO_LOG, "a", encoding="utf-8") as f:
            f.write(f"TIPO: {tipo} - DESCRIPCIÓN: {descripcion}\n")
        print("Entrada registrada exitosamente :)")
    except Exception as e:
        print("Ocurrió un error al guardar la entrada:", e)

def ver_log():
    print("\n--- HISTORIAL DEL LABORATORIO ---")
    try:
        with open(ARCHIVO_LOG, "r", encoding="utf-8") as f:
            contenido = f.read()
            if contenido.strip() == "":
                print("El log está vacío por ahora.")
            else:
                print(contenido)
    except FileNotFoundError:
        print("El log está vacío o no se ha creado aún.")
    except Exception as e:
        print("Error al leer el archivo:", e)

def main():
    while True:
        print("\nOpciones disponibles:")
        print("registrar / ver_log / salir")

        opcion = input("¿Qué deseas hacer?: ").lower().strip()

        if opcion == "registrar":
            registrar_entrada()
        elif opcion == "ver_log":
            ver_log()
        elif opcion == "salir":
            print("Cerrando el cuaderno de laboratorio... Gracias por usar :D")
            print("By Alex1217z")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
