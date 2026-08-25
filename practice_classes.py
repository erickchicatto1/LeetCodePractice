class Personaje:
    # 1. El constructor: inicializa los atributos del objeto
    def __init__(self, nombre, clase, nivel=1):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.vida_maxima = 100 * nivel
        self.vida_actual = self.vida_maxima
        self.ataque = 15 * nivel

    # 2. Método para mostrar la información del personaje
    def mostrar_estado(self):
        print(f"\n--- Estado de {self.nombre} ---")
        print(f"Clase: {self.clase}")
        print(f"Nivel: {self.nivel}")
        print(f"Vida: {self.vida_actual}/{self.vida_maxima}")
        print(f"Ataque: {self.ataque}")
        print("-" * 25)

    # 3. Método para atacar a otro personaje
    def atacar(self, otro_personaje):
        print(f"\n{self.nombre} ataca a {otro_personaje.nombre} causando {self.ataque} de daño.")
        otro_personaje.recibir_dano(self.ataque)

    # 4. Método para recibir daño
    def recibir_dano(self, cantidad):
        self.vida_actual -= cantidad
        if self.vida_actual <= 0:
            self.vida_actual = 0
            print(f"¡{self.nombre} ha sido derrotado! 💀")
        else:
            print(f"A {self.nombre} le quedan {self.vida_actual} puntos de vida.")

    # 5. Método para subir de nivel
    def subir_nivel(self):
        self.nivel += 1
        self.vida_maxima = 100 * self.nivel
        self.vida_actual = self.vida_maxima  # Recupera toda la vida al subir
        self.ataque = 15 * self.nivel
        print(f"\n¡{self.nombre} ha subido al nivel {self.nivel}! 🎉")


# --- ZONA DE PRUEBAS ---

# Creamos dos instancias (objetos) de la clase Personaje
guerrero = Personaje("Aragorn", "Guerrero", nivel=1)
mago = Personaje("Gandalf", "Mago", nivel=1)

# Mostramos su estado inicial
guerrero.mostrar_estado()
mago.mostrar_estado()

# Simulamos un combate
guerrero.atacar(mago)

# El mago sube de nivel y contraataca
mago.subir_nivel()
mago.atacar(guerrero)

# Ver estado final
guerrero.mostrar_estado()
mago.mostrar_estado()
