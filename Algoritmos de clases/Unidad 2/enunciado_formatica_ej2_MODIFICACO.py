#Menu para calcular el promedio de tres edades 📊
usuario1 = None
usuario2 = None
usuario3 = None
edad1 = None
edad2 = None
edad3 = None
while True:
    try: 
        print ("           <[¡Welcome!]>         ")
        print ("----------------------------------")
        print ()
        print ("    1) Ingresar usuario y edad ")
        print ("    2) Calcular edad y promedio")
        print ("    3) Salir")
        print ()
        print ("-----------------------------------")
        R = int(input("Ingrese a una de las opciones ingresando un numero: "))
        if R == 1:
                print ("----------------------------------")
                print ()
                print ("    1) Usuario 1    ")
                print ("    2) Usuario 2    ")
                print ("    3) Usuario 3    ")
                print ()
                print ("-----------------------------------")
                T = int(input("Seleccione a que usuario que ingresar (1 - 3): "))
                if T == 1:
                    usuario1 = input("Ingrese el nombre que le quiere dar al usuario 1: ")
                    edad1 = int (input("Ingrese la edad que le quiere dar al usuario 1: "))
                    print ("¡Se registro el usuario 1 exitosamente!")
                elif T == 2:
                    usuario2 = input("Ingrese el nombre que le quiere dar al usuario 2: ")
                    edad2 = int (input("Ingrese la edad que le quiere dar al usuario 2: "))
                    print ("¡Se registro el usuario 2 exitosamente!")

                elif T == 3:
                    usuario3 = input("Ingrese el nombre que le quiere dar al usuario 3: ")
                    edad3 = int (input("Ingrese la edad que le quiere dar al usuario 3: "))
                    print ("¡Se registro el usuario 3 exitosamente!")

                        
                else:
                    print ("Lo lamento pero no se puede ingresar mas de tres usuario...")

        elif R == 2:
                if usuario1 != None and usuario2 != None and usuario3 != None: 
                    resultado = edad1 + edad2 + edad3 / 3
                    print (f"------------------------------------------------------")
                    print ()
                    print (f"---El promedio de las tres edades es de {resultado}---")
                    print ()
                    print (f"------------------------------------------------------")
                else:
                    print ("---Le falta ingresar los usuarios...(Volviendo al Menú.)---")
                
        elif R == 3:
                print ("---Saliendo del programa---")
                break
            
        else:
            print ("--¡Error!...debe de ingresar uno de los numeros que esta en el menú (1 - 2 - 3)---")
                
    except ValueError:
        print ("-------------------------------------------------------------------")
        print ()
        print ("No debe ingresar un numero decimal en la edad. Volviendo al menu...")
        print ()
        print ("-------------------------------------------------------------------")
            
           


