# Question:
# Roman Numeral to Integer

# Given a roman numeral as a string, 
# write a function to convert it to an integer.
# (using Python)

# Input: "III"
# Output: 3

# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.



# Solution with pseudocode:
# define a function that takes a string, s, and returns an integer
def roman_to_int(s: str) -> int:
    # create a dictionary to store the values of each Roman numeral
    roman_values = {  # assigning O(1)
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    # initialize the result as 0
    result = 0
    # initialize the previous value as 0
    prev_value = 0
    # iterate over the string from right to left
    # using a reverse slice (starting at last element of the list)
    for c in s[::-1]: # O(n) loop
        # for each character, c, look up its value in the 
        # dictionary roman_values
        curr_value = roman_values[c]
        # if its value is greater than or equal to the
        # previous value, we add it to the result
        if curr_value >= prev_value:
            result += curr_value
        # otherwise, we subtract it from the result
        else:
            result -= curr_value
        # update the previous value to the current value for the 
        # next iteration
        prev_value = curr_value
    # return the result
    return result

# Time complexity O(n) because it depends how long the roman numeral is

# Explanation:
# This is one way to solve this problem, using a dictionary to
# store the values of each Roman numeral.  
# -------------------------
output = roman_to_int('XXIV')
print(output)
output = roman_to_int('XXX')
print(output)
