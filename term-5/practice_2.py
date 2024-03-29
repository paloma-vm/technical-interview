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
# solution using code:
def factorial_of_n(n):
    counter = int(n)
    current_result = int(n)

    while counter > 1:
        print("The counter is:", counter)
        counter = counter - 1
        current_result = current_result * counter
        print("The current result is:", current_result)

factorial_of_n(4)

# another solution using code:
def n_factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    print('The result is:', result)
    return result

# RECURSIVE solution:
def n_factorial_recursive(n):
    if n == 0: # base case
        return 1
    else: # subproblem
        # multiply n times n_factorial_recursive()for the n below it 
        # (like nesting dolls)
        result = n * n_factorial_recursive(n - 1)
        print('The result is:', result)
        return result

print('ANOTHER CODE SOLUTION:')
n_factorial(4)
print('RECURSIVE SOLUTION:')
output = n_factorial_recursive(4)
print(output)

# If it doesn’t work
# Step 5: Debug
# - What worked, What didn’t
# Repeat process