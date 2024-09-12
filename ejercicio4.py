# Leer un número entero del usuario
n = int(input("Introduce un número entero positivo: "))

# Verificar que el número es positivo
if n <= 0:
    print("Por favor, introduce un número entero positivo mayor que 0.")
else:
    # Generar el triángulo rectángulo
    for i in range(1, n + 1):
        # La base de cada fila es un número impar que comienza en 1 y aumenta de dos en dos
        base = 2 * i - 1
        # Crear una lista de números decrecientes
        fila = [str(base - 2 * j) for j in range(i)]
        # Unir los números con un espacio y mostrar la fila
        print(' '.join(fila))
