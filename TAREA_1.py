class Componente: 
    def __init__(self, tipo, numero_serie, costo):
        self.tipo = tipo
        self.numero_serie = numero_serie 
        self.costo = costo
        self.historial_revisiones = [] 
        self.esta_activo = True 

C1 = Componente("MOTOR", "MTR-1001", 550.70)
C2 = Componente("SENSOR", "SNR-2050", 80.20)

C1.historial_revisiones.append("2025-10-27")
C2.historial_revisiones.append("2025-09-15")

C2.esta_activo =False
print("--- REPORTE DE COMPONENTES ---")

print(f"Tipo: {C1.tipo}, S/N: {C1.numero_serie}, Costo: {C1.costo}, Revisiones: {C1.historial_revisiones}, Activo: {C1.esta_activo}")
print(f"Tipo: {C2.tipo}, S/N: {C2.numero_serie}, Costo: {C2.costo}, Revisiones: {C2.historial_revisiones}, Activo: {C2.esta_activo}")

