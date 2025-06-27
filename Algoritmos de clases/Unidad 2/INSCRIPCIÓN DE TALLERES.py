total_puntos = 0
taller1 = 10
taller2 = 10
taller3 = 10
while True:
    try:
        print ()
        print ("---INSCRIPCIÓN DE TALLERES---")
        print (" 1) Taller de programación")
        print (" 2) Taller de base de datos")
        print (" 3) Taller de costura")
        print (" 4) Ver todos los cupos disponibles")
        print (" 5) SALIR")
        print ()
        menu1 = int(input("Ingrese un numero que este relacionado con el menu de presentación: "))
        print ()
        if menu1 == 1:
            print ("¿Esta seguro de ingresar al taller de programación?: ")
            print ("    1) SI")
            print ("    2) NO")

            desición1 = int(input("Ingrese un numero que este relacionado con el menu: "))
            if desición1 == 1:
                if taller1 < 1:
                    print ("---¡No le queda mas puntos!---")
                else:
                    taller1 -= 1
                    print ("¡Usted a ingresado al taller con exito!: ")

            elif desición1 == 2:
                print ("Cancelando solicitud...")
            
        if menu1 == 2:
            print ("¿Esta seguro de ingresar al taller de base de datos?: ")
            print ("    1) SI")
            print ("    2) NO")

            desición2 = int(input("Ingrese un numero que este relacionado con el menu: "))
            if desición2 == 1:
                    if taller2 < 1:
                        print ("---¡No le queda mas puntos!---")
                    else:
                        taller2 -= 1
                        print ("¡Usted a ingresado al taller con exito!: ")
            elif desición2 == 2:
                    print ("Cancelando solicitud...")

        if menu1 == 3:
            print ("¿Esta seguro de ingresar al taller de costura?: ")
            print ("    1) SI")
            print ("    2) NO")
            desición3 = int(input("Ingrese un numero que este relacionado con el menu: "))
            if desición3 == 1:
                if taller3 < 1:
                    print ("---¡No le queda mas puntos!---")
                else:
                    taller3 -= 1
                    print ("¡Usted a ingresado al taller con exito!: ")
            elif desición3 == 2:
                    print ("Cancelando solicitud...")

        if menu1 == 4:
            while True:
                total_puntos = taller1 + taller2 + taller3
                print ("       ---CUPOS DISPONIBLES---")
                print (f"    1) Taller de programación:  {taller1}")
                print (f"    2) Taller de base de datos: {taller2}")
                print (f"    3) Taller de Costura:       {taller3}")
                print ("    ------------------------------")
                print(f"    TOTAL DE PUNTOS = {total_puntos}")
                total_puntos = 0
                print ()
                X = int(input("Ingresa el numero 1 si es que quieres salir: "))
                if X == 1:
                    print ("---Saliendo de la categoría de cupos---")
                    break
                else:
                    print ("---Porfavor, presione 1 si es que quiere salir de este menú---")

            
        if menu1 == 5:
            print ("---Saliendo del programa---")
            break
    except:
         taller1 = 10
         taller2 = 10
         taller3 = 10
         print ()
         print ("---A SURGIDO UN ERROR SE REINICIARA EL PROGRAMA---")


         
        

