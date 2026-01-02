#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// 1. Added a state for validation
enum class State {
    CLOSED,
    OPEN,
    VALIDATING
};

// 2. Added an event to trigger the check
enum class Event {
    OPEN_DOOR,
    CLOSE_DOOR,
    CHECK_NUMBER
};

class Door {
private:
    State currentState = State::CLOSED;

    // Helper function: Palindrome Logic
    bool isPalindrome(int number) {
        string str = to_string(number);
        string reversedStr = str;
        reverse(reversedStr.begin(), reversedStr.end());
        return str == reversedStr;
    }

public:
    // Overloaded handle to accept a number for the palindrome check
    void handle(Event event, int number = 0) {
        switch (currentState) {
            case State::CLOSED:
                if (event == Event::CHECK_NUMBER) {
                    cout << "Checking if " << number << " is a palindrome..." << endl;
                    
                    if (isPalindrome(number)) {
                        cout << "Success! Number is a palindrome. Access Granted." << endl;
                        currentState = State::OPEN;
                    } else {
                        cout << "Denied! " << number << " is not a palindrome. Door remains CLOSED." << endl;
                    }
                } 
                else if (event == Event::OPEN_DOOR) {
                    cout << "Error: You must provide a palindrome code to open the door." << endl;
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

    cout << "--- Starting Palindrome Door Simulation ---" << endl;

    // Try to open without code
    door.handle(Event::OPEN_DOOR);

    // Try with a non-palindrome number
    door.handle(Event::CHECK_NUMBER, 1234); 

    // Try with a palindrome number
    door.handle(Event::CHECK_NUMBER, 1221); 

    // Close the door
    door.handle(Event::CLOSE_DOOR);

    return 0;
}