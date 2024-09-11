#Convertir USD a CNY
def usd_to_cny(usd):
    # Tasa de conversión
    conversion_rate = 6.75
    # Calcular el monto en Yuanes
    cny = usd * conversion_rate
    # Devolver el resultado como una cadena formateada
    return f"{cny:.2f} Chinese Yuan"

# Ejemplo de uso
usd_amount = int(input("Introduce el monto en USD: "))
result = usd_to_cny(usd_amount)
print(result)