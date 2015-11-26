"""
Given a sorted array of unknown length and a number to search for,
return the index of the number in the array. Accessing an element out of bounds
throws exception. If the number occurs multiple times, return the index of any
occurrence. If it isn’t present, return -1.
http://www.ardendertat.com/2011/11/21/programming-interview-questions-17-search-unknown-length-array/#sthash.SK6PWW8B.dp
"""

def getIndex(arr, val):
    index = 0
    if arr[index] == val:
        return index
    else:
        index += 1

"""
arr = range(10, 50)
val = 15
"""