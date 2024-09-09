def find_third_angle(angle1, angle2):
    # Calcular el tercer ángulo
    third_angle = 180 - (angle1 + angle2)
    return third_angle

# Ejemplo de uso
angle1 = int(input("Introduce el primer ángulo: "))
angle2 = int(input("Introduce el segundo ángulo: "))

# Encontrar el tercer ángulo
result = find_third_angle(angle1, angle2)

print(f"El tercer ángulo es: {result} grados")