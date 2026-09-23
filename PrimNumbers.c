#include <stdio.h>

// Función para verificar si un número es primo
int esPrimo(int num) {
    if (num <= 1) {
        return 0; // El 0 y el 1 no son primos
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return 0; // Si es divisible, no es primo
        }
    }
    return 1; // Si pasó el ciclo, es primo
}

int main() {
    int numero;
    
    printf("Introduce un número: ");
    scanf("%d", &numero);
    
    if (esPrimo(numero)) {
        printf("%d es un número primo.\n", numero);
    } else {
        printf("%d no es un número primo.\n", numero);
    }
    
    return 0;
}
