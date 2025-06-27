#Selección de casas magicas (⌐■_■)
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Syltherin = 0
print ("--El gorro del Colegio Hogwarts de Magia y Hechizeria Te guiara a una casa dependiendo de lo que respondas a continuación:---")

print ("¿Que te gusta mas, el 'Atardecer' o el 'Amanecer'?: ")
print ("   1) Amanecer")
print ("   2) Atardecer")
Q1 = int(input("¡Responde ingresando el numero que indique tu respuesta!: "))

if Q1 == 1:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif Q1 == 2:
    Hufflepuff = Hufflepuff + 1
    Syltherin = Syltherin + 1
else:
    print ("Entrada incorrecta.")

print ("Cuando muera, quiero que la gente me recuedo como...: ")
print ("   1) El Bueno")
print ("   2) El Genial")
print ("   3) El Sabio")
print ("   4) El Audaz")
Q2 = int(input("¡Responde ingresando el numero que indique tu respuesta!: "))

if Q2 == 1:
    Hufflepuff = Hufflepuff + 2
elif Q2 == 2:
    Syltherin = Syltherin + 2
elif Q2 == 3:
    Ravenclaw = Ravenclaw + 2
elif Q2 == 4:
    Gryffindor = Gryffindor + 2
else:
    print ("Entrada incorrecta.")

print ("¿Que tipo de instrumento agrada mas a tu oído?: ")
print ("   1) El Violín")
print ("   2) La Trompeta")
print ("   3) El Piano")
print ("   4) El Tambor")
Q3 = int(input("¡Responde ingresando el numero que indique tu respuesta!: "))

if Q3 == 1:
    Syltherin = Syltherin + 4
elif Q3 == 2:
    Hufflepuff = Hufflepuff + 4
elif Q3 == 3:
    Ravenclaw = Ravenclaw + 4
elif Q3 == 4:
    Gryffindor = Gryffindor + 4
else:
    print ("Entrada incorrecta.")

print ("---A continuacion se presentaran los puntos obtenidos de cada uno---: ")
print ("----------------------------")
print (f"  🦁 Gryffindor: {Gryffindor}")
print (f"  🦅 Ravenclaw: {Ravenclaw}")
print (f"  🦡 Hufflepuff: {Hufflepuff}")
print (f"  🐍 Syltherin: {Syltherin}")
print ("----------------------------")

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and  Gryffindor > Syltherin:
    print ("---La casa que usted va ingresar es: 🦁 Gryffindo---")
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Syltherin:
    print ("---La casa que usted va ingresar es: 🦅 Ravenclaw---")
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Syltherin:
    print ("---La casa que usted va ingresar es:: 🦡 Hufflepuff---")
elif Syltherin > Gryffindor and Syltherin > Ravenclaw and Syltherin > Hufflepuff:
    print ("---La casa que usted va ingresar es: 🐍 Syltherin---")
else:
    print ("---Usted no puede ingresar a ninguna casa porque obtuvo cero puntos en todos---")


print ("---FIN DEL HECHIZO---")











