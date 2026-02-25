#include <iostream>
#include <stdexcept>

// Definición de los estados posibles del jugador
enum class HealthState {
    PlayerAlive,
    PlayerDead,
    GameOver
};

// Definición de los eventos que pueden ocurrir
enum class Event {
    HitByMonster,
    Heal,
    Restart
};

class GameStateMachine {
public:
    void startGame(unsigned int health, unsigned int lives) {
        state_ = HealthState::PlayerAlive;
        currentHealth_ = health;
        remainingLives_ = lives;
        std::cout << "Juego iniciado. Vida: " << currentHealth_ << " Vidas: " << remainingLives_ << "\n";
    }

    void processEvent(Event evt, unsigned int param) {
        switch (evt) {
            case Event::HitByMonster:
                state_ = onHitByMonster(param);
                break;
            case Event::Heal:
                state_ = onHeal(param);
                break;
            case Event::Restart:
                state_ = onRestart(param);
                break;
            default:
                throw std::logic_error("Transición de estado no soportada");
        }
    }

    // Getter para saber el estado actual (opcional pero útil)
    HealthState getState() const { return state_; }

private:
    HealthState state_;
    unsigned int currentHealth_{ 0 };
    unsigned int remainingLives_{ 0 };

    // --- Lógica de transiciones ---

    HealthState onHitByMonster(unsigned int damage) {
        if (state_ == HealthState::GameOver) return state_;

        if (damage >= currentHealth_) {
            currentHealth_ = 0;
            if (remainingLives_ > 0) {
                remainingLives_--;
                std::cout << "¡Moriste! Vidas restantes: " << remainingLives_ << "\n";
                return HealthState::PlayerDead;
            } else {
                std::cout << "GAME OVER\n";
                return HealthState::GameOver;
            }
        }
        
        currentHealth_ -= damage;
        std::cout << "Golpe recibido. Vida restante: " << currentHealth_ << "\n";
        return HealthState::PlayerAlive;
    }

    HealthState onHeal(unsigned int recovery) {
        if (state_ == HealthState::PlayerAlive) {
            currentHealth_ += recovery;
            std::cout << "Curado. Vida actual: " << currentHealth_ << "\n";
        }
        return state_;
    }

    HealthState onRestart(unsigned int initialHealth) {
        std::cout << "Reiniciando...\n";
        currentHealth_ = initialHealth;
        return HealthState::PlayerAlive;
    }
};
