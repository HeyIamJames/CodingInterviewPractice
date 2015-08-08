"""
Implement a function to check if a binary tree is balanced. For t he purposes of
this question, a bal anced t r e e is d ef i ned to be a t r ee such t hat the heights of the
two subtrees of any node never differ by more than one.
"""
#assuming a tree is already given


def balanced(btree):
    if btree is None: return True, 0
    left_balanced, left_depth = balanced(btree.left)
    right_balanced, right_depth = balanced(btree.right)
    btree.depth = 1 + max(left_depth, right_depth)
    return left_balanced and right_balanced and (abs(depth(btree.left) - depth(btree.right)) <= 1), btree.depth
