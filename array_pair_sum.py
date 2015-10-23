"""
Given an integer array, output all pairs that sum
up to a specific value k.
http://www.ardendertat.com/2011/09/17/programming-interview-questions-1-array-pair-sum/
"""

def pairSum(arr, k):
    if len(arr) < 2:
        return
    arr.sort()
    left, right = (0, len(arr) - 1)
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == k:
            print arr[left], arr[right]
            left += 1
        elif currentSum < k:
            left += 1
        else:
            right -= 1


# example pass
arr = [12, 134, 6, 9, 15, 10, 5, -10, 25, 300]
k = 15
