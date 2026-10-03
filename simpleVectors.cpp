#include <iostream>
#include <vector> // Elemento crucial: ¡No olvides incluir esta librería!

int main() {
    // 1. DECLARACIÓN E INICIALIZACIÓN
    // Creamos un vector de números enteros vacío
    std::vector<int> numeros;

    // También puedes inicializarlo con valores desde el principio:
    // std::vector<int> numeros = {10, 20, 30};

    std::cout << "--- 1. Agregar Elementos ---" << std::endl;

    // 2. AGREGAR ELEMENTOS (push_back)
    // El método push_back añade elementos al FINAL del vector
    numeros.push_back(10);
    numeros.push_back(20);
    numeros.push_back(30);
    numeros.push_back(40);

    // 3. TAMAÑO DEL VECTOR (size)
    // .size() nos dice cuántos elementos tiene el vector actualmente
    std::cout << "El tamano del vector es: " << numeros.size() << std::endl;


    std::cout << "\n--- 2. Acceder a los Elementos ---" << std::endl;

    // 4. ACCEDER A ELEMENTOS (Por índice o con .at())
    // Al igual que los arreglos tradicionales, el conteo empieza en 0
    std::cout << "Primer elemento (indice 0): " << numeros[0] << std::endl;
    std::cout << "Segundo elemento (indice 1): " << numeros.at(1) << std::endl; 
    // Nota: .at(1) es más seguro que numeros[1] porque avisa si intentas acceder a un índice que no existe.


    std::cout << "\n--- 3. Recorrer el Vector (Bucles) ---" << std::endl;

    // 5. RECORRER EL VECTOR
    // Opción A: Usando un bucle FOR tradicional (basado en el tamaño)
    std::cout << "Bucle tradicional: ";
    for (size_t i = 0; i < numeros.size(); i++) {
        std::cout << numeros[i] << " ";
    }
    std::cout << std::endl;

    // Opción B: Usando el bucle FOR "Range-based" (Forma moderna y limpia de C++)
    std::cout << "Bucle moderno (Range-based): ";
    for (int n : numeros) {
        std::cout << n << " ";
    }
    std::cout << std::endl;


    std::cout << "\n--- 4. Eliminar Elementos ---" << std::endl;

    // 6. ELIMINAR ELEMENTOS (pop_back)
    // Elimina el ÚLTIMO elemento del vector (en este caso, el 40)
    numeros.pop_back();

    std::cout << "Despues de usar pop_back(), el ultimo elemento desaparece." << std::endl;
    std::cout << "Nuevo tamano: " << numeros.size() << std::endl;
    std::cout << "Elementos restantes: ";
    for (int n : numeros) {
        std::cout << n << " ";
    }
    std::cout << std::endl;


    std::cout << "\n--- 5. Limpiar el Vector ---" << std::endl;

    // 7. LIMPIAR TODO EL VECTOR (clear)
    // Borra absolutamente todos los elementos y lo deja vacío (tamaño 0)
    numeros.clear();

    // 8. VERIFICAR SI ESTÁ VACÍO (empty)
    // .empty() devuelve true (1) si está vacío o false (0) si tiene algo
    if (numeros.empty()) {
        std::cout << "El vector ahora esta completamente vacio." << std::endl;
    }

    return 0;
}
