# Calculo de bonos "FuturoTech S.A." ⚖
salario = int(input("Ingrese cual es su salario actual: "))
desempeño = int(input("Ingrese cual es su desempeño del 1 al 10: "))
antiguedad = int(input("Ingrese cuantos años a estado en la empresa: "))
if desempeño == 9 or desempeño == 10 and antiguedad > 5:
    resultado = salario * 0.20
    print ("Usted obtuvo el bono del 20%")
    print (f"Su salario al calcularlo con el bono es: {resultado:0f}")
elif desempeño == 7 or desempeño == 8 or antiguedad == 5:
    resultado = salario * 0.10
    print ("Usted obtuvo el bono del 10%")
    print (f"Su salario al calcularlo con el bono es: {resultado:.0f}")
elif desempeño == 6 and antiguedad < 5:
    resultado = salario * 0.5
    print ("Usted obtuvo el bono del 5%")
    print (f"Su salario al calcularlo con el bono es: {resultado:.0f}")
else:
    print ("Usted no obtuvo ningún bono...")

