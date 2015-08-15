"""
find the last item in a singly linked list
"""

#keep checking list until there is node has no next

def lastnode(linked_list, k):
    if k <= 0:
        return None
    pointer2 = linkedlist.head
    for i in range(k-1):
        if pointer2.next != None:
            pointer2 = pointer2.next
        else:
            return "loop"
    pointer1 = linkedlist.head
    while pointer2.next != None:
        pointer2 = pointer2.next
        pointer1 = pointer1.next
    return pointer1
