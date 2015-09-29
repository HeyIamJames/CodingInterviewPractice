"""
is a a subtree of b
both are bst
"""

class Node:
02
    ...
03
    def compare_trees(self, node):
04
        """
05
        Compare 2 trees
06
 
07
        @param node tree's root node to compare to
08
        @returns True if the tree passed is identical to this tree
09
        """
        
def compare_trees(self, node):
    if node is None:
        return False
    if self.data != node.data:
        return False
    res = True
    if self.left is None:
        if node.left:
            return False
    else:
        res = self.left.compare_trees(node.left)
    if res is False:
        return False
    if self.right is None:
        if node.right:
            return False
    else:
        res = self.right.compare_trees(node.right)
    return res

