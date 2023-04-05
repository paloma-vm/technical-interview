# Question: Plus One
# 
# Given a non-empty list of decimal digits representing a 
# non-negative integer, increment one to the integer
#
# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# 
# Example 2: 
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].


# Assumptions/Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

# Solution with pseudocode:
# import List from typing
from typing import List
# define a function that takes a list of integers and 
# returns a list of integers
def plusOne(digits: List[int]) -> List[int]:
    # get the length of the list digits and assign the value
    # to the variable n
    n = len(digits)
    # 
    carry = 1 # this is the value that is added to the 
    # least significant digit (the last element in the list)
    # loop through the digits list from right to left with step of -1
    for i in range(n-1, -1, -1): # start, stop, step
        # (stop value is exclusive, in this case, of -1, i.e., the last index)
        # add the value of carry to each digit
        digits[i] += carry
        # if digits[i] plus carry equals 10, set digits[i] to zero and set carry to 1
        if digits[i] == 10:
            digits[i] = 0
            carry = 1
        # otherwise, set carry to zero and break out of the loop
        else:
            carry = 0
            break
    # if the value of carry is not zero, i.e. carry equals 1, 
    # insert the integer 1 at index zero of the list, digits
    if carry:
        digits.insert(0, 1) # at index zero, insert 1
    # return the updated list
    return digits

# Explanation:
# 

# Plain code:

def plusOne(digits: List[int]) -> List[int]: # pylint: disable=[E0102:function-redefined]
    n = len(digits)
    carry = 1
    for i in range(n-1, -1, -1):
        digits[i] += carry
        if digits[i] == 10:
            digits[i] = 0
            carry = 1
        else:
            carry = 0
            break
    if carry:
        digits.insert(0, 1)
    return digits

# Try it:
# ----------------------------------2

output = plusOne([1, 2, 3])
print(output)
output = plusOne([9])
print(output)
output = plusOne([1, 2, 9])
print(output)
