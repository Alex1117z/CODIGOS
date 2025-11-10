class Vehiculo:
    #este es el contructor del padre __init__
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0
        self._encendido = False
    def arrancar(self):
        if not self._encendido:
            self._encendido = True
            print (f"El {self.marca} {self.modelo} ha arrancado")
        else:
            print("El vehículo ya estaba en marcha")
    def apagar(self):
        if self._encendido:
            self._encendido = False
            print (f"El {self.marca} {self.modelo} se ha apagado")
        else:
            print("El vehículo ya estaba apagado")
    def get_kilometraje(self):
        return self._kilometraje 
    def mostrar_info_base(self):
        print ("Marca. ", self.marca)
        print ("Modelo: ", self.modelo)
        print("Año del vehículo: ", self.año)
#Clase hija numero uno.
class Coche (Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año,) #python me sugirio esta forma profe :0
        self.numero_puertas = numero_puertas
    def conducir(self, km):
        if self._encendido:
            print ("El vehículo esta encendido")
            self.kilometraje += km
            print (f"Conduciendo, {self.kilometraje} km")
        else:
            print ("El coche no ha sido encendido, intente de nuevo")
    def get_kilometraje(self):
        return self.kilometraje
    
#CLASE HIJA numero dos
class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga_kg):
        super().__init__(marca, modelo, año,) 
        self.capacidad_carga_kg = capacidad_carga_kg
        self.__carga_actual_kg = 0
    def cargar(self, kilos):
            if self.__carga_actual_kg + kilos <= self.capacidad_carga_kg:
                self.__carga_actual_kg += kilos
                print ("carga exitosa")
            else:
                print("Error: Sobrecarga")
    def descargar (self, kilos):
            if kilos <= self.__carga_actual_kg:
                self.__carga_actual_kg -= kilos
                print(f"se descargaron {kilos}")
            else:
                print("Error, no hay suficiente carga")
    def get_carga_actual(self):
            return self.__carga_actual_kg
        
print("PRUEBA FINAL DE SI FUNCIONA")

mi_coche = Coche("Chevrolet", "Camaro ZL1", 2007, 4)
mi_camion = Camion("Honda", "Optimus", 2013, 5000)

# Probar coche
mi_coche.conducir(100)   # Debe fallar porque no está encendido
mi_coche.arrancar()
mi_coche.conducir(100)
mi_coche.apagar()
print("Kilometraje del coche:", mi_coche.get_kilometraje())

# Probar camión
mi_camion.cargar(3000)     
mi_camion.cargar(3000)       # Error: Sobrecarga
mi_camion.descargar(1000)
print("Carga actual del camión:", mi_camion.get_carga_actual())