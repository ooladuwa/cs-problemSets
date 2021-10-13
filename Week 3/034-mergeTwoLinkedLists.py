# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    # set up to be able to iterate between two lists
    current_1 = l1 
    current_2 = l2
    
    # create new list and current and set to None
    new_list = None
    current = None
    
    # edge case if l1 or l2 == None
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    # edge case if l1 and l2 are not equal lengths
        
    
    if l1.value < l2.value:
        new_list = ListNode(l1.value)
        current_1 = current_1.next
    else:
        new_list = ListNode(l2.value)
        current_2 = current_2.next
    
    current = new_list
    
    # progress through l1 while both lists exist
    while current_1 is not None and current_2 is not None:
        
        if current_1.value < current_2.value:
            current.next = ListNode(current_1.value)
            current_1 = current_1.next
        else:
            current.next = ListNode(current_2.value)
            current_2 = current_2.next
            
        current = current.next
    
    if current_1 is not None:
        current.next = current_1
        
    if current_2 is not None:
        current.next = current_2
    
    return new_list
        
        
"""
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
"""