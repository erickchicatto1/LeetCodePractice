#include <stdio.h>

int main() {
    // Declaración e inicialización de un array de 5 enteros
    int numeros[5] = {10, 20, 30, 40, 50};
    
    // Imprimir los elementos del array usando un bucle for
    printf("Elementos del array:\n");
    for (int i = 0; i < 5; i++) {
        printf("Posición %d: %d\n", i, numeros[i]);
    }
    
    return 0;
}
