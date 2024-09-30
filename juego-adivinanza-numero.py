##### VIDEO 5:50 hs
import random

def juego_adivinanza():
    # Generar un número del 1 al 100
    numero_secreto = random.randint(1,100) # para elegir entre números enteros
    intentos = 0
    adivinado = False

    # Primeras líneas del juego, saludo  
    print('¡Bienvenido al juego de adivnanza de número!')
    print('Debes adivinar un número entre el 1 y el 100')
    print('¡Intenta adivinar!')

    while not adivinado:
        # Solicitar un número del 1 al 100
        adivinanza = input('Introduzca un número del 1 al 100: ') # espera que se introduzca el nro

        # Verificar que la entrada sea un nro
        if adivinanza.isdigit():
            adivinanza = int(adivinanza) # convertimos de texto a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f'El número secreto es mayor a {adivinanza}')
            elif adivinanza > numero_secreto:
                print(f'El número secreto es menor a {adivinanza}')
            else:
                print(f'Felicitaciones el número secreto es {adivinanza} y lo has logrado en {intentos} intentos.')
        else:
            print(f'Por favor introduz<ca un número válido entre el 1 y el 100: ')


juego_adivinanza()