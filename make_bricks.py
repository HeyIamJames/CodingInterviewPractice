"""
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) 
and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.
"""

#recursive 
def make_bricks(small, big, goal):
    if (small + big * 5 )< goal:
        return False
    if (small + big * 5) == goal:
        return True
    return make_bricks(small-1, big, goal) or make_bricks(small, big-1, goal)
