"""
Write a program to sort a stack in ascending order,
(with biggest items on top). You may use at most one
additional stack to hold items, but you may not copy
the elements into any other data structure (such as
    an array). The stack supports the following operations:
push, pop, peek, and isEmpty.
"""


class Stack(list):

    def peak(self):
        return self[-1]

    def push(self, item):
        self.append(item)

    def empty(self):
        return len(self) == 0

    def sort_stack(self):
        x = Stack()
        while not self.empty():
            tmp = self.pop()
            while not x.empty() and x.peak() > tmp:
                self.push(x.pop())
            x.push(tmp)
            while not self.empty() and self.peak() >= x.peak():
                x.push(self.pop())
        return x
