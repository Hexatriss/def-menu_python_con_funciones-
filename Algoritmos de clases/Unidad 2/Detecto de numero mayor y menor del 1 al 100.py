"""
La opción 1 debe permitir ingresar un número entero entre 0 y 100. El usuario puede ingresar cualquier valor,
por lo que debe hacer uso de manejo de excepciones, ya que incluso podría ingresar un string en vez de un
número. Si el usuario no ingresa un número entero, el programa debe entregar el mensaje: "Debe ingresar un
número entero!!", y repetir la solicitud de ingreso de número. Si se ingresa un número entero, pero no está
dentro del rango [0,100] entonces debe mostrar el mensaje: "Debe ingresar un número entre 0 y 100!!" y
repetir la solicitud de ingreso de número. Si se ingresa un número que cumpla las condiciones,
entonces debe mostrarse el mensaje: "Ingreso exitoso".
La opción 2 debe mostrar el número mayor ingresado hasta ese momento.
La opción 3 debe mostrar el número menor ingresado hasta ese momento.
Para ambas opciones, si no se han ingresado números, y se pido el número mayor o menor,
entonces el programa debe mostrar el mensaje: "No se han ingresado números."
La opción 4 permite terminar el programa, mostrando por pantalla el mensaje: "Fin del
programa. Adiós."
En el menú principal, si se ingresa cualquier otro valor que no sea el de las opciones
mostradas, el programa debe mostrar el mensaje: "Debe ingresar una opción válida.”, y
volver a preguntar por una opción.
A continuación, se muestra un ejemplo de ejecución

"""
opcion2 = None
mayor = -1
menor = 101
while True:
    print ("***MENÚ PRINCIPAL***")
    print ("1)  Ingresar un número")
    print ("2)  Mostar mayor")
    print ("3)  Mostrar menor")
    print ("4)  Terminar programa")
    print ()
    opcion1 = int(input("Ingrese un numero que este relacionado con el menú: "))
    if opcion1 == 1:
        while True:
            try:
                opcion2 = int(input("Ingrese un numero que sea del 1 al 100: "))
                if opcion2 >= 0 and opcion2 >= 100:
                    print ("Debe ingresar un número entre 0 y 100!!")
                    opcion2 = None
                else:
                    print ("¡Ingreso del numero exitoso!")
                    if opcion2 > mayor:
                        mayor = opcion2
                    elif opcion2 < menor:
                        menor = opcion2
                    break
            except ValueError:
                print ("Debe ingresar un número entero!!")


    elif opcion1 == 2:
        if opcion2 == None:
            print ("No se a ingresado ningún numero aun...Volviendo al menú")
        else:
            print (f"El numero mayor que se ingreso es {mayor}")



    elif opcion1 == 3:
        if opcion2 == None:
            print ("No se a ingresado ningún numero aun...Volviendo al menú")
        else:
            print (f"El numero menor que se ingreso es {menor}")



    elif opcion1 == 4:
        print("---Cerrando programa---")
        break

    else:
        print ("Debe ingresar una opción válida.")


"""

Se debe aprender usar el try/except 
manejar bien el patron de desiciones en la linea 41 - 44
y manejar mejor el uso de variables


"""