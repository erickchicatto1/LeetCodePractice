def calcular_friccion(mu, normal):
    """Calcula la fuerza de fricción (Fr = mu * N)."""
    return mu * normal


# Datos de ejemplo
coeficiente_mu = 0.4  # Coeficiente de fricción (ej. madera sobre metal)
fuerza_normal = 50.0  # Fuerza normal en Newtons (N)

# Cálculo
fuerza_friccion = calcular_friccion(coeficiente_mu, fuerza_normal)
print(f"La fuerza de fricción es: {fuerza_friccion} N")
