# example: count Russian dolls
    # asumption: can't have zero dolls

def countRussianDolls(doll):
    if (doll == 1):
        return 1
    else:
        answer = 1 + countRussianDolls(doll -1)
        print(answer)
        return answer
    
# now do recursively
# function that counts down from a number
def countDown(n):
    if (n <= 0): # base case
        print('Done')
    else: # subproblem
        print(n)
        countDown(n-1)

# TEST
countRussianDolls(5)
print('*************')
countDown(5)

# Problem
# Create a function that returns the factorial of any positive input number
# Helpful tip: Try to solve the problem comfortably in code before trying it recursively!

# We did this problem with Salomon earlier this term. 
# I did the problem in term-5/practice_2.py

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
