#Control de Acceso al Laboratorio de Biotecnología. 
print ("---UNIVERSIDAD INNOVACIÓN GLOBAL: CONTROL DE ACCESO AL LABORATIO DE BIOTECNLOGÍA---")
rol = int (input("Ingrese el numero 1 si es Estudiante. Si es investigador presione 2: "))
proyectos = int(input("Indiqueme cual es su numero de proyectos activos actualmente: "))
puntaje = int(input("Indiqueme cual es su puntaje de seguridad: "))

if rol == 2 and proyectos > 3 and puntaje >= 90:
    print ("Usted obtuvo el Acceso Prioritario: Ingrese al salon del lado izquierdo.") 
if rol == 1 and proyectos > 1 and puntaje >= 70 and puntaje <= 89:
    print ("Usted obtuvo el Acceso con Acompañante: Ingrese al salon del lado derecho.")
else:
    print ("ACCESO DENEGADO: Usted no puede ingresar al laboratorio de biotecnología.")

print ("---FIN DEL SISTEMA---")