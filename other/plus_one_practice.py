# Question: Plus One
# 
# You are given a  integer represented as an 
# integer array digits, where each digits[i] is 
# the ith digit of the integer. The digits are ordered from 
# most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.
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
# digits does not contain any leading zeroes.

# Solution:
from typing import List

def plusOne(digits: List[int]) -> List[int]:
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

output = plusOne([1, 2, 3])
print(output)
output = plusOne([9])
print(output)
