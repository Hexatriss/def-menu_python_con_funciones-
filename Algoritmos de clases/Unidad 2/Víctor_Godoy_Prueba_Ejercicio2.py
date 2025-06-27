#Ejercicio 2
BOLETOS = 50
while True:
    try:
        print ("***** Cine Estrella *****")
        print ("Bienvenido al sistema de venta de entradas del Cine Estrella")
        print ("1. Ver cuántas entradas quedan.")
        print ("2. Comprar una cantidad de entradas.")
        print ("3. Devolver entradas.")
        print ("4. Salir del sistema.")
        menu1 = int(input("Ingrese el numero de las opciones que usted quiere entrar: "))
        if menu1 == 1:
            print ()
            print (f"---QUEDAN {BOLETOS} ENTRADAS DISPONIBLES---")
            print ()
        elif menu1 == 2:
                try:
                    CANTIDAD = int(input("¿Cuantas cantidad de boletas quiere comprar?: "))
                    if BOLETOS > 0:
                        BOLETOS = BOLETOS - CANTIDAD
                        print()
                        print (f"---Se han comprado {CANTIDAD}. Total disponible: {BOLETOS}---")
                        print()
                    
                    else:
                        print ()
                        print ("---No hay suficientes boletas---")
                        print ()
                     

                except:
                    print ("---Debe ingresar un número entero válido---")

        elif menu1 == 3:
                try:
                    DEVOLVER  = int(input("¿Cuantas cantidad de bolestas quiere devolver?: "))
                    BOLETOS = BOLETOS + DEVOLVER
                    print ()
                    print (f"---Se han devuelto {DEVOLVER}. Total disponible: {BOLETOS}---")
                    print ()
                 
                except:
                    print ("---Debe ingresar un número entero válido---")


        elif menu1 == 4:
            print ("Gracias por usar el sistema de ventas del Cine Estrella. ¡Hasta pronto!")
            break


        else:
            print()
            print("---Ingrese uno de los numeros que están en el menú porfavor---")
            print()
             
    except:
        print()
        print ("---Opción no válida. Por favor, seleccione una opción del 1 al 4---")
        print()

                    