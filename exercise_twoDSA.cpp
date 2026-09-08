#include <iostream>

// Definición del nodo del árbol
struct Nodo {
    int dato;
    Nodo* izquierdo;
    Nodo* derecho;

    Nodo(int valor) {
        dato = valor;
        izquierdo = nullptr;
        derecho = nullptr;
    }
};

// Función para insertar un nuevo valor en el árbol
Nodo* insertar(Nodo* raiz, int valor) {
    if (raiz == nullptr) {
        return new Nodo(valor);
    }

    if (valor < raiz->dato) {
        raiz->izquierdo = insertar(raiz->izquierdo, valor);
    } else if (valor > raiz->dato) {
        raiz->derecho = insertar(raiz->derecho, valor);
    }

    return raiz;
}

// Recorrido In-Order (Izquierda, Raíz, Derecha) - Muestra los datos ordenados
void inOrder(Nodo* raiz) {
    if (raiz == nullptr) return;
    inOrder(raiz->izquierdo);
    std::cout << raiz->dato << " ";
    inOrder(raiz->derecho);
}

// Recorrido Pre-Order (Raíz, Izquierda, Derecha)
void preOrder(Nodo* raiz) {
    if (raiz == nullptr) return;
    std::cout << raiz->dato << " ";
    preOrder(raiz->izquierdo);
    preOrder(raiz->derecho);
}

// Recorrido Post-Order (Izquierda, Derecha, Raíz)
void postOrder(Nodo* raiz) {
    if (raiz == nullptr) return;
    postOrder(raiz->izquierdo);
    postOrder(raiz->derecho);
    std::cout << raiz->dato << " ";
}

int main() {
    Nodo* raiz = nullptr;

    // Insertar elementos de prueba
    raiz = insertar(raiz, 50);
    insertar(raiz, 30);
    insertar(raiz, 20);
    insertar(raiz, 40);
    insertar(raiz, 70);
    insertar(raiz, 60);
    insertar(raiz, 80);

    std::cout << "Recorrido In-Order (Ordenado): ";
    inOrder(raiz);
    std::cout << "\n";

    std::cout << "Recorrido Pre-Order: ";
    preOrder(raiz);
    std::cout << "\n";

    std::cout << "Recorrido Post-Order: ";
    postOrder(raiz);
    std::cout << "\n";

    return 0;
}
