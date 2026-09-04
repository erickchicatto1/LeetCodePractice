import matplotlib.pyplot as plt
import numpy as np

def generar_perfil_trapezoidal(q0, q1, v_max, a_max, dt=0.01):
    """
    Genera un perfil de movimiento trapezoidal para un robot.
    
    Parámetros:
    q0    : Posición inicial (ej. grados o metros)
    q1    : Posición final
    v_max : Velocidad máxima permitida
    a_max : Aceleración máxima permitida
    dt    : Paso del tiempo de muestreo (ciclo de control)
    """
    distancia = q1 - q0
    direccion = 1 if distancia >= 0 else -1
    D = abs(distancia)
    
    # Tiempo necesario para acelerar hasta v_max
    t_acc = v_max / a_max
    # Distancia recorrida durante la aceleración
    d_acc = 0.5 * a_max * (t_acc ** 2)
    
    # Condición: ¿Hay espacio suficiente para alcanzar la v_max?
    if 2 * d_acc > D:
        # Perfil Triangular: No alcanza v_max, se empieza a desacelerar a mitad de camino
        d_acc = D / 2
        t_acc = np.sqrt(2 * d_acc / a_max)
        v_max = a_max * t_acc
        t_flat = 0
    else:
        # Perfil Trapezoidal clásico
        d_flat = D - 2 * d_acc
        t_flat = d_flat / v_max
        
    t_total = 2 * t_acc + t_flat
    
    # Inicializar vectores de trayectoria
    tiempos = np.arange(0, t_total + dt, dt)
    posiciones = []
    velocidades = []
    aceleraciones = []
    
    for t in tiempos:
        if t < t_acc:
            # Fase 1: Aceleración
            a = a_max
            v = a_max * t
            p = 0.5 * a_max * (t ** 2)
        elif t < (t_acc + t_flat):
            # Fase 2: Velocidad Constante (Crucero)
            a = 0
            v = v_max
            p = d_acc + v_max * (t - t_acc)
        else:
            # Fase 3: Desaceleración
            t_dec = t - t_acc - t_flat
            a = -a_max
            v = v_max - a_max * t_dec
            p = d_acc + d_flat + (v_max * t_dec - 0.5 * a_max * (t_dec ** 2))
            
        # Aplicar la dirección real del movimiento
        aceleraciones.append(a * direccion)
        velocidades.append(v * direccion)
        posiciones.append(q0 + p * direccion)
        
    return tiempos, posiciones, velocidades, aceleraciones

# --- PRUEBA DEL ALGORITMO ---
# Mover la articulación de un robot de 0 a 90 grados
t, p, v, a = generar_perfil_trapezoidal(q0=0, q1=90, v_max=20, a_max=10, dt=0.05)

# Graficar Resultados
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, p, 'r', linewidth=2)
plt.title('Perfil Trapezoidal de Movimiento')
plt.ylabel('Posición (Grados)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, v, 'g', linewidth=2)
plt.ylabel('Velocidad (Grados/s)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, a, 'b', linewidth=2)
plt.ylabel('Aceleración (Grados/s²)')
plt.xlabel('Tiempo (s)')
plt.grid(True)

plt.tight_layout()
plt.show()
