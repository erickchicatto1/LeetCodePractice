class History:
    def __init__(self):
        self.history_stack = []
        self.future_stack = []

    def execute_action(self, action):
        self.history_stack.append(action)
        print(f"Executing: {action}")

    def undo_action(self):
        if self.history_stack:
            self.future_stack.append(self.history_stack.pop())
            action = self.history_stack[-1] if self.history_stack else print("Nothing to undo. Initialize a new action first")
            print(f"Undid, now on action: {action}")
        else:
            print("Nothing to undo. Initialize a new action first")

    def redo_action(self):
        if self.future_stack:
            action = self.future_stack.pop()
            self.history_stack.append(action)
            print(f"Redid, now on action: {action}")
        else:
            print("Nothing to redo")

history = History()
history.undo_action()
