""" Create a function that returns the factorial of any positive input number
Helpful tip: Try to solve the problem comfortably in code before trying it recursively!
Factorial is:

4! ==> 4 x 3 x 2 x 1 """

""" What do I need to do? Action plan? """

# Step 1: Restate question
# Return n!
# Step 2: Ask Clarifying Questions
# So we need to return n factorial, where n is any positive input number
# Is the number an integer or can it be float? => use integers
# Step 3: Write out action plan
    # Take number n
    # subtract 1 from n until you get to 1
    # multiply all the numbers together
    # return the result
# Step 4: Write out code
# solve in code before using recursion
def factorial_of_n(n):
    current_counter = int(n)
    current_result = int(n)

    while current_counter > 1:
        print("The current counter is:", current_counter)
        current_counter = current_counter - 1
        current_result = current_result * current_counter
        print(current_result)

factorial_of_n(4)

# If it doesn’t work
# Step 5: Debug
# - What worked, What didn’t
# Repeat process