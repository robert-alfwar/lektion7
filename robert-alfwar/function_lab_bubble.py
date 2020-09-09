import random
import timeit

# Bubble Sort

numbers = [1, 9, 0, 5, 18, 4, 12, 6, 8, 14, 7, 16, 10, 11, 13, 15, 3, 2, 17]

def elements(numbers, index):
    return numbers[index], numbers[index+1]

def element_greater(elements):
    return elements[0] > elements[1]

def swap_elements(numbers: list, index):
    to_swap = numbers.pop(index)
    numbers.insert(index + 1, to_swap)

def sort_iteration(numbers):
    changes = False
    for index in range(0, len(numbers) -1):
        if element_greater(elements(numbers, index)):
            swap_elements(numbers, index)
            changes = True
    return changes

def bubble_sort(numbers):
    changes = True
    while changes:
        changes = sort_iteration(numbers)
    return numbers

print(f'Before sort: {numbers}')
sorted_numbers = bubble_sort(numbers)
print(f'Bubble sorted: {sorted_numbers}')

print(timeit.timeit('bubble_sort(numbers)', 'from __main__ import bubble_sort, numbers'))