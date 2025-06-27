print ("---BANCO DE CODEDÉX---")

contraseña = int(input("Ingrese la contraseña para acceder a su cuenta: "))

while contraseña != 1234:
    contraseña = int(input("Contraseña incorrecta. Intente nuevamente: "))

if contraseña:
    print ("¡A ingresado a la cuenta exitosamente!")