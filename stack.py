

''' What is a Stack?

A stack is a linear data structure that follows the rule:
👉 LIFO (Last In, First Out)

Think of a stack of plates:

You add (push) plates on top.

You remove (pop) only from the top. '''

'''Stack Operations

Push → Add element to the top.

Pop → Remove element from the top.

Peek / Top → View the top element without removing.

isEmpty → Check if stack is empty.

Size → Number of elements. '''


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top:", s.peek())     # 30
print("Popped:", s.pop())   # 30
print("Is empty?", s.is_empty())
