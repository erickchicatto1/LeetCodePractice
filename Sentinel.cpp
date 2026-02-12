#include <iostream>
#include <string>
#include <ctime>
#include <fcntl.h>
#include <termios.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <cstring>

class SentinelDriver {
private:
    int uart_fd;
    int server_fd;
    std::string phoneNumber;
    int port;

    // --- Métodos Privados de Utilidad ---
    
    void sendAT(const std::string& cmd, int wait_ms = 1000) {
        if (uart_fd == -1) return;
        tcflush(uart_fd, TCIOFLUSH);
        std::string full_cmd = cmd + "\r\n";
        write(uart_fd, full_cmd.c_str(), full_cmd.length());
        usleep(wait_ms * 1000);
    }

public:
    SentinelDriver(std::string device, std::string phone, int listenPort) 
        : phoneNumber(phone), port(listenPort) {
        
        // Inicializar Serial
        uart_fd = open(device.c_str(), O_RDWR | O_NOCTTY);
        if (uart_fd == -1) perror("Error al abrir puerto serial");

        // Inicializar Socket
        server_fd = socket(AF_INET, SOCK_STREAM, 0);
        int opt = 1;
        setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

        struct sockaddr_in address;
        address.sin_family = AF_INET;
        address.sin_addr.s_addr = INADDR_ANY;
        address.sin_port = htons(port);

        bind(server_fd, (struct sockaddr *)&address, sizeof(address));
        listen(server_fd, 5);
    }

    // 1. Lógica de Tiempo: Determina el modo (1: Armas, 2: Personas)
    int getSecurityMode() {
        time_t t = time(0);
        tm* ahora = localtime(&t);
        int h = ahora->tm_hour;
        // Modo Armas: 09:00 a 21:59 (9 AM - 10 PM)
        return (h >= 9 && h < 22) ? 1 : 2;
    }

    // 2. Lógica de Hardware: SMS y Llamada
    void triggerHardwareAlert(const char* msg) {
        std::cout << "[HARDWARE] Ejecutando protocolo de alerta: " << msg << std::endl;
        
        // Enviar SMS
        sendAT("AT+CMGF=1");
        sendAT("AT+CMGS=\"" + phoneNumber + "\"", 500);
        write(uart_fd, msg, strlen(msg));
        char ctrl_z[1] = {26};
        write(uart_fd, ctrl_z, 1);
        sleep(3);

        // Llamada rápida
        sendAT("ATD" + phoneNumber + ";", 1000);
        sleep(5);
        sendAT("ATH");
    }

    // 3. Bucle Principal: Escuchar a Python
    void run() {
        std::cout << "DRIVER: Sistema Sentinel activo en puerto " << port << "..." << std::endl;
        struct sockaddr_in address;
        int addrlen = sizeof(address);

        while(true) {
            int new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen);
            char buffer[1024] = {0};
            read(new_socket, buffer, 1024);

            if (strcmp(buffer, "GET_MODE") == 0) {
                // Responder el modo actual a Python
                std::string mode = std::to_string(getSecurityMode());
                send(new_socket, mode.c_str(), mode.length(), 0);
            } else if (strlen(buffer) > 0) {
                // Si no es un comando, es un mensaje de alerta de IA
                triggerHardwareAlert(buffer);
            }
            close(new_socket);
        }
    }

    ~SentinelDriver() {
        if (uart_fd != -1) close(uart_fd);
        if (server_fd != -1) close(server_fd);
    }
};
