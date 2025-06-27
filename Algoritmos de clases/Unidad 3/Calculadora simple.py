"""
Actividad 2
Se pide escribir las instrucciones necesarias para crear un menú con las opciones de:
• Calcular_Iva
• Descuento
• Calcular_Imc
Las cuales deben ser desarrolladas en funciones (métodos).
Donde:
• Calcular_Iva: Es el precio del producto, multiplicado por el 19% (0.19)
• descuento: Es el precio del producto menos el descuento por aplicar. Mostrar el valor
final del producto.
• Calcular_Imc: Índice de masa corporal. Su fórmula es: peso/estatura ** 2
Además se debe mostrar el estado
de la persona de acuerdo a la
siguiente tabla
"""
def menu():
    print("---Calculadora simple---")
    print ("1. Calcular_Iva")
    print ("2. Descuento")
    print ("3. Calcular_Imc")
    print ("4. Salir")

def Calcular_Iva():
    precio = int(input("Indique el precio de su compra: "))
    resultado = precio * 0.19
    resultado2 = resultado + precio
    print (f"El resultado de la formula es : ${resultado2}")


def descuento():
    precio2 = int(input("Indique el valor de su compra para hacerle un descuento del 20%: "))
    resultado = precio2 - (precio2 * 0.20)
    print (f"El resultado de la formula es : ${resultado}")

def Calcular_Imc():
    peso = int(input("Indique su peso corporal actual: "))
    estatura = float(input("Indique su estatura actual: "))
    resultado = peso/estatura ** 2
    print(f"Usted pesa {resultado}")

    if resultado < 18:
        print ("Usted esta bajo peso")

    elif resultado >= 18 and resultado < 25:
        print ("Usted tiene un peso normal")
    
    elif resultado >= 25 and resultado < 30:
        print ("Usted esta a exceso de peso")
    
    elif resultado >= 30 and resultado < 35:
        print ("Usted tiene obesidad grado I")

    elif resultado >= 35 and resultado < 40:
        print ("Usted tiene obesidad grado II")

    elif resultado >= 40 and resultado < 45:
        print ("Usted tiene obesidad grado III")

while True:
    try:
        menu()
        OP = int(input("Elija una de las opciones (1-4): "))
        if OP == 1:
            Calcular_Iva()
        elif OP == 2:
            descuento()
        elif OP == 3:
            Calcular_Imc()
        elif OP == 4:
            print ("Cerrando programa...")
            break
        else:
            print ("Eliga una opción valida porfavor.")
    except:
        print("Ingrese un valor valido porfavor.")



        



