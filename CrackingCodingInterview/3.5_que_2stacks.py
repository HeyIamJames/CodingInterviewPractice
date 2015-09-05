class MyQueue(object):
    def __init__(self):
        self.front_stack = Stack()
        self.back_stack = Stack()

    def eq(self, data):
        self.back_stack.push(data)

    def dq(self):
        if self.front_stack.size == 0:
            self.rebuild()
        return self.front_stack.pop()

    def peek_front(self):
        if self.front_stack.size == 0:
            self.rebuild()
        return self.front_stack.peek()
    
    def rebuild(self):
        """
        Lazily rebuilds the front stack when a value is needed by pop/peek.
        When the front_stack empties, rebuild it by reversing the values in
        the back_stack.
        """
        while self.back_stack.size > 0:
            self.front_stack.push(self.back_stack.pop())
  
