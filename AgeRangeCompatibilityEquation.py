import math


def dating_range(age):
    if age > 14:
        # Aplicar la regla de "la mitad de tu edad más siete" para mayores de 14 años
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)
    else:
        # Aplicar la regla del 10% para menores o iguales a 14 años
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)

    return f"{min_age}-{max_age}"


# Ejemplo de uso
age = int(input("Introduce la edad: "))
result = dating_range(age)

print(f"El rango de edad recomendado es: {result}")