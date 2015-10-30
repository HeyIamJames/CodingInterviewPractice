"""
Generate all permutations of a given string.
P(n,k) = n! / (n-k)!
"""

#for len of str, rotate and return each permutation


def permutate(str):
    if len(str) == 1:
        return str
    perms = permutate(word[1:])
    char = word[0]
    result = []
