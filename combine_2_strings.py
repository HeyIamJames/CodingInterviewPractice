"""
We are given 3 strings: str1, str2, and str3.
Str3 is said to be a shuffle of str1 and str2
if it can be formed by interleaving the characters
of str1 and str2 in a way that maintains the left to
right ordering of the characters from each string.
http://www.ardendertat.com/2011/10/10/programming-interview-questions-6-combine-two-strings/
"""


def isShuffle(str1, str2, str3):
    