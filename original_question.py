# Given a list of entries, find the entry that occurs most often.


# example_1:
# input: list_of_entries = ['dog', 'cat', 'pig', 'dog']
# output: 'dog'

# example_2:
# input: list_of_entries = [1, 2, 3, 7, 4, 6, 4]
# output: [4]




# create a function that returns the entry that occurs most frequently in the list:
def occurs_most(list_of_entries):
    # create a dictionary to store the frequencies
    frequency_dict = {}
    #set a variable to track the largest frequency and set it to zero
    max_freq = 0
    # create a variable to keep track of the most frequent entry
    max_entry = None

    # loop through the list    O(n)
    for entry in list_of_entries:
        # if the entry is already in the dictionary, increment its frequency count by 1,
        if entry in frequency_dict:
            frequency_dict[entry] += 1
        # if it is not, initialize a count of that entry to the dictionary
        else:
            frequency_dict[entry] = 1

        # if the frequency of that entry is greater than the largest frequency so far, 
        # then update the max_freq
        if frequency_dict[entry] > max_freq:
            max_freq = frequency_dict[entry]
            # set the max_entry to the entry that now has the highest frequency
            max_entry = entry
    # return the max_entry, the one that occurs the most in the list
    return max_entry

# Time complexity O(n) because of the loop and it depends how long the list is

# --------------------------------------------------------------------------
# example_1:
list_of_animals = ['dog', 'cat', 'pig', 'dog']
output = occurs_most(list_of_animals)
print(output)

# example_2:
list_of_entries = [1, 2, 3, 7, 4, 6, 4]
another_output = occurs_most(list_of_entries)
print(another_output)