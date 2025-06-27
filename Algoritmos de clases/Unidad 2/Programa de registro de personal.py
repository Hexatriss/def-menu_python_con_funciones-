usuario1, usuario2, usuario3 = None,None,None 
contraseña1, contraseña2, contraseña3 = None,None,None   
while True:
    print ("\n---COMPUTADORA DE REGISTRO---")
    print ("1)Iniciar sesión")
    print ("2)Registrar usuario")
    print ("3)Salir")
    
    i = int(input("---Seleccione una opción---:"))

    if i == 1:
        if usuario1 != None and usuario2 != None and usuario3 != None:
            l = input("Ingrese un usuario: ")
            h = input("Ingrese la contraseña del usuario: ")
            if  (l == usuario1 and h == contraseña1) or \
                (l == usuario2 and h == contraseña2) or \
                (l == usuario3 and h == contraseña3):
                print (f"---¡Bienvenido {l}!---")

                while True:
                    print ("\n---REGISTRO---")
                    print ("1)Realiza llamada")
                    print ("2) Enviar correo electrónico")
                    print ("3)Cerrar sesión")

                    try:
                        opcion_usuario = int(input("---Seleccione una opción---:"))
                        if opcion_usuario == 1:
                            while True:
                                numero = input("Ingrese un número celular (Debe comenzar con 9 y ser de 8 digitos): ")
                                if len(numero) == 8 and numero[0] == "9" and numero.istdigit():
                                    print (f"Llamada realizada al número {numero}.")
                                    break
                                else:
                                    print ("Numero invalido. Debe comenzar con 9 y ser de 8 digitos")

                        elif opcion_usuario == 2:
                            while True:
                                correo = input("Ingrese el correo electronico: ")
                                if "@" in correo:
                                        break
                                else:
                                    print ("Correo invalido. Debe contener al menos un @")
                                mensaje = input("Ingrese un mensaje a enviar: ")
                                print (f"Correo enviado a {correo} con el mensaje: {mensaje}")

                        elif opcion_usuario == 3:
                            print ("Cerrando sesión...")
                            break
                        else:
                            print("Opción no valido intente nuevamente.")
                    except ValueError:
                        print ("Por favor ingrese un número válido")
                
            else:
                print ("Acceso Denegado...Volviendo al menu principal.")
        else:
            print ("---No se a registrado ningún usuario aun...Volviendo al menu principal---")      
    if i == 2:
        print ("1)Usuario")
        print ("2)Usuario")
        print ("3)Usuario")
        y = int(input("Seleccione cual usuario desea registrar en a computadora (del 1 al 3): "))
        if y == 1:
            usuario1 =  input("Ingrese que nombre le quiere dar al primer usuario: ")
            contraseña1 = input("Ingrese una contraseña al primer usuario: ")
        elif y == 2:
            usuario2 = input("Ingrese el nombre que le quiere dar al segundo usuario: ")
            contraseña2 = input("Ingrese la contraseña que le quiere dar al segundo usuario: ")
        elif y == 3:
            usuario3 = input("Ingrese el nombre que le quiere dar al tercer usuario: ")
            contraseña3 = input("Ingrese la contraseña que le quiere dar al tercer usuario: ")
    if i ==3:
        print ("---Cerrando programa---")
        break


    