import math

def litres(time):
    # Calcular los litros de agua bebidos y redondear hacia abajo
    return math.floor(time * 0.5)#math.floor(): Redondeamos hacia abajo

# Ejemplo de uso
time = float(input("Introduce el tiempo en horas: "))
result = litres(time)
print(f"Nathan beberá {result} litros de agua.")