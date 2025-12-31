#include <iostream>

using namespace std;

// 1. Define possible states
enum class State {
    CLOSED,
    OPEN
};

// 2. Define possible events (actions)
enum class Event {
    OPEN_DOOR,
    CLOSE_DOOR
};

class Door {
private:
    State currentState = State::CLOSED; // Initial state

public:
    void handle(Event event) {
        switch (currentState) {
            case State::CLOSED:
                if (event == Event::OPEN_DOOR) {
                    cout << "Opening the door..." << endl;
                    currentState = State::OPEN;
                } else {
                    cout << "Error: The door is already closed." << endl;
                }
                break;

            case State::OPEN:
                if (event == Event::CLOSE_DOOR) {
                    cout << "Closing the door..." << endl;
                    currentState = State::CLOSED;
                } else {
                    cout << "Error: The door is already open." << endl;
                }
                break;
        }
    }
};

int main() {
    Door door;

    cout << "--- Starting Simulation ---" << endl;

    door.handle(Event::OPEN_DOOR);  // Success: Closed -> Open
    door.handle(Event::CLOSE_DOOR); // Success: Open -> Closed
    door.handle(Event::CLOSE_DOOR); // Error: Already closed
    door.handle(Event::OPEN_DOOR);  // Success: Closed -> Open

    return 0;
}