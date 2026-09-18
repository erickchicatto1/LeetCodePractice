#include <iostream>
#include <cmath>
#include <fstream>

// Constantes astrofísicas en unidades del Sistema Internacional (SI)
const double G = 6.67430e-11;      // Constante de gravitación universal (m^3 kg^-1 s^-2)
const double MASS_SUN = 1.989e30;  // Masa del Sol (kg)
const double AU = 1.496e11;        // Una Unidad Astronómica (distancia Tierra-Sol en metros)

int main() {
    // 1. Condiciones iniciales del planeta (la Tierra)
    double x = AU;                 // Posición inicial en el eje X (1 UA)
    double y = 0.0;                // Posición inicial en el eje Y
    double vx = 0.0;               // Velocidad inicial en X (m/s)
    double vy = 29780.0;           // Velocidad orbital media de la Tierra en Y (m/s)

    // 2. Parámetros de la simulación
    double dt = 86400.0;           // Paso de tiempo: 1 día en segundos
    double total_time = 365 * dt;  // Tiempo total: 1 año completo

    // Crear un archivo para guardar los datos de la órbita
    std::ofstream data_file("orbita.txt");
    if (!data_file.is_open()) {
        std::cerr << "Error al abrir el archivo para guardar datos." << std::endl;
        return 1;
    }

    std::cout << "Simulando órbita..." << std::endl;

    // 3. Bucle de simulación (Integración numérica)
    for (double t = 0; t < total_time; t += dt) {
        // Calcular la distancia actual al Sol (origen 0,0)
        double r = std::sqrt(x * x + y * y);

        // Calcular la fuerza de gravedad y la aceleración (F = G*M*m/r^2  ->  a = G*M/r^2)
        double acc = - (G * MASS_SUN) / (r * r * r);

        // Componentes de la aceleración en X e Y
        double ax = acc * x;
        double ay = acc * y;

        // Actualizar velocidades (Método de Euler)
        vx += ax * dt;
        vy += ay * dt;

        // Actualizar posiciones
        x += vx * dt;
        y += vy * dt;

        // Guardar posiciones en el archivo (convertidas a Unidades Astronómicas para leerlo más fácil)
        data_file << x / AU << " " << y / AU << "\n";
    }

    data_file.close();
    std::cout << "Simulación terminada. Datos guardados en 'orbita.txt'." << std::endl;

    return 0;
}
