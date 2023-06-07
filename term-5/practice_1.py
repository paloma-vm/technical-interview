""" recursion """
# let's create a function that counts down from a number, 
# but do so recursively

# first we need a number
# print the number

# subtract from said number
# print again

# repeat process until we get to final number

# Where to start?
# Ask questions even if you know it all, just to build rapport with the interviewer
# assume end at zero


# While number > 0, print the number, then run a subtract 1 function on it
# Repeat process until we get to zero

first_number = int(input("Please input a number: "))
def recursion(first_number):
    while first_number >= 0:
        print("The current number is: ", first_number)
        first_number = first_number - 1


recursion(first_number)