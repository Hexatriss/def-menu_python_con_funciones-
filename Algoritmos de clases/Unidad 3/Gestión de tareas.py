"""
Enunciado:
Gestión de una Lista de Tareas:
Estás desarrollando un programa para gestionar las tareas de una persona. El programa debe permitir agregar nuevas tareas, mostrar las
tareas
actuales y salir de la aplicación. Cada tarea tiene un nombre y un estado (completada o pendiente).
El programa debe tener las siguientes opciones:
Agregar tarea: Permite al usuario agregar una nueva tarea. Se pide el nombre de la tarea y su estado (completada o pendiente).
Mostrar tareas: Muestra todas las tareas con su nombre y estado.
Salir: Termina el programa.
Requisitos adicionales:
Si se elige la opción de mostrar tareas y no hay ninguna tarea guardada, el programa debe indicar que no hay tareas.
El programa debe seguir ejecutándose hasta que el usuario decida salir

"""
Tareas = {}
contador = 1
while True:
    print ("---GESTIÓN DE TAREAS---")
    print ("1. Añadir Tareas    ")
    print ("2. Ver Tareas       ")
    print ("3. Salir            ")
    menu = int(input("Escoja una opción (1-3): "))

    if menu == 1:
        print()
        Añadir_tarea = input("Ingrese una tarea en la lista: ")
        Añadir_Estado = input("¿Su tarea en que estado esta? (completado/pendiente): ").upper()
        if Añadir_Estado == "COMPLETADO" or Añadir_Estado == "PENDIENTE":
            Tareas[Añadir_tarea] = Añadir_Estado
            print ()
            print ("Se a ingresado la tarea correctamente.")
            print ()

            
            print (Tareas)


        else:
            print ()
            print ("Opción no valida. Vuelva a intentarlo")
            print ()
       
    elif menu == 2:
        print()
        print ("---LISTA DE TAREAS---")
        for Añadir_Tarea, Añadir_Estado in Tareas.items():
            print (f"{contador}. {Añadir_Tarea} = {Añadir_Estado}")
            contador += 1

        contador = 1
        print()

    elif menu == 3:
        print ("Saliendo del programa.")
        break

