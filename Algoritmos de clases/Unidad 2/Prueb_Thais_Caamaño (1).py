"""
🧾 Sistema de Gestión de Pacientes – Centro Médico DUOC
El Centro Médico DUOC necesita implementar un sistema básico de gestión de pacientes que le 
permita registrar, atender y consultar información clínica de manera rápida y eficiente. Con este fin, 
se les pide como programadores realicen un programa en Python que simule dicho sistema, el cual busca facilitar 
la administración básica de pacientes dentro de un entorno clínico.

🎯 Objetivo del Programa
El objetivo del programa es permitir al usuario:
Registrar los datos personales de un paciente.
Registrar una atención médica asociada a dicho paciente.
Consultar la información completa del paciente registrado.
Salir del sistema.

⚙️ Funcionamiento General
El sistema se basa en un menú interactivo con las siguientes opciones:
Registrar Paciente:

El sistema solicita los siguientes datos del paciente, con validaciones para asegurar la integridad:
RUT: Debe ser numérico, sin puntos ni dígito verificador, entre 5.000.000 y 99.999.999.
Nombre y Dirección: Entrada libre por texto.
Correo Electrónico: Debe contener exactamente un símbolo @. Se valida contando cuántos hay.
Edad: Debe ser un número entero entre 0 y 110 años.
Sexo: Se aceptan los valores F/f o M/m.
Plan de Salud: Solo se aceptan los valores ISAPRE o FONASA.
Atención Paciente:

Solicita el RUT del paciente para verificar si está registrado. Si coincide con el paciente registrado:
Solicita la fecha de atención y una observación médica.
Guarda esta información como registro de atención.
Consultar Datos del Paciente:
Muestra todos los datos ingresados del paciente, incluyendo el RUT, nombre, dirección, correo, edad, sexo, plan de 
salud y el registro de atención médica (si existe).

Salir:
Finaliza el programa.
"""

RUT =    None
NOMBRE = None
CORREO = None
EDAD =   None
SEXO =   None
SEXO1 = None
SALUD =  None
ARROBA = 0
ATENCIÓN1 = None
ATENCIÓN2 = None

while True:
    print ("---Sistema de gestión de pacientes---")
    print ("   1) Registrar datos del paciente")
    print ("   2) Registrar atención médica")
    print ("   3) Consultar información del paciente")
    print ("   4) Salir del sistema")
    menu1 = int(input("Ingrese a una de las opciones ingresando un numero: "))
    if menu1 == 1:
        while True:
                try:
                    RUT = int(input("Ingresa tu RUT (Sin guión ni tampoco el ultimo digito o letra): "))
                    if RUT >= 5000000 and RUT <= 99999999:
                        break
                    else:
                        print ()
                        print ("---Ingreso el RUT incorrectamente, vuelva a intentarlo---")
                        print ()
                except:
                    print()
                    print ("---Letra, numero o simbolo erroneo, porfavor haga caso a las instrucciones---")
                    print()

        NOMBRE = input("Ingrese su nombre y apellido: ")
        DIRECCIÓN = input ("Ingrese su dirección: ")

        while True:
                CORREO = input("Ingrese su correo: ")
                for CARACTER in CORREO:
                    if CARACTER == "@":
                        ARROBA += 1
                if ARROBA == 1:
                    break
                if ARROBA == 0:
                    print ()
                    print ("---Su correo no contiene '@'. Ingreselo nuevamente con arroba---")
                    print()

        while True:
                try:
                    EDAD = int(input("Ingrese su edad: "))
                    if EDAD >= 0 and EDAD <= 110:
                        break
                    else:
                        print ()
                        print ("---Ingrese una edad validad (Maximo 110 - Minimo 0)---")
                        print ()

                except:
                    print ()
                    print ("---Letra, numero o simbolo erroneo, porfavor haga caso a las instrucciones---")
                    print ()
        

        while True:
                try:
                  SEXO = input("Ingresa el inicial de tu sexo (Femenino F/f | Masculino / M/m): ").lower()
                  if SEXO == "f":
                       SEXO1 == "Femenino"
                       break
                  elif SEXO == "m":
                       SEXO1 == "Masculino"
                       break
                  else:
                    print ()
                    print ("--Ingrese lo que se le indica porfavor---")
                    print ()

                except:
                    print ()
                    print ("---Letra, numero o simbolo erroneo, porfavor haga caso a las instrucciones---")
                    print ()


        while True:
                try:
                 SALUD = input ("Ingrese al plan de salud que pertenece (FONASA / ISAPRE): ").lower()
                 if SALUD == "fonasa":
                    
                    print ("---!Se a ingresado toda la información con exito¡---")
                   
                    break
                 elif SALUD == "isapre":
                
                    print ("---!Se a ingresado toda la información con exito!---")
                   
                 else:
                    print ()
                    print ("---Ingrese lo que se le indica porfavor---")
                    print()
                except:
                    print()
                    print ("---Letra, numero o simbolo erroneo, porfavor haga caso a las instrucciones---")
                    print()

    if menu1 == 2:
        if SALUD != None and SEXO != None and EDAD != None and CORREO != None and DIRECCIÓN != None and RUT != None:
            while True:
                try:
                    RUT2 = int(input("Ingrese el RUT que registro en el sistema: "))
                    if RUT2 == RUT:
                        break
                    else:
                        print ("---Porfavor. Ingrese el rut que registro anteriormente---")
                except:
                    print ("---Letra, numero o simbolo erroneo, porfavor haga caso a las instrucciones---")
            
            ATENCIÓN1 = input("Ingrese en que día quiere que se le atienda: ")
            ATENCIÓN2 = input("Ingrese porque quiere pedir hora: ")

        else:
            print ("---Usted no se a registrado al sistema aun---")

    if menu1 == 3:
        if SALUD != None and SEXO != None and EDAD != None and CORREO != None and DIRECCIÓN != None and RUT != None:
            print ()
            print ("---DATOS DEL PACIENTE---")
            print (f" 1) RUT = {RUT}")
            print (f" 2) NOMBRE = {NOMBRE}")
            print (f" 3) SEXO = {SEXO1}")
            print (f" 4) EDAD = {EDAD} ")
            print (f" 5) DIRECCIÓN = {DIRECCIÓN}")
            print (f" 6) CORREO = {CORREO}")
            print (f" 7) PLAN DE SALUD = {SALUD}")
            print ("---------------------------------")
            print (f"HORA QUE QUIERE SE LE ATIENDA = SIN DATOS")
            print (f"OBSERVACIÓN: SIN DATOS")
            print()

        if SALUD != None and SEXO != None and EDAD != None and CORREO != None and DIRECCIÓN != None and RUT != None and ATENCIÓN1 != None and ATENCIÓN2 != None:
            print ()
            print ("---DATOS DEL PACIENTE---")
            print (f" 1) RUT = {RUT}")
            print (f" 2) NOMBRE = {NOMBRE}")
            print (f" 3) SEXO = {SEXO1}")
            print (f" 4) EDAD = {EDAD} ")
            print (f" 5) DIRECCIÓN = {DIRECCIÓN}")
            print (f" 6) CORREO = {CORREO}")
            print (f" 7) PLAN DE SALUD = {SALUD}")
            print ("---------------------------------")
            print (f"HORA QUE QUIERE SE LE ATIENDA = {ATENCIÓN1}")
            print (f"OBSERVACIÓN: {ATENCIÓN2}")
            print()
    
        else:
            print ("---Usted no se a registrado al sistema aun---")


    if menu1 == 4:
        print ()
        print ("---SALIENDO DEL SISTEMA---")
        print ()
        break
        









