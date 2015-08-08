"""
A child is running up a staircase with n steps,
and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the
child can run up the stairs.
"""

# psudo code:
# try dividing staris by largest num, 3, for the modulos, try it against 2, then 1
# then try entre set against 2, using above method, then call entire set agins 1, which would always be 1


def run(stairs):
    for steps in stairs:
