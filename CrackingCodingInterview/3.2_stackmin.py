"""
stack with pop, push, min
opperate in O(1)
"""
class StackMin:
    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, value):
        self.stack.append(value)
        if len(self.min) == 0 or value <= self.min[-1]:
            self.min.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        data = self.stack.pop()
        if data == self.min[-1]:
            self.min.pop()
        return data

    def get_min(self):
        if len(self.min)==0:
            return None
        return self.min[-1]
