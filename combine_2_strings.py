"""
We are given 3 strings: str1, str2, and str3.
Str3 is said to be a shuffle of str1 and str2
if it can be formed by interleaving the characters
of str1 and str2 in a way that maintains the left to
right ordering of the characters from each string.
http://www.ardendertat.com/2011/10/10/programming-interview-questions-6-combine-two-strings/
"""

"""
check if len str3 is = len str1 + str 2
check if start of str 1 or 2 = start of 3
either false = false
if and only if 

or.. check all odd / indexs of str 1 in 3
based on that check all indexes of str 2 in 3

"""

#slow solution
def isShuffle(str1, str2, str3):
    if len(str3) != len(str1 + str2):
        return False
    x = len(str3)
    odd = []
    for i in range(x):
        if i % 2 == 1:
            odd.append(i)
    even = []
    for i in range(x):
        if i % 2 == 0:
            even.append(i)


    elif 