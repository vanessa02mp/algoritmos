def points_per_48(ppg, mpg):
    # Si el jugador no tiene minutos, devolvemos 0
    if mpg == 0:
        return 0
    # Calcular los puntos extrapolados por 48 minutos
    extrapolated_ppg = (ppg / mpg) * 48
    # Redondear a la décima más cercana
    return round(extrapolated_ppg, 1)

# Ejemplo de uso
ppg = float(input("Introduce los puntos por juego (ppg): "))
mpg = float(input("Introduce los minutos por juego (mpg): "))

# Calcular los puntos extrapolados
result = points_per_48(ppg, mpg)

print(f"El jugador marcaría {result} puntos si jugara los 48 minutos.")