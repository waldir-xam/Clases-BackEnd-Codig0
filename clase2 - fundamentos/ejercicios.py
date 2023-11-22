""" def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()

    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False


print(es_palindromo("Ana"))  # True
print(es_palindromo("Hola"))  # False
print(es_palindromo("Jose"))  # False
"""

palabra = "aeropuerto"
""" print("-".join(["1","2","3"])) """

""" letras_invertidas = []

for letra in palabra:
    letras_invertidas.insert(0, letra)

    print("".join(letras_invertidas))
"""

# ejercicio 2
# solicitar el yearo en el que nacimos, este mismo se va a iterar restandolo el year atual, de tal manera que nos mostrara los mensajes como
# en 1995 tenias 1 year

# 1 el year ingresado no debe ser mayor al year actual,
# 2 cuando se llegue al year actual, el m,ensaje debe decir: " actualnmmente en el year 2022, tienes 28 years"
#indicar el anio a introducir
nacimiento = int(input("Ingresa el year en el que naciste: "))
# Obtener el year actual
from datetime import datetime

# Obtener el año actual
ahora = datetime.now()
year_actual = ahora.year

# Verificar que el year de nacimiento no sea mayor al year actual
if nacimiento > year_actual:
    print(
        "El year ingresado es mayor al year actual. Por favor ingresa un year válido."
    )
else:
    # Iterar desde el year de nacimiento hasta el year actual
    for year in range(nacimiento, year_actual+1):
        # Calcular la edad en el year actual
        edad = year - nacimiento
        if year == year_actual:
            # Mostrar el mensaje para el year actual
            print(f"Actualmente en el year {year_actual}, tienes {edad} anios.")
        else:
            # Mostrar el mensaje para otros years
            print(f"En {year}, tenías {edad} anios.")