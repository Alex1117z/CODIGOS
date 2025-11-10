print("-------------GESTIÓN DE COMPRAS------------")
lista = ["Leche","Pan","Manzanas"]
print("------Bienvenido a tu lista de compras-----")
print("Opciones disponibles: \nañadir / quitar / REvisar")
Decision=input("¿que deseas hacer? ")
if Decision.lower() == "añadir":
    articulo=str(input("¿Que articulo desea añadir a la lista? "))
    lista.append(articulo)
    print("Articulo añadido a la lista :)")
    print("Lista actual: ", lista)
elif Decision.lower() == "quitar":
    articulo=str(input("Escribe el articulo que deseas remover: ")).capitalize()
    lista.remove(articulo)
    print("Articulo remoivido correctamente :D")
    print("Lista actual: ", lista)
elif Decision.lower() == "revisar":
    print(" Tu lista actual es: ", lista)
else:
    print("Opcion no válida. Favor de escribir añadir, quitar o revisar..")
print("GRacias por usarme!, vuelve pronto :^")
print("By Alex1217z")