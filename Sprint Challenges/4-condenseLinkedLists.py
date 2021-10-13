"""
Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. Your function should return a reference to the head of the updated linked list.

Example:
Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):
    bucket = []
    current = node
    prev = None
    next = None
    
    if current == None:
        return
        
    bucket.append(current.value)
    
    while current.next != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
        
        
        if current.value not in bucket:
            bucket.append(current.value)
            continue
    return bucket