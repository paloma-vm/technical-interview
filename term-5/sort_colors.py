# Medium

# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

# Solution start provided:
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

# ------ SOLUTION ----------------
# can't use sort
# create a pointer, or pointers
# compare the pointer to the first element,
# if the pointer is greater or equal to the element it is being compared to,
# move the pointer up an index space 

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # make pointers
        low = 0
        middle = 0
        high = len(nums) - 1 # the last element

        # do as long as the middle pointer is less than or equal to the high pointer
        while middle <= high:
            # if nums at the index of the middle pointer is zero,
            if nums[middle] == 0:
                # switch it with nums[low] and increment low and middle pointers
                nums[middle], nums[low] = nums[low], nums[middle]
                low += 1
                middle += 1
            # if nums[middle] is 1, increment middle pointer
            elif nums[middle] == 1:
                middle += 1
            # lastly, if nums[middle] is 2, switch  nums of middle and high and decrement high
            else:
                nums[middle], nums[high] = nums[high], nums[middle]
                high -= 1
            # don't return anything!

# Time complexity:
    # worst: O(n)

# Notes:
    # this is also known as the Dutch Flag Algortithm (red, white, blue) 
    # or 3-way quicksort
    
    




  
