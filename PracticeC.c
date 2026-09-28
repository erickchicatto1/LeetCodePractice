#include <stdio.h> // Librería estándar de entrada y salida

// Definición de una constante
#define GRAVEDAD 9.81

int main() {
    // 1. Comentarios y tipos de datos básicos
    // Los comentarios de una línea usan doble barra
    int edad = 20;               // Entero (4 bytes aprox.)
    float altura = 1.75;         // Decimal de simple precisión
    char inicial = 'A';          // Un solo carácter
    double pi = 3.1415926535;    // Decimal de doble precisión

    // 2. Operadores aritméticos básicos
    int a = 10, b = 5;
    int suma = a + b; // Operador suma (+)

    // 3. Salida de datos en consola (printf)
    printf("--- CONCEPTOS BASICOS EN C ---\n");
    printf("Edad: %d anios\n", edad);        // %d para enteros
    printf("Altura: %.2f metros\n", altura); // %.2f para decimales con 2 dígitos
    printf("Inicial: %c\n", inicial);        // %c para caracteres
    printf("Constante Gravedad: %.2f\n", GRAVEDAD);
    printf("Suma de a + b = %d\n\n", suma);

    // 4. Entrada de datos por teclado (scanf)
    int anio_nacimiento;
    printf("Ingresa tu ano de nacimiento: ");
    scanf("%d", &anio_nacimiento); // El operador & indica la dirección de memoria de la variable

    printf("Naciste en el ano: %d\n\n", anio_nacimiento);

    // 5. Estructura de control condicional (if-else)
    if (edad >= 18) {
        printf("Eres mayor de edad.\n");
    } else {
        printf("Eres menor de edad.\n");
    }

    // 6. Estructura de control repetitiva (Bucle for)
    printf("\nContando del 1 al 3:\n");
    for (int i = 1; i <= 3; i++) {
        printf("Numero %d\n", i);
    }

    return 0; // Indica que el programa terminó correctamente
}
