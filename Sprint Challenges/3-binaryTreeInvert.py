"""
Given a binary tree, write a function that inverts the tree.

Example:

Input:
     6
   /   \
  4     8
 / \   / \
2   5 7   9

Output:
     6
   /   \
  8     4
 / \   / \
9   7 5   2
"""


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
        
def csBinaryTreeInvert(root):
    stack = [root]
    while stack:
        node = stack.pop(-1)
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
    return(root)
    
    
    
    # if root is None:
    #     return []

    # result = []
    # queue = []
    # queue.append(root)

    # while len(queue) != 0:
    #     node = queue.pop(-1)
    #     result.append(node.value)
            
    #     if node.left is not None:
    #         queue.append(node.left)

    #     if node.right is not None:
    #         queue.append(node.right)
        
    #     if len(queue) == 2:
    #         temp = queue[0]
    #         queue[0] = queue[1]
    #         queue[1] = temp
        
    # return result


