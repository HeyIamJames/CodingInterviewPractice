"""
Find the first non-repeated (unique) character in a given string.
"""

def counts(string):
    count = [256]
    for i in string:
        count[ord(i)]+=1
    return count
    
def unique(string):
    count = counts(string)
    index = -1
    k = 0
 
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
 
    return index
