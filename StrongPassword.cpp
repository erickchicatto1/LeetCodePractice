#include <iostream>
#include <string>
#include <algorithm> // Para std::max
#include <cctype>    // Para isdigit, islower, isupper

using namespace std;

int minimumNumber(int n, string password) {
    bool has_num = false, has_low = false, has_upp = false, has_spec = false;
    
    for (char c : password) {
        if (isdigit(c)) has_num = true;
        else if (islower(c)) has_low = true;
        else if (isupper(c)) has_upp = true;
        else has_spec = true;
    }

    // Sumar booleanos en C++ convierte true en 1 y false en 0
    int types_present = has_num + has_low + has_upp + has_spec;
    int missing_types = 4 - types_present;
    
    // Debug: Ver cuántos tipos detectó
    cout << "--- Debug Info ---" << endl;
    cout << "Tipos encontrados: " << types_present << endl;
    cout << "Tipos faltantes: " << missing_types << endl;
    cout << "Faltan para longitud de 6: " << (6 - n > 0 ? 6 - n : 0) << endl;
    cout << "------------------" << endl;

    return max(missing_types, 6 - n);
}

int main() {
    int n;
    string password;

    cout << "Introduce la longitud de la contraseña: ";
    if (!(cin >> n)) return 0; // Validación simple de entrada

    cout << "Introduce la contraseña: ";
    cin >> password;

    int result = minimumNumber(n, password);

    cout << "\nCaracteres minimos a añadir: " << result << endl;

    return 0;
}