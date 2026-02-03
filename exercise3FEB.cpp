#include <iostream>
#include <vector>

using namespace std;

/*
 * La función recibe dos vectores de enteros (a y b)
 * y devuelve un vector con los dos puntajes.
 */
vector<int> compareTriplets(vector<int> a, vector<int> b) {
    int scoreAlice = 0;
    int scoreBob = 0;

    // En C++ no existe 'zip' de forma nativa como en Python,
    // pero como sabemos que ambos arreglos tienen el mismo tamaño (3),
    // usamos un ciclo for tradicional con el índice.
    for (int i = 0; i < a.size(); i++) {
        if (a[i] > b[i]) {
            scoreAlice++;
        } else if (a[i] < b[i]) {
            scoreBob++;
        }
    }

    // Retornamos un vector con los dos resultados
    return {scoreAlice, scoreBob};
}

int main() {
    vector<int> a(3);
    vector<int> b(3);

    // Leer los valores de Alice
    for (int i = 0; i < 3; i++) {
        cin >> a[i];
    }

    // Leer los valores de Bob
    for (int i = 0; i < 3; i++) {
        cin >> b[i];
    }

    vector<int> result = compareTriplets(a, b);

    // Imprimir el resultado separado por un espacio
    cout << result[0] << " " << result[1] << endl;

    return 0;
}