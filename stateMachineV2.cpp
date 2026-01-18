#include <iostream>
#include <memory>
#include <string>

// Declaración adelantada
class Context;

// 1. Interfaz Base State
class State {
protected:
    Context* context_;
public:
    virtual ~State() = default;
    void set_context(Context* context) { context_ = context; }
    virtual void handle1() = 0;
    virtual void handle2() = 0;
};

// 2. Clase Contexto (Usa smart pointers para evitar fugas de memoria)
class Context {
private:
    std::unique_ptr<State> state_;
public:
    Context(std::unique_ptr<State> state) { transition_to(std::move(state)); }

    void transition_to(std::unique_ptr<State> state) {
        std::cout << "Contexto: Cambiando de estado...\n";
        state_ = std::move(state);
        state_->set_context(this);
    }

    void request1() { state_->handle1(); }
    void request2() { state_->handle2(); }
};

// 3. Estados Concretos
class ConcreteStateB : public State {
public:
    void handle1() override { std::cout << "Estado B maneja peticion 1.\n"; }
    void handle2() override; // Se define abajo para evitar problemas de dependencia circular
};

class ConcreteStateA : public State {
public:
    void handle1() override {
        std::cout << "Estado A cambia a B.\n";
        context_->transition_to(std::unique_ptr<State>(new ConcreteStateB()));
    }
    void handle2() override { std::cout << "Estado A maneja peticion 2.\n"; }
};

// Definición tardía de B para que conozca a A
void ConcreteStateB::handle2() {
    std::cout << "Estado B cambia a A.\n";
    context_->transition_to(std::unique_ptr<State>(new ConcreteStateA()));
}

// 4. Código del Cliente
int main() {
    // Usamos make_unique para mayor seguridad
    auto context = std::unique_ptr<Context>(new Context(std::unique_ptr<State>(new ConcreteStateA())));
    
    context->request1(); // Cambiará A -> B
    context->request2(); // Cambiará B -> A

    return 0;
}