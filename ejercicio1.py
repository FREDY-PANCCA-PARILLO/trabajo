# Leer un entero positivo del usuario
n = int(input("Introduce un entero positivo: "))

# Verificar que el número es positivo
if n <= 0:
    print("Por favor, introduce un entero positivo mayor que 0.")
else:
    # Calcular la suma de los enteros desde 1 hasta n
    suma = sum(range(1, n + 1))
    
    # Mostrar el resultado
    print(f"La suma de todos los enteros desde 1 hasta {n} es: {suma}")