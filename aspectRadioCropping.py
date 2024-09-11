#Aspect Radio Cropping
import math

def convert_to_16_9(x, y):
    # Calcular el nuevo ancho basado en la relación 16:9
    new_x = math.ceil(y * (16 / 9)) #math.ceil(): Usamos ceil para redondear el nuevo ancho al entero más cercano hacia arriba.
    return new_x, y

# Ejemplo de uso
x = int(input("Introduce el ancho original (X): "))
y = int(input("Introduce la altura original (Y): "))

# Convertir la resolución a una de aspecto 16:9
new_resolution = convert_to_16_9(x, y)

print(f"La nueva resolución con aspecto 16:9 es: {new_resolution[0]}x{new_resolution[1]}")
