import random

# Genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Bienvenido al juego de adivinanza!")
print("He elegido un número entre 1 y 100. ¿Puedes adivinar cuál es?")

while True:
    intento = int(input("Ingresa tu número: "))
    intentos += 1

    if intento < numero_secreto:
        print("El número es mayor. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("El número es menor. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break