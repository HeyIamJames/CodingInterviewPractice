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
check all odd / indexs of str 1 in 3
based on that check all indexes of str 2 in 3
then if not try other other way

"""

def isShuffle(str1, str2, str3):
    if len(str3) != len(str1 + str2):
        return False
    if str1 == str3[0::2] and str2 == str3[1::2]:
        return True
    if str2 == str3[0::2] and str1 == str3[1::2]:
        return True
    else:
        return False
#fail
str1 = "the apple"
str2 = "pears"
str3 = "james hemmaplardh"

#pass
str1 = "apple"
str2 = "pears"
str3 = "appepalres"
