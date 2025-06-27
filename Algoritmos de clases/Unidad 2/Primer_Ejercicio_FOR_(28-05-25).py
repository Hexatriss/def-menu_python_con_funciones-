contador = 0
vocales = "aeiou"
palabra = input("Ingresa una palabra con vocales: ").lower()

for i in palabra:
    if i in vocales:
        contador += 1

print (f"La palabra tiene {contador} vocal(es).")


