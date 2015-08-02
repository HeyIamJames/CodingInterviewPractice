#remove duplicates from an unsorted linked list


def foo(linkedlist):
    current_node = linkedlist.head
    while current_node is not None:
        checker_node = current_node
        while checker_node.next is not None:
            if checker_node.next.value == current_node.value:
                checker_node.next = checker_node.next.next
            else:
                checker_node = checker_node.next
        current_node = current_node.next
