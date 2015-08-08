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



def run(stairs):
    for steps in stairs:
