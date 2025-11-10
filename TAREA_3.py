print("-----Perfil de datos-----")
Nombre = input("Ingresa tu nombre de usuario: ")
Año = int(input("Ingresa tu año de nacimiento: "))
Videojuegos = input("ingresa tus 3 videojuegos favoritos, separados por comas: ")
Perfil = [Nombre]
Edad= int(2025 - Año)
Perfil.append(Edad)
Juegos =Videojuegos.split(",")
Perfil.extend(Juegos)
Perfil.insert(0, True)
Juego_favorito = Perfil.pop(3)
#Comprobaciones lógiccas
es_mayor_de_edad = int(Perfil[2])>=18
nombre_largo = len(Perfil[1]) > 10
es_gamer_retro = Perfil.count("pacman") > 0
#mostrado en patanlla de los resultos
print("\n----Resultados----")
print("Perfil final: ", Perfil)
print("Juego favorito: ", Juego_favorito)
print(f"Es mayor de edad:  {es_mayor_de_edad} \nNombre largo: {nombre_largo} \nEs gamer retro: {es_gamer_retro} ")
print("TODO UN GAMER ;)")
print("By Alex1217z")
