from enum import Enum, auto

# 1. Define possible states and events using Enums
class State(Enum):
    CLOSED = auto()
    OPEN = auto()
    LOCKED = auto()

class Event(Enum):
    OPEN_DOOR = auto()
    CLOSE_DOOR = auto()
    LOCK_DOOR = auto()
    UNLOCK_DOOR = auto()

class Door:
    def __init__(self):
        self.current_state = State.CLOSED
        print(f"Initial State: {self.current_state.name}")

    def handle(self, event):
        # 2. Logic using a simple if/elif structure (similar to switch-case)
        if self.current_state == State.CLOSED:
            if event == Event.OPEN_DOOR:
                print("Opening the door...")
                self.current_state = State.OPEN
            elif event == Event.LOCK_DOOR:
                print("Locking the door...")
                self.current_state = State.LOCKED
            else:
                print(f"Error: Cannot perform {event.name} while CLOSED.")

        elif self.current_state == State.OPEN:
            if event == Event.CLOSE_DOOR:
                print("Closing the door...")
                self.current_state = State.CLOSED
            else:
                print(f"Error: Cannot perform {event.name} while OPEN.")

        elif self.current_state == State.LOCKED:
            if event == Event.UNLOCK_DOOR:
                print("Unlocking the door...")
                self.current_state = State.CLOSED
            else:
                print(f"Error: The door is LOCKED. Must unlock first.")

        print(f"--> Current State: {self.current_state.name}\n")

# --- Simulation ---
if __name__ == "__main__":
    door = Door()
    
    door.handle(Event.OPEN_DOOR)   # Open the door
    door.handle(Event.CLOSE_DOOR)  # Close it
    door.handle(Event.LOCK_DOOR)   # Lock it
    door.handle(Event.OPEN_DOOR)   # Error: It's locked!
    door.handle(Event.UNLOCK_DOOR) # Unlock it
    door.handle(Event.OPEN_DOOR)   # Now it opens!