print ("---¡Bienvenido a la montaña rusa 'The Cyclone'!---")
creditos = int(input("Ingrese cuantos créditos tiene para entrar: "))
altura = float(input("Ingrese cual es su altura en centimetros (Ej: 1.70 - 1.82 - 1.68): "))

if altura >= 1.37 and creditos >= 10:
    print ("---Puedes entrar: ¡Disfruta de tu Viaje!---")
elif altura < 1.37 and creditos >= 10:
    print ("---Lo lamento: No eres lo suficientemente alto para poder entrar.---")
elif altura >= 1.37 and creditos < 10:
    print ("---Lo lamento: No tienes lo suficientes creditos para poder entrar---")
else:
    print ("---No tienes acceso: No eres lo suficientemente alto y le falta mas creditos---")


print ("---FIN DEL SISTEMA---")