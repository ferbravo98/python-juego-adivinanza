import random


def juego_Adivinanza():
    # Generar un numero del 1 al 50
    numero_secreto = random.randint(1, 50)
    intento = 0
    adivinado = False

    print("""+-+-+BIENVENIDO al juego de la adivinanza del numero+-+-""")
    print("Hay que adivinar el numero secreto del 1 al 50")
    print("""Comencemos""")
    while not adivinado:
        # Solicitar el numero del 1 al 50
        adivinanza = input("Ingrese un numero del 1 al 50 ")

        # Verificar si ingreso un numero entero
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Lo estamos pasando de texto a entero
            intento += 1

            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor a {adivinanza}")
            else:
                print(f"Felicitaciones has ganado. El numero {adivinanza} es el numero ganador y lo has logrado en {intento} intentos"
                )
                break
        else:
            print("ERROR al ingresar el numero, ingrese un valor del 1 al 50")


juego_Adivinanza()
