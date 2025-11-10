inventario = ["paneles solares", "traje espacial", "comida deshidratada", "herramientas"]
print("---|Sistema de Inventario de la estación espacial|---")
while True:
    print("\nMenú de opciones:")
    print("1. añadir")
    print("2. quitar")
    print("3. ver")
    print("4. inspeccionar")
    print("5. salir")
    opcion = input("\n¿Qué deseas hacer?: ").strip().lower() #.strip sirve para eliminar espacios 
    if opcion == "añadir" or opcion == "1":
        nuevo_item = input("¿Qué artículo deseas añadir?: ").strip()
        if nuevo_item:
            inventario.append(nuevo_item)
            print(f" '{nuevo_item}' ha sido añadido al inventario.")
        else:
            print("No se añadió ningún artículo (entrada vacía).")

    elif opcion == "quitar" or opcion == "2":
        item = input("¿Qué artículo deseas quitar?: ").strip()
        if item in inventario:
            inventario.remove(item)
            print(f" '{item}' ha sido eliminado del inventario.")
        else:
            print("Error: Ese ítem no existe en el inventario.")

    elif opcion == "ver" or opcion == "3":
        if len(inventario) == 0:
            print("El inventario está vacío.")
        else:
            print("\nInventario actual:")
            for a, articulo in enumerate(inventario, start=1):
                print(f"  {a}. {articulo}")#me costo mucho esta parte

    elif opcion == "inspeccionar" or opcion == "4":
        if len(inventario) == 0:
            print("No hay artículos para inspeccionar (inventario vacío).")
            continue
        try:
            numero = int(input("¿Qué número de ítem quieres inspeccionar?: "))
            if 1 <= numero <= len(inventario):
                print(f"Estás inspeccionando: '{inventario[numero - 1]}'")
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Error: Debes ingresar un número válido.")

    elif opcion == "salir" or opcion == "5":
        print("\nCerrando sistema de inventario. ¡Buen viaje!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")

    if opcion in ("añadir", "quitar", "inspeccionar"):
        print("\n Estado actual del inventario:")
        if len(inventario) == 0:
            print("   (Vacío)")
