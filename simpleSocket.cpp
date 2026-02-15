#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
    // 1. Crear el socket (AF_INET = IPv4, SOCK_STREAM = TCP)
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1) {
        perror("Fallo en socket");
        return 1;
    }

    // 2. Configurar dirección y puerto
    sockaddr_in address;
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY; // Escuchar en todas las interfaces
    address.sin_port = htons(8080);       // Puerto 8080

    // 3. Unir el socket al puerto (Bind)
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        perror("Fallo en bind");
        return 1;
    }

    // 4. Escuchar conexiones entrantes
    listen(server_fd, 3);
    std::cout << "Servidor escuchando en el puerto 8080..." << std::endl;

    // 5. Aceptar una conexión
    int addrlen = sizeof(address);
    int new_socket = accept(server_fd, (struct sockaddr*)&address, (socklen_t*)&addrlen);
    
    // 6. Leer datos
    char buffer[1024] = {0};
    read(new_socket, buffer, 1024);
    std::cout << "Mensaje recibido: " << buffer << std::endl;

    // 7. Responder y cerrar
    const char* hello = "Hola desde el servidor";
    send(new_socket, hello, strlen(hello), 0);
    
    close(new_socket);
    close(server_fd);
    return 0;
}
