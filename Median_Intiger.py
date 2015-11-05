"""
Given a stream of unsorted integers, find the median element in sorted order at any given time.
So, we will be receiving a continuous stream of numbers in some random order and we don’t know the stream length in advance.
Write a function that finds the median of the already received numbers efficiently at any time.
We will be asked to find the median multiple times.
"""

def findMedian(stream):
    if stream % 2 == 0:
        return (-1*steam.maxHeap[0]+stream.minHeap[0])/2.0
    else: 
        eturn -1*stream.maxHeap[0]
