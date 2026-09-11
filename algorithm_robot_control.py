# Función que calcula la velocidad del motor usando un controlador Proporcional
def control_proporcional(objetivo, actual, kp):
    # Calcula el error entre la posición deseada y la actual
    error = objetivo - actual
    
    # La velocidad es proporcional al error
    velocidad = kp * error
    
    return velocidad

# Posición deseada (ejemplo: 100 cm)
posicion_deseada = 100.0

# Posición actual del robot leída por un sensor (ejemplo: 20 cm)
posicion_actual = 20.0

# Constante proporcional (Kp) que define la fuerza de la respuesta
constante_kp = 0.5

# Simulación de un ciclo de control
for paso in range(5):
    # Calcula la nueva velocidad
    vel = control_proporcional(posicion_deseada, posicion_actual, constante_kp)
    
    # Simula el movimiento sumando una parte de la velocidad a la posición actual
    posicion_actual += vel
    
    print(f"Paso {paso + 1}: Posición actual = {posicion_actual:.1f}, Velocidad enviada = {vel:.1f}")
