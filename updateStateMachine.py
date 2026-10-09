class StateMachine:
    def __init__(self):
        # Lista de estados válidos
        self.states = ['INICIO', 'PROCESANDO', 'FINALIZADO']
        # Estado inicial
        self.current_state = 'INICIO'

    def process_input(self, inp):
        if self.current_state == 'INICIO':
            if inp == 'iniciar':
                self.current_state = 'PROCESANDO'
            elif inp == 'reset':
                self.current_state = 'INICIO'

        elif self.current_state == 'PROCESANDO':
            if inp == 'completar':
                self.current_state = 'FINALIZADO'
            elif inp == 'error':
                self.current_state = 'INICIO'

        elif self.current_state == 'FINALIZADO':
            if inp == 'reiniciar':
                self.current_state = 'INICIO'

    def get_state(self):
        return self.current_state


# Ejemplo de uso:
machine = StateMachine()
print(f"Estado inicial: {machine.get_state()}")

# Enviando comandos
comandos = ['iniciar', 'completar', 'reiniciar']
for comando in comandos:
    machine.process_input(comando)
    print(f"Entrada: '{comando}' -> Estado actual: {machine.get_state()}")
