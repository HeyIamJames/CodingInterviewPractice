"""
return node at begining of a cricularly linked list
"""

def findBeginning(linkedlist):
    slow = linkedlist.head
    fast = linkedlist.head
    while (fast != None) and (fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return fast
