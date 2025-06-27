import random
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
suma = dado1 + dado2
intento1 = int(input("Primer intento: ¿Cual es la suma de los dados?: "))

if intento1 == suma:
    print ("Usted acerto!")
else:
    moneda = suma % 2
    if moneda == 0:
        intento2 = int(input("No adivinaste...Segundo intento: ¿Cual es la suma de los dados? (Pista: El numero es par): "))
    else:
        intento2 = int(input("No adivinaste...Segundo intento: ¿Cual es la suma de los dados? (Pista: el numero es impar): " )) 

    if intento2 == suma:
      print ("Usted acerto!")
    else:
      print(f"No pudo adivinar la suma. La respuesta era: {suma}")


#El error que hubo fue el mal posicionamiento del if de la decimasexta linea del algoritmo, debe de estar conectado
#con la onceava linea del algoritmo 
