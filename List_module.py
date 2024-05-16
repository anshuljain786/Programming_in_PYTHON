'''
A Module is a file in python containing Python definitions and statements. 
These files help organize code into logical, reusable units. Modules make it
easier to manage and scale Python projects by breaking them down into smaller 
components.
'''

#creating module

def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]

def reverse_list(input_list):
    return input_list[::-1]

def concatenate_lists(list1, list2):
    return list1 + list2
