#include <stdio.h> // Librería estándar para entrada y salida

// Declaración de una función simple que suma dos números
int sumar(int a, int b) {
    return a + b;
}

int main(void) {
    // 1. Variables y Tipos de Datos basicos
    int edad = 0;
    float altura = 0.0f;
    char inicial = ' ';

    // 2. Entrada y Salida de datos
    printf("--- Repaso de Conceptos Basicos en C ---\n");
    
    printf("Ingresa tu edad (numero entero): ");
    scanf("%d", &edad); // %d es el formato para enteros

    printf("Ingresa tu altura en metros (ej. 1.75): ");
    scanf("%f", &altura); // %f es el formato para flotantes

    // Limpiar el buffer antes de leer un caracter
    while(getchar() != '\n'); 

    printf("Ingresa la inicial de tu nombre: ");
    scanf("%c", &inicial); // %c es el formato para caracteres

    // 3. Mostrar los datos ingresados
    printf("\nHola, %c. Tienes %d anos y mides %.2f metros.\n", inicial, edad, altura);

    // 4. Estructuras de control (Condicional if-else)
    if (edad >= 18) {
        printf("Eres mayor de edad.\n");
    } else {
        printf("Eres menor de edad.\n");
    }

    // 5. Estructuras repetitivas (Ciclo for)
    printf("\nContando del 1 al 3 usando un ciclo for:\n");
    for (int i = 1; i <= 3; i++) {
        printf("Numero: %d\n", i);
    }

    // 6. Uso de una funcion personalizada
    int resultado = sumar(10, 5);
    printf("\nEl resultado de la funcion sumar(10, 5) es: %d\n", resultado);

    return 0; // Indica que el programa termino correctamente
}
