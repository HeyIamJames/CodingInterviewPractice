"""
This is a very common interview question.
Given a binary tree, check whether it’s a binary
search tree or not. Simple as that..
http://www.ardendertat.com/2011/10/10/programming-interview-questions-7-binary-search-tree-check/
"""


class Node:
    def __init__(self, val=None):
        self.left, self.right, self.val = None, None, val

INFINITY = float("infinity")
NEG_INFINITY = float("-infinity")

def isBST(tree, lastNode=[NEG_INFINITY]):
    if tree is None:
        return True
    if not isBST(tree.left, lastNode):
        return False
    if tree.val < lastNode[0]:
        return False
    lastNode[0] = tree.val
    return isBST(tree.right, lastNode)
