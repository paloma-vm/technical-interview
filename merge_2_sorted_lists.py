# Question:
# Merge two sorted linked lists (using Python)
# If you are given two sorted linked lists, write a Python function 
# to merge them into one sorted linked list
# For example, 
#     Input: l1 = 1 -> 2-> 3 -> 4, l2 = 1 -> 3-> 4
#     Output: 1 -> 1 -> 2-> 3 -> 4 -> 4


# Solution with pseudocode:
# initialize a class for node list
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# define a function that merges the lists
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Create a dummy node to start the result linked list
    dummy = ListNode(0)
    # Create a pointer to traverse the result linked list
    current = dummy
    
    # Traverse both linked lists until one of them is completely traversed
    while l1 and l2:
        # Compare the values of the head nodes of the linked lists
        if l1.val <= l2.val:
            # Add the smaller value to the result linked list
            current.next = l1
            # Move the pointer of the linked list that had the smaller value to its next node
            l1 = l1.next
        else:
            # Add the smaller value to the result linked list
            current.next = l2
            # Move the pointer of the linked list that had the smaller value to its next node
            l2 = l2.next
        # Move the pointer of the result linked list to its next node
        current = current.next
    
    # Add the remaining nodes of the other linked list to the result linked list
    if l1:
        current.next = l1
    else:
        current.next = l2
    
    # Return the head of the result linked list (excluding the dummy node)
    return dummy.next


# Explanation:
# The listNode class represents each node of the linked lists.  
# The mergeTwo lists function takes l1 and l2 as arguments and 
# returns the head of the merged
# list.  
#  A dummy node is created as the head of the result linked list.
# The current node acts as a pointer to traverse the result list.
# The lists are both traversed until the pointer gets to the end of one of them.

# In the loop, the head of each list is compared and the smaller 
# value is added to the result linked list. 
# Then the pointer of the linked list that had the smaller value
# is moved to the next node.  
# Once one of the lists has been completely traversed, the remaining
# nodes of the other list are added to the end of the resultl linked list
# and the the result list's head is returned.




