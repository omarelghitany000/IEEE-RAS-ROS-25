class Stack:
    def __init__(self):
        self.items = []

    def push(self,items):
        self.items.append(items)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return ("the stack is empty")
        
    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements:", self.items)


my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.display()
print("Popped:", my_stack.pop())
my_stack.display()
