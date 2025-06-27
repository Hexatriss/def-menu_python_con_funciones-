#Registrar e iniciar contraseña 🔐
# Esta es una versión distinta a la que quería el profesor pero proposito del ejercicio si esta (Esta en la linea 30 hasta la linea 61)
cond1 = False
cond2 = False
cond3 = False 
cond4 = False 
cond5 = False 
cond6 = False 
cont_simbolos = 0
contraseña = None
while True:
    print ("           [¡Welcome!]         ")
    print ("-------------------------------")
    print ("    1) Ingresar contraseña")
    print ("    2) Registrar contraseña")
    print ("    3) Salir")
    print ("--------------------------------")
    R = int(input("Ingrese a una de las opciones ingresando un numero: "))

    if R == 1:
        if contraseña == None:
            print ("Usted aun no se a registrado en la pagina...(Volviendo al menu).")
        else:
            C = input("Ingrese la contraseña: ")
            if C == contraseña:
                print ("¡Bienvenido!...¡Has ingresado a la pagina existosamente!")
                break
            else:
                print ("Contraseña incorrecta.")
    elif  R == 2:
        contraseña = input ("Ingrese la contraseña que desee: ")

        if len(contraseña) >= 8 and len(contraseña) <=16:
            cond1 = True

        for i in contraseña:
            if i in "0123456789":
                cond2 = True

        if i in "qwertyuiopasdfghjklñzxcvbnm":
            cond3 = True

        if i in "-_*.!?#$%:":
            cont_simbolos += 1
        if cont_simbolos <= 1:
            cond4 = True
        
        if i not in " ":
            cond5 = True

        if contraseña[-1] not in "-_*.!?#$%:":
            cond6 = True
        
        if cond1 and cond2 and cond3 and cond4 and cond5 and cond6:
            print ("Contraseña valida")
        else:
            contraseña = None
            print ("Contraseña invalida (Se devolvera al inicio)...")
    elif R == 3:
        print ("---SALIENDO DE LA PAGINA---")
        break
    else:
        print ("---Por favor...Ingrese uno de los numeros que esta dentro de la opción (1 - 2 - 3)---")
