def mangoes_cost(quantity, price_per_mango):
    # Calcular cuántos mangos se pagan
    payable_mangoes = (quantity // 3) * 2 + (quantity % 3)
    # Calcular el costo total
    total_cost = payable_mangoes * price_per_mango
    return total_cost

# Ejemplo de uso
quantity = int(input("Introduce la cantidad de mangos: "))
price_per_mango = float(input("Introduce el precio por mango: "))

# Calcular el costo total
total_cost = mangoes_cost(quantity, price_per_mango)

print(f"El costo total es: {total_cost}")