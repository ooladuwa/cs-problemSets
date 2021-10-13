#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def treePaths(t):
    if t is None:
        return []
        
    def repeat(root, path, result):
        if root is None:
            return
        path.append(f"{root.value}")
        if root.left is None and root.right is None:
            result.append("->".join(path[:]))
        repeat(root.left, path, result)
        repeat(root.right, path, result)
        path.pop()
    path = []
    result = []
    repeat(t, path, result)
    return result
    
    
    
    
# # Function to convert  
# def listToString(s): 
#     # initialize an empty string
#     str1 = " " 
#     # return string  
#     return (str1.join(s))


# def treePaths(t):
#     holder = []
#     input_stack = [[]]
    
#     holder.insert(0, t)
#     root = holder.pop()

#     def find_path(root, input_stack):
#         # input_stack.append([])
#         if root is not None:
#             input_stack[0].append(root.value)
#             find_path(root.left, input_stack)
#             if root.left == None:
#                 input = input_stack[0]
#                 input = [str(c) for c in input]
#                 input = "->".join(input)
#                 output_stack.append(input)
#                 "->".join(output_stack)
#                 input_stack.pop()
#                 input_stack.append([])
#             print(output_stack)
            
#             print(input_stack)
#             # find_path(root.right, input_stack)
            
            
            
#     #     print(output_stack)
        
#     output_stack = []
    
#     find_path(root, input_stack)
#     # return output


# # outer function
#   # inner function that takes in a root node and an output list
#     # if the root exists
#       # call inner function on the roots left
#       # append the roots value to the output list
#       # call the inner function on the roots right

#   # create an empty list to hold our output
#   # call the inner function pass the ref to the root node, and a ref to the output list

#   # return our output list



"""
Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, where root is the value stored in the root and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes in the path respectively (noden representing the leaf).

Example

For

t = {
    "value": 5,
    "left": {
        "value": 2,
        "left": {
            "value": 10,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": -3,
        "left": null,
        "right": null
    }
}
the output should be
treePaths(t) = ["5->2->10", "5->2->4", "5->-3"].

The given tree looks like this:

    5
   / \
  2  -3
 / \
10  4
Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 710,
-1000 ≤ node value ≤ 1000.

[output] array.string

The root-to-leaf paths, sorted by the leaves in the order that they appear in the pre-order traversal (i.e. from the leftmost leaf to the rightmost).
"""