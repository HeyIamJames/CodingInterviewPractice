"""
Given a linkedlist of integers and an integer value, 
delete every node of the linkedlist containing that value. 
"""
def delete_node(self,location):
    if location == 0:
        try:
            self.cur_node = cur_node.next
        except AttributeError:
            self.cur_node = None
        finally:
            return 
    node = self.cur_node        
    try:
        for _ in xrange(location):
            node = node.next
    except AttributeError:
        raise ValueError("List does not have index {0}".format(location))
    try:
        node.next = node.next.next 
    except AttributeError:
        node.next = None
