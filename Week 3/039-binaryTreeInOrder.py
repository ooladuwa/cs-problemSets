#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def binaryTreeInOrderTraversal(root):
    
    def visit(root, output):
        if not root == None:
            visit(root.left, output)
            output.append(root.value)
            visit(root.right, output)
    output = []
    visit(root, output)
    return output
"""
#outer function
    #inner function
        #if root?
            #visit root.left
            #append root.value to output list
            #visit root.right
    
    #create empty list to hold output
    #call inner function and pass the ref to the root node, and a ref to the output list
    
    #return output list
"""



"""
You are given a binary tree. Write a function that returns the binary tree's node values using an in-order traversal.

Example:
Input: [2,None,3,4]

   2
    \
     3
    /
   4
Output: [2,4,3]

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] array.integer
"""