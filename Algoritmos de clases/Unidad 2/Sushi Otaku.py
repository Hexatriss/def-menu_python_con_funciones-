"""
Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver 
el siguiente caso: En un delivery de Sushi vende 4 tipos de Sushi:
1. Pikachu Roll $4500
2. Otaku Roll $5000
3. Pulpo Venenoso Roll $5200
4. Anguila Eléctrica Roll $4800
La empresa le ha solicitado a usted, que genere una pequeña aplicación en Python
 para tomar el pedido de un cliente el cuál puede ir agregando Rolls 
a través de un menú uno por uno con solo seleccionar la opción (1 a 4)
La aplicación debe mostrar en un menú los Rolls que agregará el usuario, esto 
se debe repetir hasta que el usuario decida que su pedido está completo.
Luego de ello, debe preguntar al usuario si posee un código de descuento. En caso 
de que posea el código, deberá ingresarlo. Si el código ingresado 
es “soyotaku”, debe realizar un 10% de descuento al total del pedido, en caso 
contrario enviar el mensaje “código no válido” y dar al usuario la opción de reingresar
 el código o volver al menú tecleando “X”
Una vez realizado los pasos anteriores, debe mostrar el detalle del pedido 
contabilizando el total de productos y la cantidad de cada uno de ellos y si aplica o no el descuento

"""

pikachu_roll = 0
otaku_roll = 0
pulpo_roll = 0
anguila_roll = 0
cantidad_pikachu = 0
cantidad_otaku = 0
cantidad_pulpo = 0
cantidad_anguila = 0
total_de_productos = 0
CUENTA = 0
while True:
    try:
        print ("       ---Menu Delivery Sushi---")
        print (f"1)  Pikachu Roll x{cantidad_pikachu} =            $4500")
        print (f"2)  Otaku Roll x{cantidad_otaku} =              $5000")
        print (f"3)  Pulpo Venenoso Roll x{cantidad_pulpo} =     $5200")
        print (f"4)  Anguila Eléctrica Roll x{cantidad_anguila} =  $4800")
        print (f"5) ¡COMPRAR!                      CUENTA = ${CUENTA}")
        comprar = int(input("¡Ingrese a una de las opciones ingresando el numero indicado!: "))
        if comprar == 1:
            CUENTA += 4500
            pikachu_roll += 4500
            cantidad_pikachu += 1
            print ("¡Se ha ingresado 'Pikachu roll' al carro!")
        elif comprar == 2:
            CUENTA += 5000
            otaku_roll += 5000
            cantidad_otaku += 1
            print ("¡Se ha ingresado 'Otaku roll' al carro!")
        elif comprar == 3:
            CUENTA += 5200
            pulpo_roll += 5200
            cantidad_pulpo += 1
            print ("¡Se ha ingresado 'Pulpo venoso roll' al carro!")
        elif comprar == 4:
            CUENTA += 4800
            anguila_roll += 4800
            cantidad_anguila += 1
            print ("¡Se ha ingresado 'Anguila eléctrica roll' al carro!")
        elif comprar == 5:
            print ("¿Posee codigo de descuento?: ")
            print ("1) SI")
            print ("2) NO")

            codigo1 = int(input("¡Ingrese a una de las opciones ingresando el numero indicado!: "))
            if codigo1 == 1:
                while True:
                    print ("------ COLOQUE 'X' SI QUIERE SALIR DE ESTA VENTANA-----")
                    codigo2 = input("Ingrese el codigo de descuento: ").lower()
                    if codigo2 == "soyotaku":
                        DESCUENTO = CUENTA - (CUENTA * 0.10)
                        total_de_productos = cantidad_pikachu + cantidad_otaku + cantidad_pulpo + cantidad_anguila
                        print ("---Se ingreso el codigo correctamente---")
                        print ("       ---BOLETA---")
                        print (f"1)  Pikachu Roll x{cantidad_pikachu} =            ${pikachu_roll}")
                        print (f"2)  Otaku Roll x{cantidad_otaku} =              ${otaku_roll}")
                        print (f"3)  Pulpo Venenoso Roll x{cantidad_pulpo} =     ${pulpo_roll}")
                        print (f"4)  Anguila Eléctrica Roll x{cantidad_anguila} =  ${anguila_roll}")
                        print ("------------------------------------------------------------------------------")
                        print (f"                                  TOTAL DE PRODUCTOS =  {total_de_productos}")
                        print (f"                                  SUBTOTAL = ${CUENTA}")
                        print (f"                                  DESCUENTO = 10%")
                        print (f"                                  TOTAL = ${DESCUENTO}")
                        exit()

                    elif codigo2 == "x":
                        print ("---Saliendo de la ventana---")
                        break

                    else:
                        print ("---Codigo ingresado incorrecto. Pruebe nuevamente---")
                    
            if codigo1 == 2:
                total_de_productos = cantidad_pikachu + cantidad_otaku + cantidad_pulpo + cantidad_anguila
                print ("       ---BOLETA---")
                print (f"1)  Pikachu Roll x{cantidad_pikachu} =            ${pikachu_roll}")
                print (f"2)  Otaku Roll x{cantidad_otaku} =              ${otaku_roll}")
                print (f"3)  Pulpo Venenoso Roll x{cantidad_pulpo} =     ${pulpo_roll}")
                print (f"4)  Anguila Eléctrica Roll x{cantidad_anguila} =  ${anguila_roll}")
                print ("------------------------------------------------------------------------------")
                print (f"                                  TOTAL DE PRODUCTOS =  {total_de_productos}")
                print (f"                                  SUBTOTAL =       ${CUENTA}")
                print (f"                                  DESCUENTO =      'NO HAY DESCUENTO'")
                print (f"                                  ¡TOTAL! =        ${CUENTA}")
                exit()
                
    except ValueError:
        pikachu_roll = 0
        otaku_roll = 0
        pulpo_roll = 0
        anguila_roll = 0
        cantidad_pikachu = 0
        cantidad_otaku = 0
        cantidad_pulpo = 0
        cantidad_anguila = 0
        total_de_productos = 0
        CUENTA = 0
        print ()
        print ("---¡¡ACABA DE SURGIR UN ERROR!!---")
        print("----SE RESETEARA EL PROGRAMA----")
        print ("    ---PROGRAMA RESETEADO---")
        print ()      