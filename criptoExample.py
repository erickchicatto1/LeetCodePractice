from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

# 1. Generar la clave privada DSA (tamaño recomendado: 2048 bits)
clave_privada = dsa.generate_private_key(key_size=2048)

# 2. Extraer la clave pública a partir de la privada
clave_publica = clave_privada.public_key()

# Mensaje a firmar (debe estar en bytes)
mensaje = b"Transferencia autorizada por $5,000 MXN"

# 3. Firmar el mensaje usando la clave privada y SHA-256
firma = clave_privada.sign(mensaje, hashes.SHA256())
print("Firma generada (en hexadecimal):", firma.hex()[:60] + "...")

# 4. Verificar la firma usando la clave pública
try:
    clave_publica.verify(firma, mensaje, hashes.SHA256())
    print("✅ Éxito: La firma es válida y el mensaje no fue alterado.")
except InvalidSignature:
    print("❌ Error: La firma no es válida.")
