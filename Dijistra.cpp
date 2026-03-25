#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

typedef pair<int, int> pii; // (distancia, nodo)

class Graph {
private:
    int V; // número de nodos
    vector<vector<pii>> adj; // lista de adyacencia

public:
    Graph(int V) {
        this->V = V;
        adj.resize(V);
    }

    void addEdge(int u, int v, int weight) {
        adj[u].push_back({v, weight});
        adj[v].push_back({u, weight}); // quitar si es dirigido
    }

    void dijkstra(int start) {
        vector<int> dist(V, numeric_limits<int>::max());

        priority_queue<pii, vector<pii>, greater<pii>> pq;

        dist[start] = 0;
        pq.push({0, start});

        while (!pq.empty()) {
            int currentDist = pq.top().first;
            int u = pq.top().second;
            pq.pop();

            // Si ya encontramos una mejor distancia, ignorar
            if (currentDist > dist[u]) continue;

            for (auto& neighbor : adj[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;

                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    pq.push({dist[v], v});
                }
            }
        }

        // Imprimir resultados
        cout << "Distancias desde el nodo " << start << ":\n";
        for (int i = 0; i < V; i++) {
            cout << "Nodo " << i << " -> " << dist[i] << endl;
        }
    }
};

int main() {
    Graph g(6);

    g.addEdge(0, 1, 7);
    g.addEdge(0, 2, 9);
    g.addEdge(0, 5, 14);
    g.addEdge(1, 2, 10);
    g.addEdge(1, 3, 15);
    g.addEdge(2, 3, 11);
    g.addEdge(2, 5, 2);
    g.addEdge(3, 4, 6);
    g.addEdge(4, 5, 9);

    g.dijkstra(0);

    return 0;
}
