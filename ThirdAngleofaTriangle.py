#Problema An NBA game runs 48 minutes (Four 12 minute quarters). Players do not typically play the full game, subbing in and out as necessary. Your job is to extrapolate a player's points per game if they played the full 48 minutes.

#Write a function that takes two arguments, ppg (points per game) and mpg (minutes per game) and returns a straight extrapolation of ppg per 48 minutes rounded to the nearest tenth. Return 0 if 0.
#Este programa encuentra el angulo de un triangulo apartor de los otros
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