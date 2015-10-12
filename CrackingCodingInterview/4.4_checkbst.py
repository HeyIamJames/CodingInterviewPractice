"""
check if a binary tree is a bst
"""

def tree_max(node):
    maxleft  = float('-inf') if not node.left  else tree_max(node.left)
    maxright = float('-inf') if not node.right else tree_max(node.right)
    return max(node.value, maxleft, maxright)

def tree_min(node):
    minleft  = float('-inf') if not node.right else tree_min(node.left)
    minright = float('-inf') if not node.left else tree_min(node.right)
    return min(node.value, minleft, minright)

def verify(node):
    if tree_max(node.left) <= node.value and node.value <= tree_min(node.right):
       if verify(node.left) and verify(node.right):
           return True
       else:
           return False
    else:
        return False
