# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

"""
- create function to insert a node
- create new link node with value provided
- set up a current variable pointing to the head of the list and set a ref to the current node
- while current.next < value
    - traverse to the next node
- set new nodes pointer to current nodes next
- set current nodes pointer to new node
"""

def insertValueIntoSortedLinkedList(l, value):
    new_node = ListNode(value)
    current = l
    
    # edge case if l is empty
    if l == None:
        return new_node
    
    # edge case if value is less than initial current value ie. first node 
    if new_node.value < l.value:
        new_node.next = current
        return new_node
    
    # middle cases
    while current.next is not None: 
        if current.next.value > new_node.value:
            new_node.next = current.next
            current.next = new_node
            return l
            
        current = current.next
    
    # edge case if value to be replaced comes after last element   
    current.next = new_node    
    return l


"""
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, since this is what you will be asked to accomplish in an interview.

You have a singly linked list l, which is sorted in strictly increasing order, and an integer value. Add value to the list l, preserving its original sorting.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

For l = [1, 3, 4, 6] and value = 5, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 5, 6];
For l = [1, 3, 4, 6] and value = 10, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 6, 10];
For l = [1, 3, 4, 6] and value = 0, the output should be
insertValueIntoSortedLinkedList(l, value) = [0, 1, 3, 4, 6].
"""