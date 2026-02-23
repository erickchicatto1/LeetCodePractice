#include <iostream>
#include <vector>
#include <tuple>
#include <unordered_map>

using namespace std;

vector<pair<string, int>> transactionOperations(
    const vector<tuple<int, string, int>>& transactions) {
    
    unordered_map<string, int> totals;  // mapa para acumular montos por usuario

    for (const auto& transaction : transactions) {
        int id;
        string user;
        int amount;

        tie(id, user, amount) = transaction;

        cout << id << " " << user << " " << amount << endl;

        // Acumular montos por usuario
        totals[user] += amount;  
        // En unordered_map, si la clave no existe, se inicializa automáticamente en 0
    }

    // Convertir el mapa a vector de pares
    vector<pair<string, int>> result;
    for (const auto& entry : totals) {
        result.push_back(entry);
    }

    return result;
}

int main() {
    vector<tuple<int, string, int>> transactions = {
        {1, "user1", 150},
        {2, "user3", 100},
        {3, "user2", 150},
        {4, "user1", 200},
        {2, "user2", 100}
    };

    vector<pair<string, int>> totals_list = transactionOperations(transactions);

    cout << "\nTotales por usuario:\n";
    for (const auto& entry : totals_list) {
        cout << entry.first << " -> " << entry.second << endl;
    }

    return 0;
}
