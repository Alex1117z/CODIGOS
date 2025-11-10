class Personaje:
    #pass indica queno haga nada de momento.
    #lo siguiente son los atributos
    #nombre= "Default"
    #fuerza = 0
    #inteligencia =0
    #defensa = 0 
    #defensa =0 
    #vida =0
#las sigueinte 5 lineas son el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre =nombre
        self.defensa =defensa
        self.inteligencia =inteligencia
        self.fuerza=fuerza
        self.vida = vida
    #lo siguiente va a ser el estado del objeto:
    #self para que tenga acceso a los atributos
    #este metodo sivre para ver los atributos
    def atributos(self):
        print(self.nombre, ":", sep="")
        print(".Fuerza: ", self.fuerza)
        print(".inteligencia: ", self.inteligencia)
        print(".defensa: ", self.defensa)
        print(".vida", self.vida)
    #creación de un método :) que va a subir de nivel:
    #self porque vamos a modificar los atributos
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    #metodo para saber si esta vivo mazinger
    def esta_vivo (self):
        return self.vida > 0 
    #metodo para enseñar que murio mazinger
    def murio(self):
        self.vida=0
        print(self.nombre, "ha muerto")

#mi_personaje = Personaje("Alex", 10, 1, 5, 100) #constructor
#print(mi_personaje)
#para modificar los atributos:
#mi_personaje.nombre= "Mazinger Z"
#mi_personaje.defensa=100

#para consultar los atributos a traves de ".":
#print("El nombre del jugador es", mi_personaje.nombre)
#print("La defensa del jugador es: ", mi_personaje.defensa)
#mi_personaje.atributos() #mostrar atributos
#mi_personaje.subir_nivel(10, 5, 100)
mi_personaje = Personaje("Mazinger Z", 10, 1, 5, -10)
mi_personaje.murio()
mi_personaje.atributos()
print(mi_personaje.esta_vivo())



