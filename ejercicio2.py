# Leer la edad del usuario
edad = int(input("Introduce tu edad: "))

# Leer los ingresos mensuales del usuario
ingresos = float(input("Introduce tus ingresos mensuales en soles (S/): "))

# Determinar si el usuario debe tributar
if edad > 18 and ingresos >= 3000:
    print("Debes tributar.")
else:
    print("No necesitas tributar.")
