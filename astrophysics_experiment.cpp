#include <iostream>
#include <cmath>
#include <iomanip>

// Constantes Astrofísicas Universales
const double G = 6.67430e-11;      // Constante de Gravitación Universal (m^3 kg^-1 s^-2)
const double SIGMA = 5.67037e-8;   // Constante de Stefan-Boltzmann (W m^-2 K^-4)
const double M_SOL = 1.989e30;     // Masa del Sol en kg

// 1. Tercera Ley de Kepler: Calcula el periodo orbital (en años) dado el semieje mayor (en UA)
double calcularPeriodoKepler(double semiejeMayorUA) {
    // T^2 = a^3 (para órbitas alrededor del Sol si T está en años y 'a' en Unidades Astronómicas)
    return std::sqrt(std::pow(semiejeMayorUA, 3));
}

// 2. Velocidad de Escape: v = sqrt(2 * G * M / R)
double calcularVelocidadEscape(double masaKG, double radioMetros) {
    return std::sqrt((2.0 * G * masaKG) / radioMetros);
}

// 3. Luminosidad Estelar: L = 4 * pi * R^2 * sigma * T^4
double calcularLuminosidad(double radioMetros, double temperaturaKelvin) {
    double areaSuperficie = 4.0 * M_PI * std::pow(radioMetros, 2);
    return areaSuperficie * SIGMA * std::pow(temperaturaKelvin, 4);
}

int main() {
    // Configurar la salida para mostrar notación científica limpia
    std::cout << std::fixed << std::setprecision(2);

    std::cout << "=== DEMOSTRACIÓN DE ASTROFÍSICA BÁSICA EN C++ ===\n\n";

    // --- Prueba 1: Periodo de Júpiter ---
    double distanciaJupiter = 5.20; // 5.2 UA del Sol
    double periodoJupiter = calcularPeriodoKepler(distanciaJupiter);
    std::cout << "1. Tercera Ley de Kepler:\n";
    std::cout << "   Un planeta a " << distanciaJupiter << " UA del Sol tarda " 
              << periodoJupiter << " anos terrestres en dar una vuelta.\n\n";

    // --- Prueba 2: Velocidad de escape de la Tierra ---
    double masaTierra = 5.972e24; // kg
    double radioTierra = 6.371e6;  // metros (6371 km)
    double vEscapeTierra = calcularVelocidadEscape(masaTierra, radioTierra);
    std::cout << "2. Velocidad de Escape:\n";
    std::cout << "   La velocidad de escape de la Tierra es: " << (vEscapeTierra / 1000.0) << " km/s.\n\n";

    // --- Prueba 3: Luminosidad del Sol ---
    double radioSol = 6.9634e8;      // metros
    double tempSol = 5778;           // Kelvin
    double luminosidadSol = calcularLuminosidad(radioSol, tempSol);
    std::cout << "3. Luminosidad Estelar (Ley de Stefan-Boltzmann):\n";
    std::cout << "   La energia total emitida por el Sol es: " << std::scientific << luminosidadSol << " Vatios (W).\n";

    return 0;
}
