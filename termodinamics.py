"""
================================================================
MÓDULO DE FÓRMULAS DE TERMODINÁMICA
================================================================
Incluye:
  1. Ley de los gases ideales
  2. Primera ley de la termodinámica
  3. Trabajo termodinámico (procesos isotérmico, isobárico, adiabático)
  4. Calor específico y calorimetría
  5. Entropía
  6. Ciclo de Carnot (eficiencia y COP)
  7. Transferencia de calor (conducción, convección, radiación)

Unidades: Sistema Internacional (SI) salvo que se indique lo contrario.
================================================================
"""

import math

# ----------------------------------------------------------------
# CONSTANTES FÍSICAS
# ----------------------------------------------------------------
R = 8.314          # Constante de los gases ideales [J/(mol·K)]
Kb = 1.380649e-23   # Constante de Boltzmann [J/K]
SIGMA = 5.670374e-8 # Constante de Stefan-Boltzmann [W/(m^2·K^4)]


# ----------------------------------------------------------------
# 1. LEY DE LOS GASES IDEALES:  P V = n R T
# ----------------------------------------------------------------
def presion_gas_ideal(n, T, V):
    """Calcula la presión P = nRT / V   [Pa]"""
    return (n * R * T) / V


def volumen_gas_ideal(n, T, P):
    """Calcula el volumen V = nRT / P   [m^3]"""
    return (n * R * T) / P


def temperatura_gas_ideal(P, V, n):
    """Calcula la temperatura T = PV / (nR)   [K]"""
    return (P * V) / (n * R)


def moles_gas_ideal(P, V, T):
    """Calcula el número de moles n = PV / (RT)"""
    return (P * V) / (R * T)


# ----------------------------------------------------------------
# 2. PRIMERA LEY DE LA TERMODINÁMICA:  ΔU = Q - W
# ----------------------------------------------------------------
def primera_ley(Q=None, W=None, dU=None):
    """
    Calcula la variable faltante en ΔU = Q - W.
    Proporciona dos de los tres valores (Q, W, dU) y deja el tercero como None.
    """
    if dU is None:
        return Q - W
    elif Q is None:
        return dU + W
    elif W is None:
        return Q - dU
    else:
        raise ValueError("Debes dejar exactamente una variable como None")


# ----------------------------------------------------------------
# 3. TRABAJO TERMODINÁMICO
# ----------------------------------------------------------------
def trabajo_isobarico(P, V1, V2):
    """Trabajo a presión constante: W = P (V2 - V1)   [J]"""
    return P * (V2 - V1)


def trabajo_isotermico(n, T, V1, V2):
    """Trabajo a temperatura constante: W = nRT ln(V2/V1)   [J]"""
    return n * R * T * math.log(V2 / V1)


def trabajo_adiabatico(P1, V1, P2, V2, gamma):
    """
    Trabajo en proceso adiabático (sin transferencia de calor):
    W = (P1 V1 - P2 V2) / (gamma - 1)
    """
    return (P1 * V1 - P2 * V2) / (gamma - 1)


def relacion_adiabatica(P1, V1, V2, gamma):
    """Presión final en proceso adiabático: P1 V1^gamma = P2 V2^gamma"""
    return P1 * (V1 / V2) ** gamma


# ----------------------------------------------------------------
# 4. CALOR Y CALORIMETRÍA
# ----------------------------------------------------------------
def calor_sensible(m, c, dT):
    """Calor necesario para cambiar la temperatura: Q = m c ΔT   [J]"""
    return m * c * dT


def calor_latente(m, L):
    """Calor en cambio de fase (sin cambio de temperatura): Q = m L   [J]"""
    return m * L


def calor_molar_volumen_cte(n, Cv, dT):
    """Calor a volumen constante: Q = n Cv ΔT"""
    return n * Cv * dT


def calor_molar_presion_cte(n, Cp, dT):
    """Calor a presión constante: Q = n Cp ΔT"""
    return n * Cp * dT


# ----------------------------------------------------------------
# 5. ENTROPÍA
# ----------------------------------------------------------------
def entropia_proceso_reversible(Q, T):
    """Cambio de entropía en un proceso reversible: ΔS = Q / T   [J/K]"""
    return Q / T


def entropia_gas_ideal(n, Cv, T1, T2, V1, V2):
    """
    Variación de entropía de un gas ideal:
    ΔS = n Cv ln(T2/T1) + n R ln(V2/V1)
    """
    return n * Cv * math.log(T2 / T1) + n * R * math.log(V2 / V1)


# ----------------------------------------------------------------
# 6. CICLO DE CARNOT
# ----------------------------------------------------------------
def eficiencia_carnot(Tf, Tc):
    """
    Eficiencia máxima de una máquina de Carnot:
    η = 1 - Tf/Tc   (temperaturas en Kelvin)
    """
    return 1 - (Tf / Tc)


def cop_refrigerador_carnot(Tf, Tc):
    """Coeficiente de desempeño (COP) de un refrigerador de Carnot"""
    return Tf / (Tc - Tf)


def cop_bomba_calor_carnot(Tf, Tc):
    """COP de una bomba de calor de Carnot"""
    return Tc / (Tc - Tf)


# ----------------------------------------------------------------
# 7. TRANSFERENCIA DE CALOR
# ----------------------------------------------------------------
def conduccion_calor(k, A, dT, espesor, t=1):
    """
    Ley de Fourier (conducción): Q = k A ΔT t / L
    k: conductividad térmica [W/(m·K)]
    A: área [m^2], t: tiempo [s], L: espesor [m]
    """
    return (k * A * dT * t) / espesor


def conveccion_calor(h, A, dT):
    """Ley de enfriamiento de Newton (convección): Q = h A ΔT   [W]"""
    return h * A * dT


def radiacion_calor(emisividad, A, T):
    """
    Ley de Stefan-Boltzmann (radiación): Q = ε σ A T^4   [W]
    T en Kelvin
    """
    return emisividad * SIGMA * A * T**4


# ----------------------------------------------------------------
# EJEMPLOS DE USO
# ----------------------------------------------------------------
if __name__ == "__main__":
    print("=== Ejemplos de uso ===\n")

    # 1. Gas ideal
    P = presion_gas_ideal(n=1, T=300, V=0.0224)
    print(f"Presión gas ideal: {P:.2f} Pa")

    # 2. Primera ley
    dU = primera_ley(Q=500, W=200)
    print(f"ΔU (primera ley): {dU} J")

    # 3. Trabajo isotérmico
    W_iso = trabajo_isotermico(n=1, T=300, V1=0.01, V2=0.02)
    print(f"Trabajo isotérmico: {W_iso:.2f} J")

    # 4. Calor sensible
    Q = calor_sensible(m=2, c=4186, dT=10)
    print(f"Calor sensible: {Q} J")

    # 5. Entropía
    dS = entropia_proceso_reversible(Q=1000, T=300)
    print(f"ΔS: {dS:.3f} J/K")

    # 6. Eficiencia de Carnot
    eta = eficiencia_carnot(Tf=300, Tc=600)
    print(f"Eficiencia de Carnot: {eta*100:.1f} %")

    # 7. Radiación
    Qr = radiacion_calor(emisividad=0.9, A=1, T=400)
    print(f"Calor por radiación: {Qr:.2f} W")
