#include <iostream>
#include <thread>
#include <chrono>

// Definimos los posibles estados
enum class Estado {
    ROJO,
    VERDE,
    AMARILLO
};

class Semaforo {
private:
    Estado estadoActual;

public:
    Semaforo() : estadoActual(Estado::ROJO) {}

    void transicionar() {
        switch (estadoActual) {
            case Estado::ROJO:
                std::cout << "Rojo -> Verde\n";
                estadoActual = Estado::VERDE;
                break;

            case Estado::VERDE:
                std::cout << "Verde -> Amarillo\n";
                estadoActual = Estado::AMARILLO;
                break;

            case Estado::AMARILLO:
                std::cout << "Amarillo -> Rojo\n";
                estadoActual = Estado::ROJO;
                break;
        }
    }

    Estado getEstado() const {
        return estadoActual;
    }

    void imprimirEstado() const {
        switch (estadoActual) {
            case Estado::ROJO:     std::cout << "Estado: ROJO\n"; break;
            case Estado::VERDE:    std::cout << "Estado: VERDE\n"; break;
            case Estado::AMARILLO: std::cout << "Estado: AMARILLO\n"; break;
        }
    }
};

int main() {
    Semaforo semaforo;

    for (int i = 0; i 
