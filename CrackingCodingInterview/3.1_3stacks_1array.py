"""
Create an array utalizing 3 stacks.
"""

#make an array class with attribues of size and number of stacks
#implement stack functions of push pop on each stack

# Psudo Code:
#   Class:
#     -stacksize
#     -stack#
#     -array = sizestack X stack#s
#     -pointer based on stack#
    
#   ClassMethods:
  
#   Push:
#     -point at end of stack in array and add self
#     -increment pointer/stackszie
    
#   Pop:
#     -point at end of stack in array and remove self
#     -decrement pointer/stackszie

class ArrayOfStacks(object):

    def __init__(self, stacksize = 100, number = 3):
        self.stacksize = stacksize
        self.number = number
        self.array = [None] * self.stacksize * self.number
        self.pointer = [-1] * self.number

    def push(self, stacknumber, value):
        if self.pointer[stacknumber] + 1 >= self.stacksize:
            print "Full Stack."
        else:
            self.pointer[stacknumber] += 1
            self.array[self.stacktop(stacknumber)] = value

    def pop(self, stacknumber):
        if self.pointer[stacknumber] < 0:
            return "Empty Stack."
        else:
            data = self.array[self.stacktop(stacknumber)]
            self.array[self.stacktop(stacknumber)] = None
            self.pointer[stacknumber] -= 1
            return data
