#Ejericio 1
NOMBRE = None
MAYOR15 = 0
MENOR15 = 0
while True:
    try:

        op1 = int(input("Ingrese la cantidad de libros prestados: "))
        break
        
    except:
        print("---El numero debe ser un numero entero---")

while True:
    
        if op1 <= 0:
            print (f"Se registraron {MAYOR15} libros con préstamo mayor a 15 días")
            print (f"Se registraron {MENOR15} libros con préstamo de 15 días o menos")
            break

        else:
            NOMBRE = input("Ingrese el nombre del titulo: ")
        while True:
            try:
                op2 = int(input(f"Ingrese los días de prestamo para '{NOMBRE}': "))

                if op2 > 15:
                    op1 -= 1
                    MAYOR15 += 1
                    print ("Préstamo por más de 15 días")
                    break
                        
                if op2 <= 15:
                    op1 -= 1
                    MENOR15 += 1
                    print ("Préstamo por 15 días o menos")
                    break
            except:
                print ("---Debe ingresar un numero entero---")






