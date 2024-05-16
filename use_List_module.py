import List_module

numbers = [5, 3, 4, 7]
avg = List_module.find_average(numbers)
evens = List_module.filter_even(numbers)
reversed_list = List_module.reverse_list(numbers)
concatenated_lists = List_module.concatenate_lists([1, 2, 3], [4, 5, 6])

print(avg)
print(evens)
print(reversed_list)
print(concatenated_lists)