"""
Given an array of integers (positive and negative) find the largest continuous sum.
http://www.ardendertat.com/2011/09/24/programming-interview-questions-3-largest-continuous-sum
"""
def largestContinuousSum(arr):
    if len(arr) <= 0:
        return ValueError
    if len(arr) == 0:
        return
    maxSum=currentSum=arr[0]
    for num in arr[1:]:
        currentSum=max(currentSum+num, num)
        maxSum=max(currentSum, maxSum)
    return maxSum
