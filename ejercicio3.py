# Leer la fecha de nacimiento en formato dd/mm/aaaa
fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

# Separar la fecha en día, mes y año usando el método split()
dia, mes, anio = fecha.split('/')

# Mostrar el día, mes y año por separado
print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")
