"""
Desarrolla una aplicación en python para ayudar a los usuarios a gestionar sus tareas diarias. El objetivo es permitir que el usuario 
pueda
agregar, consultar y eliminar tareas, todo desde un menú sencillo.
El debe ser interactivo, funcionar en un bucle continuo y utilizar estructuras de control para manejar el menú. También se deben usar 
listas
para almacenar las tareas y aplicar condiciones para asegurar que el programa funcione de forma segura y lógica.
Crear un gestor de tareas que:

Permita al usuario agregar tareas a una lista.
Permita ver todas las tareas que ha agregado.
Permita eliminar una tarea específica usando su número en la lista.
Funcione en bucle hasta que el usuario elija salir
"""

Tareas = []
numero = 0
Flag = False

while True:
    print ("---¡MENU DE TAREAS!---")
    print ("1. Agregar tareas     ")
    print ("2. Ver tareas         ")
    print ("3. Eliminar tareas    ")
    print ("4. Salir              ")
    menu = int(input("Seleccione una de las opciones que muestra el menu ingresando un numero: "))

    if menu == 1:
        print() 
        AGREGAR = input("Ingrese la tarea que desea agregar a la nota: ")
        Tareas.append(AGREGAR)
        print ("¡Se agrego la tarea con exito!")
        print() 
        Flag = True

    elif menu == 2:
        if Flag == True:
            print() 
            print ("---LISTA DE TAREAS---")
            for elemento in Tareas:
                print (f"{numero} : {elemento}")
                numero += 1
            numero = 0
            print() 
        else:
            print (Tareas)
            print ("No se a añadido ninguna lista hasta ahora.")

    elif menu == 3:
        if Flag == True:
            print() 
            print ("---ELIMINA UNA DE LAS TAREAS INGRESANDO EL NUMERO DE LA TAREA---")
            for elemento in Tareas:
                print (f"{numero} : {elemento}")
                numero += 1
            print() 

            numero = 0
            eliminar = int(input(":"))
            Tareas.pop(eliminar)
            print() 
            print ("¡Se a eliminado una nota de la lista con exito!")
            print() 
            if Tareas == []:
                Flag = False
        else:
            print (Tareas)
            print ("No se a añadido ninguna lista hasta ahora.")

    elif menu == 4:
        print() 
        print ("Cerrando el programa...")
        break
