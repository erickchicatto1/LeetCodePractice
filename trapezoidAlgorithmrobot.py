import numpy as np
import matplotlib.pyplot as plt

def perfil_trapezoidal(pos_inicial, pos_final, v_max, a_max, dt=0.01):
    """
    Genera un perfil de velocidad trapezoidal para mover un robot
    desde pos_inicial hasta pos_final.

    Parámetros:
        pos_inicial: posición inicial (rad o m)
        pos_final:   posición final (rad o m)
        v_max:       velocidad máxima permitida
        a_max:       aceleración máxima permitida
        dt:          paso de tiempo de la simulación

    Retorna:
        t:  vector de tiempo
        pos: vector de posición
        vel: vector de velocidad
        acc: vector de aceleración
    """
    distancia = pos_final - pos_inicial
    signo = np.sign(distancia)
    distancia = abs(distancia)

    # Tiempo de aceleración para llegar a v_max
    t_acc = v_max / a_max
    d_acc = 0.5 * a_max * t_acc**2

    if 2 * d_acc >= distancia:
        # No alcanza v_max -> perfil triangular
        t_acc = np.sqrt(distancia / a_max)
        v_max = a_max * t_acc
        t_const = 0
    else:
        d_const = distancia - 2 * d_acc
        t_const = d_const / v_max

    t_total = 2 * t_acc + t_const
    t = np.arange(0, t_total, dt)

    pos = np.zeros_like(t)
    vel = np.zeros_like(t)
    acc = np.zeros_like(t)

    for i, ti in enumerate(t):
        if ti < t_acc:
            # Fase de aceleración
            acc[i] = a_max
            vel[i] = a_max * ti
            pos[i] = 0.5 * a_max * ti**2
        elif ti < t_acc + t_const:
            # Fase de velocidad constante
            acc[i] = 0
            vel[i] = v_max
            pos[i] = d_acc + v_max * (ti - t_acc)
        else:
            # Fase de desaceleración
            td = ti - (t_acc + t_const)
            acc[i] = -a_max
            vel[i] = v_max - a_max * td
            pos[i] = (d_acc + v_max * t_const) + (v_max * td - 0.5 * a_max * td**2)

    pos = pos_inicial + signo * pos
    vel = signo * vel
    acc = signo * acc

    return t, pos, vel, acc


# ---- Ejemplo de uso ----
if __name__ == "__main__":
    t, pos, vel, acc = perfil_trapezoidal(
        pos_inicial=0,
        pos_final=10,
        v_max=2.0,
        a_max=1.0
    )

    fig, axs = plt.subplots(3, 1, figsize=(8, 8), sharex=True)
    axs[0].plot(t, pos); axs[0].set_ylabel("Posición")
    axs[1].plot(t, vel); axs[1].set_ylabel("Velocidad")
    axs[2].plot(t, acc); axs[2].set_ylabel("Aceleración")
    axs[2].set_xlabel("Tiempo (s)")
    for ax in axs: ax.grid(True)
    plt.tight_layout()
    plt.savefig("perfil_trapezoidal.png")
    plt.show()
