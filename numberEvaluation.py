def evaluar_numero(numero: int) -> str:
    """Devuelve si un número es par o impar."""
    if numero % 2 == 0:
        return "par"
    return "impar"

def juego_logica():
    secreto = 7
    intentos = 0
    print("Adivina el número secreto del 1 al 10")
    
    while True:
        entrada = input("Escribe un número: ")
        
        # Validar que sea un número entero
        if not entrada.isdigit():
            print("Por favor, ingresa solo números válidos.")
            continue
            
        numero = int(entrada)
        intentos += 1
        
        if numero == secreto:
            print(f"¡Ganaste en {intentos} intentos!")
            break
        elif numero < secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

if __name__ == "__main__":
    juego_logica()
