respuesta = 0
intentos = 0

while respuesta != 10 and intentos < 5:
    respuesta = int(input(f"Adivina el numero (Intentos = {intentos}/5): "))
    if respuesta != 10:
        intentos += 1
        print ("Sigue intentandolo, aun tienes mas intentos.")
    else:
        print ("---ADIVINASTE---")

print ("---FIN DEL JUEGO---")
