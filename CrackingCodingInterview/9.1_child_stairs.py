"""
A child is running up a staircase with n steps,
and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the
child can run up the stairs.
"""

# psudo code:
# try dividing staris by largest num, 3, for the modulos, try it against 2, then 1
# then try entre set against 2, using above method, then call entire set agins 1, which would always be 1
# if there is no remainder, dont call again for same subset

# more psudo code:
# if steps was 8
# intialize a counter = 0
# 8 % 3 = 2, counter += 1
# 2 % 2 = 0, counter += 2 > I add 2 because there is no point checking against 1

# call recusiveley on 2
# 8 % 2 = 0, counter += 2

# sum the counters:
# 1 + 2 + 2 = 5

#number of permutations
def run(stairs, step_range=3):
    if not stairs:
        return 1
    elif stairs < 0:
        return 0
    else:
        total = 0
        for n in xrange(1, min(stairs, step_range) + 1):
            total += run(stairs - n, step_range=step_range)
        return total

#extend for 3
def fibR(n):
    if n == 1 or n == 2:
        return 1
    return fibR(n - 1) + fibR(n - 2)
