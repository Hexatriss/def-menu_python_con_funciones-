Taller1 = 12
Taller2 = 8
Taller3 = 10
total_de_puntos = 0
while True:
    try:
        print ("---TALLERES DE EL INSITUTO---")
        print (" 1) Taller de pintura     ")
        print (" 2) Taller de fotografía ")
        print (" 3) Taller de Robotica   ")
        print (" 4) Ver los cupos disponibles")
        print (" 5) SALIR")
        menu1 = int(input("Ingrese el numero de la opción que usted desee: "))
        if menu1 == 1:
            print ("¿Esta seguro que quiere ingresar al taller de pintura?")
            print (" 1) SI")
            print (" 2) NO")
            DESICIÓN1 = int(input("Ingrese el numero de la opción que usted desee:"))
            if DESICIÓN1 == 1:
                if Taller1 < 1:
                    print()
                    print ("---¡Se a quedado sin puntos, ya no puede matricularse al taller!---")
                    print()
                else:
                    Taller1 -= 1
                    print()
                    print ("---¡Usted a ingresado con exito al Taller de pintura!---")
                    print()

            if DESICIÓN1 == 2:
                print ("---Saliendo de la primera sección---")

        if menu1 == 2:
            print ("¿Esta seguro que quiere ingresar al taller de fotografía?")
            print (" 1) SI")
            print (" 2) NO")
            DESICIÓN2 = int(input("Ingrese el numero de la opción que usted desee: "))
            if DESICIÓN2 == 1:
                if Taller2 < 1:
                    print()
                    print ("---¡Se a quedado sin puntos, ya no puede matricularse al taller!---")
                    print()
                else:
                    Taller2 -= 1
                    print()
                    print ("---¡Usted a ingresado con exito al Taller de fotografía!---")
                    print()

            if DESICIÓN2 == 2:
                print ("---Saliendo de la segunda sección---")
        
        if menu1 == 3:
            print ("¿Esta seguro que quiere ingresar al taller de robotica?")
            print (" 1) SI")
            print (" 2) NO")
            DESICIÓN3 = int(input("Ingrese el numero de la opción que usted desee: "))
            if DESICIÓN3 == 1:
                if Taller3 < 1:
                    print()
                    print ("---¡No puede matricularse al taller, ya que se a quedado sin puntos!---")
                    print()
                else:
                    Taller3 -= 1
                    print()
                    print ("---¡Usted a ingresado con exito al Taller de Robotica!---")
                    print()


            if DESICIÓN3 == 2:
                print()
                print ("---Saliendo de la tercera sección---")
                print()
        
        if menu1 == 4:
            total_de_puntos = Taller1 + Taller2 + Taller3
            print()
            print("---CUPONES DISPONIBLES DE CADA TALLER---")
            print (f"      1) Taller de pintura = {Taller1}")
            print (f"      2) Taller de diseño = {Taller2} ")
            print (f"      3) Taller de Robotica = {Taller3}")
            print ("--------------------------------------")
            print (f"      TOTAL DE PUNTOS = {total_de_puntos}")
            print()
            total_de_puntos = 0



        if menu1 == 5:
            print ("---Saliendo del programa---")
            break
    except:
        Taller1 = 12
        Taller2 = 8
        Taller3 = 10
        total_de_puntos = 0
        print ()
        print ("---OCURRIO UN ERROR SE RESETEARA EL PROGRAMA---")
        print()

        





