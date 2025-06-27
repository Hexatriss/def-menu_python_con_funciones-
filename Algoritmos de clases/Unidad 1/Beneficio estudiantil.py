#Beneficios estudiantiles en Educación superior 📚
edad = int(input("Ingrese su edad: "))
nota = int(input("Ingrese su calificación del 1 al 100: "))
lugar = int(input("Ingrese el numero 1 si vive fuera de la ciudad, ingrese el numero 0 si vive dentro de una ciudad: "))
trabajo = int(input("Ingrese el numero 1 si esta trabajando, ingrese el numero 0 si no trabaja: "))

if edad < 25 and nota >= 80 and lugar == 1 and trabajo == 0:
    print ("¡FELICIDADES! Tiene acceso al beneficio total")
elif edad < 25 and nota >= 80 and lugar == 1 and trabajo == 1:
    print ("¡FELICIDADES! ¡Tiene acceso al beneficio parcial A!") 
elif nota >= 60 and lugar == 1:
    print ("¡FELICIDADES! ¡Tiene acceso al beneficio parcial B!")
else:
    print ("¡Una lastima! ¡no obtuvo ningún beneficio!") 