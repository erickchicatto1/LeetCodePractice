"""
Conceptos básicos de Termodinámica en Python
=============================================
Este script implementa fórmulas y ejemplos de:
1. Ley de los gases ideales
2. Primera ley de la termodinámica
3. Trabajo en procesos termodinámicos (isotérmico, isobárico)
4. Calor sensible (calor específico)
5. Eficiencia del ciclo de Carnot
6. Cambio de entropía
"""

import math

# Constante universal de los gases (J / mol·K)
R = 8.314


# ---------------------------------------------------------
# 1. LEY DE LOS GASES IDEALES:  P·V = n·R·T
# ---------------------------------------------------------
def ley_gases_ideales(P=None, V=None, n=None, T=None):
    """
    Calcula la variable faltante de la ecuación P*V = n*R*T.
    Pasa None en la variable que quieras calcular.
    P: presión (Pa), V: volumen (m^3), n: moles, T: temperatura (K)
    """
    if P is None:
        return (n * R * T) / V
    if V is None:
        return (n * R * T) / P
    if n is None:
        return (P * V) / (R * T)
    if T is None:
        return (P * V) / (n * R)
    raise ValueError("Debes dejar una variable como None para calcularla.")


# ---------------------------------------------------------
# 2. PRIMERA LEY DE LA TERMODINÁMICA:  ΔU = Q - W
# ---------------------------------------------------------
def primera_ley(Q=None, W=None, delta_U=None):
    """
    Calcula la variable faltante: ΔU = Q - W
    Q: calor añadido al sistema (J)
    W: trabajo hecho por el sistema (J)
    delta_U: cambio de energía interna (J)
    """
    if delta_U is None:
        return Q - W
    if Q is None:
        return delta_U + W
    if W is None:
        return Q - delta_U
    raise ValueError("Debes dejar una variable como None para calcularla.")


# ---------------------------------------------------------
# 3. TRABAJO EN PROCESOS TERMODINÁMICOS
# ---------------------------------------------------------
def trabajo_isobarico(P, V_inicial, V_final):
    """Trabajo a presión constante: W = P * ΔV"""
    return P * (V_final - V_inicial)


def trabajo_isotermico(n, T, V_inicial, V_final):
    """Trabajo a temperatura constante: W = n*R*T*ln(Vf/Vi)"""
    return n * R * T * math.log(V_final / V_inicial)


# ---------------------------------------------------------
# 4. CALOR SENSIBLE:  Q = m * c * ΔT
# ---------------------------------------------------------
def calor_sensible(masa, calor_especifico, T_inicial, T_final):
    """
    Calcula el calor necesario para cambiar la temperatura de una sustancia.
    masa: kg, calor_especifico: J/(kg·K), temperaturas en K o °C (misma escala)
    """
    return masa * calor_especifico * (T_final - T_inicial)


# ---------------------------------------------------------
# 5. EFICIENCIA DEL CICLO DE CARNOT
# ---------------------------------------------------------
def eficiencia_carnot(T_frio, T_caliente):
    """
    Eficiencia máxima teórica de una máquina térmica: n = 1 - Tc/Th
    Las temperaturas deben estar en Kelvin.
    """
    return 1 - (T_frio / T_caliente)


# ---------------------------------------------------------
# 6. CAMBIO DE ENTROPÍA (proceso reversible a T constante)
# ---------------------------------------------------------
def cambio_entropia(Q, T):
    """ΔS = Q / T  (T en Kelvin, Q en Joules)"""
    return Q / T


# ---------------------------------------------------------
# DEMOSTRACIÓN / EJEMPLOS DE USO
# ---------------------------------------------------------
if __name__ == "__main__":
    print("=== 1. Ley de los gases ideales ===")
    T_calculada = ley_gases_ideales(P=101325, V=0.024, n=1)
    print(f"Temperatura de 1 mol de gas a 101325 Pa y 0.024 m^3: {T_calculada:.2f} K\n")

    print("=== 2. Primera ley de la termodinámica ===")
    dU = primera_ley(Q=500, W=200)
    print(f"Si Q = 500 J y W = 200 J, entonces ΔU = {dU} J\n")

    print("=== 3. Trabajo termodinámico ===")
    w_isob = trabajo_isobarico(P=101325, V_inicial=0.01, V_final=0.02)
    print(f"Trabajo isobárico (P=101325 Pa, ΔV=0.01 m^3): {w_isob:.2f} J")

    w_isot = trabajo_isotermico(n=1, T=300, V_inicial=0.01, V_final=0.02)
    print(f"Trabajo isotérmico (n=1 mol, T=300 K, V: 0.01→0.02 m^3): {w_isot:.2f} J\n")

    print("=== 4. Calor sensible ===")
    Q_agua = calor_sensible(masa=1, calor_especifico=4186, T_inicial=20, T_final=80)
    print(f"Calor para calentar 1 kg de agua de 20°C a 80°C: {Q_agua:.2f} J\n")

    print("=== 5. Eficiencia de Carnot ===")
    eficiencia = eficiencia_carnot(T_frio=300, T_caliente=600)
    print(f"Eficiencia máxima entre 300 K y 600 K: {eficiencia * 100:.1f} %\n")

    print("=== 6. Cambio de entropía ===")
    dS = cambio_entropia(Q=1000, T=300)
    print(f"Cambio de entropía con Q=1000 J a T=300 K: {dS:.2f} J/K")
