"""
Note: Your solution should have O(l.length) time complexity and O(1) space complexity, since this is what you will be asked to accomplish in an interview.

Given a singly linked list, reverse and return it.

Example

For l = [1, 2, 3, 4, 5], the output should be
reverseLinkedList(l) = [5, 4, 3, 2, 1].
"""


"""
You are given the root node of a binary search tree (BST).

You need to write a function that returns the sum of values of all the nodes with a value between lower and upper (inclusive).

The BST is guaranteed to have unique values.

Example 1:

Input:
root = [10, 5, 15, 3, 7, null, 18]
lower = 7
upper = 15

         10
         / \
        5  15
       / \    \
      3   7    18

Output:
32
Example 2:

Input:
root = [10,5,15,3,7,13,18,1,null,6]
lower = 6
upper = 10

           10
          /  \
       5       15
     / \     /   \ 
    3   7  13   18
   /   /
  1   6

Output:
23
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBSTRangeSum(root, lower, upper):
    if root!=None:
        l=0
        r=0
			
        if root.value>=lower:
            l=csBSTRangeSum(root.left,lower,upper)
				
        if root.value<=upper:
            r=csBSTRangeSum(root.right,lower,upper)
				
        if root.value<=upper and root.value>=lower:
            return root.value+l+r
        else:
            return l+r
				
    else:
        return 0
    
    # def traverse(root,lower,upper):
    #     if root:
    #         if lower<=root.value<=upper:
    #             sum1+=root.value
    #         if lower<root.value:
    #             traverse(root.left,lower,upper)
    #         if root.value<upper:
    #             traverse(root.right,lower,upper)
                
    #     sum1=0
    #     traverse(root, lower ,upper)
    #     return sum1
                
    # def DFT(root, out):
    #     if root:
    #         print("hello")
    #         DFT(root.left, into)
    #         out.append(root.value)
    #         if not lower <= root.value <= upper:
    #             out.pop()
    #         DFT(root.right, out)
                
    #     out = [] 
    #     DFT(root, out)
    #     return out