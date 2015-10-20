"""
There is an array of non-negative integers.
A second array is formed by shuffling the elements of the first array and deleting a random element.
Given these two arrays, find which element is missing in the second array.
http://www.ardendertat.com/2012/01/09/programming-interview-questions/
"""

def findMissingNumber3(array1, array2):
    result=0 
    for num in array1+array2:
        result^=num 
    return result
