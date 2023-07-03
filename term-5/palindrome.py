""" #Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1 """

# ------------------------------------------------------------------
# 1. Restate question
# 2. Ask clarifying questions
# 3. State assumptions
# 4. Think through process out loud
#     4a. Brainstorm solution ideas
#     4b. Explain your rationale
#     4c. Discuss tradeoffs
#     4d. Suggest improvements

#  Figure out if integer x is a palindrome, and if it is, return true, otherwise, return false
# One way to solve is by converting to a string and reversing:
def isPalindrome(x):
    x = str(x)
    return x == x[::-1] # slicing syntax, no start (starts at beginning), no stop (stops at end),
                        # step is -1, decrements index by 1

result = isPalindrome(121)
print(result)


