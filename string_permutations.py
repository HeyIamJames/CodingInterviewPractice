"""
Generate all permutations of a given string.
P(n,k) = n! / (n-k)!
http://www.ardendertat.com/2011/10/28/programming-interview-questions-11-all-permutations-of-string/
"""

#for len of str, rotate and return each permutation


def permutate(string):


#string = james, expected = ['james', 'ajmes', 'amjes', 'amejs', 'amesj']


#import hack

from itertools import permutations
def permutate2(string):
    return [''.join(p) for p in permutations(string)]
