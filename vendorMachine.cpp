#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <string>
#include <map>
#include <sstream>
#include <cstring> // Necesario para memset

// --- Clase VendingMachine ---
class VendingMachine {
public:
    double balance = 0.0;
    std::string state = "IDLE";
    std::map<std::string, double> prices = {
        {"soda", 1.25}, 
        {"chips", 0.75}, 
        {"candy", 1.00}
    };

    std::string process_command(std::string cmd) {
        std::stringstream ss(cmd);
        std::string action, value;
        ss >> action >> value;

        if (action == "INSERT") {
            try {
                double coin = std::stod(value);
                if (coin == 0.25 || coin == 0.10 || coin == 0.05) {
                    balance += coin;
                    state = "ACCEPTING";
                    return "OK. Saldo: $" + std::to_string(balance);
                }
                return "ERROR: Moneda no aceptada (usa 0.25, 0.10, 0.05)";
            } catch (...) {
                return "ERROR: Valor de moneda invalido";
            }
        } 
        
        if (action == "BUY") {
            if (prices.count(value)) {
                double price = prices[value];
                if (balance >= price) {
                    balance -= price;
                    return "DESPACHANDO " + value + ". Cambio: $" + std::to_string(balance);
                }
                return "ERROR: Saldo insuficiente ($" + std::to_string(price) + " necesario)";
            }
            return "ERROR: Producto no existe";
        }

        return "COMANDOS: INSERT [valor] | BUY [producto]";
    }
};

// --- Función Principal ---
int main() {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    
    sockaddr_in addr;
    std::memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY;
    addr.sin_port = htons(8080);

    bind(server_fd, (struct sockaddr*)&addr, sizeof(addr));
    listen(server_fd, 5);

    VendingMachine machine;
    std::cout << "--- Servidor PERSISTENTE Iniciado ---" << std::endl;

    while (true) {
        int client_sock = accept(server_fd, nullptr, nullptr);
        std::cout << "[INFO] Cliente conectado. Manteniendo sesión abierta..." << std::endl;

        // BUCLE DE PERSISTENCIA
        while (true) {
            char buffer[1024] = {0};
            ssize_t bytes_read = read(client_sock, buffer, 1024);

            // Si read devuelve 0 o menos, el cliente cerró la conexión
            if (bytes_read <= 0) {
                std::cout << "[INFO] Cliente desconectado." << std::endl;
                break; 
            }

            std::string command(buffer);
            // Limpiar saltos de línea molestos de la terminal
            command.erase(command.find_last_not_of(" \n\r\t") + 1);

            if (command == "EXIT") {
                send(client_sock, "Adiós!\n", 7, 0);
                break;
            }

            std::string response = machine.process_command(command) + "\n";
            send(client_sock, response.c_str(), response.length(), 0);
        }

        close(client_sock); // Ahora solo cerramos cuando el cliente se va
    }

    close(server_fd);
    return 0;
}
