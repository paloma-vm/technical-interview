# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# SOLUTION 1: Output to Array
# My Solution:
# find length
# divide by 2
# use ceiling to get index if there are even number of elements

# list = [1, 2, 3, 4, 5]  # put nodes into an array

import math

# def middle_of_list(list):
#     length_of_list = len(list)
#     middle_index = math.ceil(length_of_list / 2)
#     return list[middle_index - 1] # because list starts at index zero

# result = middle_of_list(list)
# print(result)


# SOLUTION 2: Fast and Slow Pointer
# Solution using nodes
head = [1, 2, 3, 4, 5]

class ListNode: # node in a linked list
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def middleNode(head):
    slow = fast = head # 2 pointers, one slow, one fast, both pointing to head of ll
    while fast and fast.next:
        slow = slow.next # moves 1 step with each iteration
        fast = fast.next.next # moves 2 steps ahead with each iteration
    print(slow)

    return slow # when the fast pointer is at the end of the list, the
                # slow will be at the middle since the fast moves twice as fast as the slow pointer


# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5  (help from ChatGPT)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)



middle_node = middleNode(head)
print(middle_node.data)

# I am still confused, the question and diagram do not match the output LeetCode expects



