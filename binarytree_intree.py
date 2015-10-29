""""
find if a is a subset of b,
where both a and b are binary trees
"""

def tree_max(node):
    if not node:
        return float("-inf")
    maxleft  = tree_max(node.left)
    maxright = tree_max(node.right)
    return max(node.key, maxleft, maxright)

def tree_min(node):
    if not node:
        return float("inf")
    minleft  = tree_min(node.left)
    minright = tree_min(node.right)
    return min(node.key, minleft, minright)

def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and
        verify(node.left) and verify(node.right)):
        return True
    else:
        return False

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
