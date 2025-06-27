compradores = {}

def comprar_entrada():
    nombre = input("Ingresa el nombre del comprador: ")
    if nombre in compradores:
        print ("¡Error! El usuario ya esta ingresado.")
        return
    else:
        tipo_entrada = input("Ingrese tipo de entrada (G/V): ").upper()
        if tipo_entrada == "G":
            print("===¡Usted ingreso a la entrada tipo General!===")
            compradores[nombre] = "General"
        elif tipo_entrada == "V":
            print("===¡Usted ingreso a la entrada tipo VIP!===")
            compradores[nombre] = "VIP"

        else:
            print()
            print("Ingrese un codigo valido porfavor.")
            print()
            return
        
def consultar_comprador():
    verificador = input ("Ingrese el nombre del comprador: ")
    if verificador not in compradores:
        print ("El comprador no se encuentra en la lista.")
    else:
        if compradores[verificador] == "General":
            print (f"=== Nombre: {verificador} Tipo de entrada General===")
        else:
            print (f"=== Nombre: {verificador} Tipo de entrada VIP===")

def cancelar_compra():
    verificador = input("Ingrese el nombre del comprador para cancelar: ")
    if verificador not in compradores:
        print()
        print ("El comprador no se encuentra en la lista.")
        print()
        return
    else:
            compradores.pop(verificador) 
            print ("¡Compra Cancelada con exito!")




def menu():
    print("===MENU PRINCIPAL===   ")
    print ("-" * 20)
    print ("1. Comprar entrada    ")
    print ("2. Consultar comprador")
    print ("3. Cancelar compra    ")
    print ("4. Salir              ")


while True:
    menu()
    op = (input("Ingrese una de las siguientes opciones (1-4): "))
    if op == "1":
        comprar_entrada()
    elif op == "2":
        consultar_comprador()
    elif op == "3":
        cancelar_compra()
    elif op == "4":
        print("Cerrando el programa...")
        break
    else:
        print("Debe ingresar una opción válida!!")