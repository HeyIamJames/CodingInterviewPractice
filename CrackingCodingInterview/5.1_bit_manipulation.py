"""
You are given two 32-bit numbers, N and M, and bit positions, i and j. 
Write a method to insert M into N such that M starts at bit j and ends at bit i.
You can assume that the bits j through i have enough space to fit all of M.
That is, if M = 10011, you can assume that there are at least 5 bits between j and i. 
You would not, for example, have j = 3 and i = 2, because M could not fully fit
between bit 3 and bit 2.
EXAMPLE:
Input: N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100
"""

def merge(n,m, i, j):
    val1  = ~0
    val1  = val1 << j 
    val2 = (1 << (i+1)) -1 
    mask = val1 | val2 
        
    ncleared = n & mask
    print bin(ncleared)
    mshifted = m << i
    print bin(mshifted)
    result = ncleared | mshifted
    return result
