import datetime

# Función para determinar el saludo según la hora
def obtener_saludo():
    hora_actual = datetime.datetime.now().hour
    if hora_actual < 12:
        return "¡Buenos días"
    elif hora_actual < 18:
        return "¡Buenas tardes"
    else:
        return "¡Buenas noches"

# Solicitar el nombre del usuario
nombre = input("¿Cuál es tu nombre? ")
saludo = obtener_saludo()

print(f"{saludo}, {nombre}! Bienvenido a Python.")