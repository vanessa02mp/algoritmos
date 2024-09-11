#calcula la edad del perro y el gato en años humanos
#programa que calcula la edad
#
def calculate_pet_ages(humanYears):
    #al primer año
    if humanYears == 1:
        catYears = 15
        dogYears = 15
        #al segundo año
    elif humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
        #mas de 3 años
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5
    #devuelve una lista con los años humanos gato y perro
    return [humanYears, catYears, dogYears]


# Ejemplo de uso:
#pregunat por consola
humanYears = int(input("Introduce los años humanos: "))

#llama a la funcion para los calculos
#result = calculate_pet_ages(12)
result = calculate_pet_ages(humanYears)
#print(result)

print(f"Edad en años humanos: {result[0]}") #la f son una forma de concatenar
print("Edad en años de gato: "+str(result[1]))# esta es otra forma en lugar de poner la F practicamente concatena 
print(f"Edad en años de perro: {result[2]}")

#imprime el tipo de datos delvueltos por la funcion
print(type(result))