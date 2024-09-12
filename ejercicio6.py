# Programa para calcular el precio de entrada en una sala de juegos

def calcular_precio_entrada(edad):
    if edad < 4:
        return 0
    elif 4 <= edad <= 18:
        return 5
    else:
        return 10

def main():
    try:
        edad = int(input("Por favor, ingresa la edad del cliente: "))
        if edad < 0:
            print("La edad no puede ser negativa. Por favor ingresa una edad válida.")
        else:
            precio = calcular_precio_entrada(edad)
            print(f"El precio de la entrada es: ${precio}")
    except ValueError:
        print("Por favor, ingresa un número entero válido para la edad.")

if __name__ == "__main__":
    main()
