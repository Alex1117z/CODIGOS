print("Ejercicio tipo entrevista \n")
def eliminar_duplicados(lista):
    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)
    return nueva_lista


# Lista dada
lista = [1, 8 , 9, 7, 52, 78, 37, 13, 32, 2, 3, 8, 1, 44, 2, 9, 53, 54, 52, 7, 2, 1, 37, 13, 0, 1, 2, 3]


resultado = eliminar_duplicados(lista)
print(resultado)
print("\nBy Alex1217z")
