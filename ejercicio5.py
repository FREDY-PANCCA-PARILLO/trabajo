# Leer el nombre del usuario
nombre = input("Introduce tu nombre: ").strip()

# Leer el sexo del usuario
sexo = input("Introduce tu sexo (M para mujer, H para hombre): ").strip().upper()

# Verificar que el sexo es válido
if sexo not in ['M', 'H']:
    print("Sexo no válido. Por favor, introduce 'M' para mujer o 'H' para hombre.")
else:
    # Convertir el primer carácter del nombre a mayúscula para la comparación
    primera_letra = nombre[0].upper()

    # Determinar el grupo según las reglas
    if sexo == 'M':
        if primera_letra < 'F':
            grupo = 'A'
        else:
            grupo = 'B'
    elif sexo == 'H':
        if primera_letra > 'O':
            grupo = 'A'
        else:
            grupo = 'B'

    # Mostrar el grupo al usuario
    print(f"Te corresponde el grupo {grupo}.")
