#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

// Definimos un tipo para representar una arista (destino, peso)
typedef pair<int, int> Arista;

// Función principal de Dijkstra
void dijkstra(int origen, int n, const vector<vector<Arista>>& grafo) {
    // Vector para almacenar la distancia más corta desde el origen
    vector<int> dist(n, INT_MAX);
    
    // Cola de prioridad min-heap (guarda pares de {distancia, nodo})
    priority_queue<Arista, vector<Arista>, greater<Arista>> pq;

    // Inicializamos el nodo de origen
    dist[origen] = 0;
    pq.push({0, origen});

    while (!pq.empty()) {
        int d = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        // Si la distancia en la cola es mayor a la registrada, la ignoramos
        if (d > dist[u]) continue;

        // Recorremos todos los vecinos del nodo actual
        for (auto& arista : grafo[u]) {
            int v = arista.first;      // Nodo vecino
            int peso = arista.second;  // Peso de la arista

            // Relajación de la arista
            if (dist[u] + peso < dist[v]) {
                dist[v] = dist[u] + peso;
                pq.push({dist[v], v});
            }
        }
    }

    // Mostramos las distancias mínimas desde el origen
    cout << "Distancias desde el nodo " << origen << ":\n";
    for (int i = 0; i < n; i++) {
        cout << "Nodo " << i << " : ";
        if (dist[i] == INT_MAX) cout << "Inalcanzable\n";
        else cout << dist[i] << "\n";
    }
}

int main() {
    int n = 5; // Número de nodos (del 0 al 4)
    vector<vector<Arista>> grafo(n);

    // Agregamos las conexiones (grafo no dirigido)
    // grafo[u].push_back({v, peso});
    grafo[0].push_back({1, 4});
    grafo[0].push_back({2, 1});
    grafo[2].push_back({1, 2});
    grafo[2].push_back({3, 5});
    grafo[1].push_back({3, 1});
    grafo[3].push_back({4, 1});

    dijkstra(0, n, grafo);

    return 0;
}
