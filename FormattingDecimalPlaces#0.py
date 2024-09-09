def format_number(num):
    # Formatear el número con dos decimales
    return f"{num:.2f}"

# Ejemplo de uso
number = float(input("Introduce un número: "))
formatted_number = format_number(number)

print(f"El número formateado es: {formatted_number}")