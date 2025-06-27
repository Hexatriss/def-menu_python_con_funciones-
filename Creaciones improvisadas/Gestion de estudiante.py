"""
🏥 Sistema de Gestión de Estudiantes – Instituto Profesional "Aurora"

El Instituto Profesional "Aurora" necesita un sistema básico para gestionar estudiantes, sus matrículas y registros académicos. 
Debes crear un programa en Python que permita:
🎯 Opciones del Menú Principal:

    Registrar Estudiante

        ID Estudiante: Número único de 6 dígitos (entre 100000 y 999999).
        Nombre completo: Texto libre (mínimo 3 caracteres).
        Carrera: Solo aceptar "Informática", "Administración" o "Diseño".
        Edad: Entero entre 16 y 80 años.
        Email: Debe contener @ 

    Registrar Matrícula

        Solicitar el ID del estudiante. Si existe:

            Añadir semestre (1 o 2, solo 2024).
    Consultar Datos

        Mostrar:

            Datos personales del estudiante.
            Historial de matrículas (semestre y asignaturas).

    Salir

⚙️ Validaciones Importantes:
    El ID debe ser único.
    No se puede matricular un estudiante sin antes registrarlo.
"""
ID = None
NOMBRE = None
CARRERA = None
EDAD = None
GMAIL = None
SEMESTRE = None
ASIGNATURA = None
SEMESTRE1 = 0
ARROBA = 0

while True:
    print (" ---GESTIÓN DE ESTUDIANTES - INSTITUTO PROFESIONAL: 'AURORA'")
    print ("  1) Registrar Estudiante")
    print ("  2) Registrar Matricula ")
    print ("  3) Consultar Datos     ")
    print ("  4) Salir               ")
    menu1 = int(input("Ingrese el digito de alguna de las opciones del menú: "))

    if menu1 == 1:
            while True:
                try:
                 ID = int(input("Ingrese su ID como estudiante: "))
                 if ID >= 100000 and ID <= 999999:
                    break
                 else:
                    print ("---Agregue una ID que sea compatible---")
                except:
                    print ("--Siga las instrucciones como corresponda. Porfavor---")

            while True:
                try:
                 CARRERA = input("Ingrese la carrera a la que pertenece ('Informática' - 'Administración' - 'Diseño'): ").lower()
                 if CARRERA == "informática" or CARRERA == "administración" or CARRERA == "diseño":
                    break
                 else:
                    print ("---Agregue una carrera que este dentro del instituto---")
                except:
                    print ("--Siga las instrucciones como corresponda. Porfavor---")
                
            while True:
                try:
                    EDAD = int(input("Ingrese su edad: "))
                    if EDAD >= 18 and EDAD <= 80:
                        break
                    else:
                        print ("---La edad que ingreso no es valida para el instituto---")
                except:
                    print ("--Siga las instrucciones como corresponda. Porfavor---")

            while True:
                    EMAIL = input("Ingrese su correo electronico (Incluyendo un arroba obligatoriamente): ")
                    for i in EMAIL:
                        if i == "@":
                            ARROBA += 1

                    if ARROBA == 1:
                        break
                    if ARROBA == 0:
                        print ("---Debe ingresar un '@' para poder registrarse---")
    if menu1 == 2:
        if ID != None and CARRERA != None and EDAD != None and EMAIL != None:
            while True:
                try:
                 ID2 = int(input("Ingrese su ID nuevamente para asegurar su persona: "))
                 if ID2 == ID:
                    break
                 else:
                    print("---ID invalido. Porfavor vuelva a ingresarlo nuevamente---")
                except:
                    print ("--Siga las instrucciones como corresponda. Porfavor---")

            while True:
                SEMESTRE = input("Ingrese a que semestre pertenece en estos momentos (1 - 2): ")
                for i in SEMESTRE:
                    if i == "1":
                        SEMESTRE1 += 1
                    if i == "2":
                        SEMESTRE1 += 1
                    else:
                        SEMESTRE1 = 0

                if SEMESTRE1 == 1:
                    break
                if SEMESTRE1 == 0:
                    print ("--Siga las instrucciones como corresponda. Porfavor---")
        else:
            print ("---Antes de registrar matricula debe registrarse como usuario---")
    
    if menu1 == 3:
        if ID != None and CARRERA != None and EDAD != None and EMAIL != None:
            print ("---DATOS DEL ESTUDIANTE---")
            print (f"   1)ID = {ID}")
            print (f"   2)CARRERA = {CARRERA}")
            print (f"   3)EDAD = {EDAD}")
            print (f"   4)EMAIL = {EMAIL}")
            print ("    5)SEMESTRE = SIN DATOS")
        if ID != None and CARRERA != None and EDAD != None and EMAIL != None and SEMESTRE != None:
            print ("---DATOS DEL ESTUDIANTE---")
            print (f"   1)ID = {ID}")
            print (f"   2)CARRERA = {CARRERA}")
            print (f"   3)EDAD = {EDAD}")
            print (f"   4)EMAIL = {EMAIL}")
            print (f"   5)SEMESTRE = {SEMESTRE}")
        else:
            print("---Debe de registrarse primero---")
    
    if menu1 == 4:
        print ("---CERRANDO SISTEMA---")
        break



            






                     







