#Acceso a un Torneo de videojuegos 🎮
edad = int(input("Ingrese su edad: "))
años = int(input("Ingrese sus años de experiencia jugando videojuegos: "))
promedio = int(input("Digame cual es su promedio de rendimiento del 1 al 100: "))
anterior = int(input("Presione el numero 1 si ha participado en algún otro torneo si no, presione el numero 0: "))
recomienda = int(input("Presione el numero 1 si cuenta con recomendación oficial de un club si no, presione el numero 0: "))

if edad >= 16 and edad <= 25 and años >= 3 and promedio > 85:
    print ("El jugador obtuvo la 'Clasificación directa'")
elif edad >= 16 and edad <= 25 and anterior == 1 or edad > 25 and recomienda == 1:
    print ("El jugador obtuvo 'Clasificación bajo revisión'")
else: 
    print ("El jugador no a clasificado...") 