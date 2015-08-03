"""
The rules of the game are very simple, but the solution is not so obvious. The game "Towers of Hanoi" uses three rods. A number of disks is stacked in decreasing order from the bottom to the top of one rod, i.e. the largest disk at the bottom and the smallest one on top. The disks build a conical tower. 

The aim of the game is to move the tower of disks from one rod to another rod. 

The following rules have to be obeyed:
Only one disk may be moved at a time.
Only the most upper disk from one of the rods can be moved in a move
It can be put on another rod, if this rod is empty or if the most upper disk of this rod is larger than the one which is moved.
"""


def hanoi(n, source, buffer, target):
    if n > 0:
        # move tower of size n - 1 to buffer:
        hanoi(n - 1, source, target, buffer)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from buffer to target
        hanoi(n - 1, buffer, source, target)

source = [4, 3, 2, 1]
target = []
buffer = []
hanoi(len(source), source, buffer, target)

print source, buffer, target
