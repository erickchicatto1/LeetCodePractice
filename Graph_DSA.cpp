#include <iostream>
#include <vector>
using namespace std;

class Graph {
private:
    int vertices;
    vector<vector<int>> adjList;

public:
    // Constructor
    Graph(int v) {
        vertices = v;
        adjList.resize(v);
    }

    // Agregar una arista
    void addEdge(int u, int v) {
        adjList[u].push_back(v);
        adjList[v].push_back(u); // porque es no dirigido
    }

    // Mostrar el grafo
    void printGraph() {
        for (int i = 0; i < vertices; i++) {
            cout << "Vertice " << i << ": ";
            for (int neighbor : adjList[i]) {
                cout << neighbor << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    Graph g(5);

    g.addEdge(0, 1);
    g.addEdge(0, 4);
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(3, 4);

    g.printGraph();

    return 0;
}
