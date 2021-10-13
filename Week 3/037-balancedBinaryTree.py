#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def max_depth(root):
    if root is None:
        return 0
        
    return max(max_depth(root.left), max_depth(root.right)) + 1

def min_depth(root):
    if root is None:
        return 0
        
    return min(min_depth(root.left), min_depth(root.right)) + 1

def balancedBinaryTree(root):
    return max_depth(root) - min_depth(root) <= 1




# a different recursive way that works:

    # if root is None:
    #     return True
    
    # def get_height(root):
    #     if root is None:
    #         return 0
    #     return max(get_height(root.left), get_height(root.right)) + 1
    
    # def repeat(root):
    #     if root is None:
    #         return 0
            
    #     else:
    #         l = get_height(root.left)
    #         r = get_height(root.right)
    #         return abs(l - r)
    
    # h = repeat(root)
    # if h > 1:
    #     return False
    # return balancedBinaryTree(root.left) and balancedBinaryTree(root.right)



    """
    You are given a binary tree and you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.

Example 1:
Given the following tree [5,10,25,None,None,12,3]:

    5
   / \
 10  25
    /  \
   12   3
return True.

Example 2:
Given the following tree [5,6,6,7,7,None,None,8,8]:

       5
      / \
     6   6
    / \
   7   7
  / \
 8   8
return False.

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] boolean
"""
