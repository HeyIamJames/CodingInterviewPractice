"""
Generate all permutations of a given string.
P(n,k) = n! / (n-k)!
"""

#for len of str, rotate and return each permutation


def permutate(string):
    if len(str) == 1:
        return str
    perms = permutate(string[1:])
    char = string[0]
    result = []
    for i in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i]) + char + perm
