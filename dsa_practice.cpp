#include <iostream>
#include <stdexcept>

using namespace std;

// ==========================================
// 1. NODO BASE (Para la Lista Enlazada)
// ==========================================
struct Node {
    int data;
    Node* next;
    
    Node(int value) {
        data = value;
        next = nullptr;
    }
};

// ==========================================
// 2. LISTA ENLAZADA SIMPLE (Singly Linked List)
// ==========================================
class LinkedList {
private:
    Node* head;

public:
    LinkedList() : head(nullptr) {}

    // Insertar al inicio
    void insertAtHead(int val) {
        Node* newNode = new Node(val);
        newNode->next = head;
        head = newNode;
    }

    // Insertar al final
    void insertAtTail(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr) {
            head = newNode;
            return;
        }
        Node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
    }

    // Mostrar la lista
    void display() {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << " -> ";
            temp = temp->next;
        }
        cout << "NULL" << endl;
    }

    // Destructor para liberar memoria
    ~LinkedList() {
        Node* temp = head;
        while (temp != nullptr) {
            Node* nextNode = temp->next;
            delete temp;
            temp = nextNode;
        }
    }
};

// ==========================================
// 3. PILA (Stack - LIFO: Last In, First Out)
// ==========================================
class Stack {
private:
    Node* top;

public:
    Stack() : top(nullptr) {}

    // Empujar elemento (Push)
    void push(int val) {
        Node* newNode = new Node(val);
        newNode->next = top;
        top = newNode;
    }

    // Sacar elemento (Pop)
    void pop() {
        if (isEmpty()) {
            cout << "Pila vacía. No se puede hacer pop.\n";
            return;
        }
        Node* temp = top;
        top = top->next;
        delete temp;
    }

    // Obtener el elemento superior (Peek)
    int peek() {
        if (isEmpty()) {
            throw runtime_error("Pila vacía.");
        }
        return top->data;
    }

    bool isEmpty() {
        return top == nullptr;
    }

    ~Stack() {
        while (!isEmpty()) {
            pop();
        }
    }
};

// ==========================================
// 4. FUNCIÓN PRINCIPAL (Pruebas)
// ==========================================
int main() {
    // --- Prueba de Lista Enlazada ---
    cout << "--- PRUEBA DE LISTA ENLAZADA ---" << endl;
    LinkedList lista;
    lista.insertAtHead(10);
    lista.insertAtHead(5);
    lista.insertAtTail(20);
    cout << "Contenido de la lista: ";
    lista.display(); // Debe mostrar: 5 -> 10 -> 20 -> NULL
    cout << endl;

    // --- Prueba de Pila (Stack) ---
    cout << "--- PRUEBA DE PILA (STACK) ---" << endl;
    Stack pila;
    pila.push(100);
    pila.push(200);
    pila.push(300);

    cout << "Elemento en la cima: " << pila.peek() << endl; // Debe ser 300
    pila.pop();
    cout << "Elemento en la cima tras un pop: " << pila.peek() << endl; // Debe ser 200

    return 0;
}
