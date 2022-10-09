# -*- coding: utf-8 -*-
# =============================================================================
# Algorithms project 2
# Due date: October 9, 2022
# Authors: Matt Wagers, Caylen Johnson, Tyler Menzie
# =============================================================================
# This code was written and created to test the time complexity and
#   sorting computation time of 4 different sorting algorithms.
# =============================================================================
# Arrays of lengths: 100, 1_000, 10_000, 100_000
# Algorithms tested: Bubble, Merge, Quick, Insertion
# =============================================================================
# Arrays were tested with unique values in random order
#   then tested against an already sorted array (least to greatest)
#   finally tested against a reversed ordered array (greatest to least)
# =============================================================================

import time
import random 

# Generates random numbers
# This was used to test arrays with possible duplicate values
# =============================================================================
# def randomNumberList(num, start, end):
#     result = []
#     for i in range(num):
#         temp = random.randint(start, end + 1)
#         result.append(temp)
#         
#     return result
# =============================================================================

# Function to create an array with unique numbers in each element
# random.shuffle() used to randomize the locations of each value
def randomNumberList(num, start, end):
    result = []
    for i in range(num):
        result.append(i + 1)
        
    random.shuffle(result)
    return result
# End of Random Number List

# Code for Bubble Sort
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
        
    n = len(arr)
    swapped = True
    x = -1
    
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True  
    return arr
# End of Bubble Sort

# Code for Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    
    # Merge each side together
    return merge(left, right, arr.copy())
def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
        
    return merged
# End of Merge Sort

# Code for Quick Sort
# Failed to run correctly with array of 10,000 elements or more
# =============================================================================
# def partition(array, begin, end):
#     pivot_idx = begin
#     for i in range(begin + 1, end + 1):
#         if array[i] <= array[begin]:
#             pivot_idx += 1
#             array[i], array[pivot_idx] = array[pivot_idx], array[i]
#     array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
#     return pivot_idx
# def quick_sort_recursion(array, begin, end):
#     if begin >= end:
#         return
#     pivot_idx = partition(array, begin, end)
#     quick_sort_recursion(array, begin, pivot_idx - 1)
#     quick_sort_recursion(array, pivot_idx + 1, end)
# def quick_sort(array, begin = 0, end = None):
#     if end is None:
#         end = len(array)  - 1
#     return quick_sort_recursion(array, begin, end)
# =============================================================================

# Secondary code for Quick Sort
# Similar issue to the previous Quick Sort Algorithm
# =============================================================================
# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1
#     for j in range(low, high):
#         if array[j] <= pivot:
#             i = i + 1
#             (array[i], array[j]) = (array[j], array[i])
#     (array[i + 1], array[high]) = (array[high], array[i + 1])
#     return i + 1
# 
# def quick_sort(array, low, high):
#     if low < high:
#         pi = partition(array, low, high)
#         quick_sort(array, low, pi - 1)
#         quick_sort(array, pi + 1, high)
# =============================================================================

# This version of Quick Sort yielded no Stack Overflow errors
# Iterative and non-recursive
# This code was found at (https://stackoverflow.com/questions/68524038/is-there-a-python-implementation-of-quicksort-without-recursion)
def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]
    
    for j in range(l, h):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)

def quick_sort(arr, l, h):
    size = h - l + 1
    stack = [0] * (size)
    
    top = -1
    
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        
        p = partition(arr, l, h)
        
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
# End of Quick Sort Algorithm

# Code for Insertion Sort
def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor
        
    return arr
# End of Insertion Sort

# Reverse order to test worst case for sorts
# Sorts array by greatest to least
def reverse_order(arr):
    for i in range(len(arr)):
        max = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max]:
                max = j
                
        arr[max], arr[i] = arr[i], arr[max]
    return arr
# End of Reverse Order

# Call this function by sending an array to test
# along with a sorting algorithm to perform
# Algorithms available:
#   bubble_sort
#   insertion_sort
#   merge_sort
#   quick_sort
# Returns T(n)
def experiment(arr, sort):
    if sort == quick_sort:
        start_time = time.time()
        quick_sort(arr, 0, len(arr) - 1)
        arr_total_time = time.time() - start_time
        return arr_total_time
    else:
        start_time = time.time()
        sort(arr)
        arr_total_time = time.time() - start_time
        return arr_total_time
# End of Experiment Function


# Testing Zone

# Create Array Lists
arrH = randomNumberList(100, 1, 100)
arrT = randomNumberList(1000, 1, 1000)
arrTT = randomNumberList(10_000, 1, 10_000)
arrHT = randomNumberList(100_000, 1, 100_000)


# Test Buble Sort
print("Array of 100 Elements: Bubble Sort")
print("Average T(n): ", experiment(arrH, bubble_sort))
print("Best T(n): ", experiment(arrH, bubble_sort))
print("Worst T(n): ", experiment(reverse_order(arrH), bubble_sort))

print("\nArray of 1000 Elements: Bubble Sort")
print("Average T(n): ", experiment(arrT, bubble_sort))
print("Best T(n): ", experiment(arrT, bubble_sort))
print("Worst T(n): ", experiment(reverse_order(arrT), bubble_sort))

print("\nArray of 10_000 Elements: Bubble Sort")
print("Average T(n): ", experiment(arrTT, bubble_sort))
print("Best T(n): ", experiment(arrTT, bubble_sort))
print("Worst T(n): ", experiment(reverse_order(arrTT), bubble_sort))

print("\nArray of 100_000 Elements: Bubble Sort")
print("Average T(n): ", experiment(arrHT, bubble_sort))
print("Best T(n): ", experiment(arrHT, bubble_sort))
print("Worst T(n): ", experiment(reverse_order(arrHT), bubble_sort))

# Test Insertion Sort
print("Array of 100 Elements: Insertion Sort")
print("Average T(n): ", experiment(arrH, insertion_sort))
print("Best T(n): ", experiment(arrH, insertion_sort))
print("Worst T(n): ", experiment(reverse_order(arrH), insertion_sort))
 
print("\nArray of 1000 Elements: Insertion Sort")
print("Average T(n): ", experiment(arrT, insertion_sort))
print("Best T(n): ", experiment(arrT, insertion_sort))
print("Worst T(n): ", experiment(reverse_order(arrT), insertion_sort))
 
print("\nArray of 10_000 Elements: Insertion Sort")
print("Average T(n): ", experiment(arrTT, insertion_sort))
print("Best T(n): ", experiment(arrTT, insertion_sort))
print("Worst T(n): ", experiment(reverse_order(arrTT), insertion_sort))

print("\nArray of 100_000 Elements: Insertion Sort")
print("Average T(n): ", experiment(arrHT, insertion_sort))
print("Best T(n): ", experiment(arrHT, insertion_sort))
print("Worst T(n): ", experiment(reverse_order(arrHT), insertion_sort))

# Test Merge Sort
print("Array of 100 Elements: Merge Sort")
print("Average T(n): ", experiment(arrH, merge_sort))
print("Best T(n): ", experiment(arrH, merge_sort))
print("Worst T(n): ", experiment(reverse_order(arrH), merge_sort))
 
print("\nArray of 1000 Elements: Merge Sort")
print("Average T(n): ", experiment(arrT, merge_sort))
print("Best T(n): ", experiment(arrT, merge_sort))
print("Worst T(n): ", experiment(reverse_order(arrT), merge_sort))
 
print("\nArray of 10_000 Elements: Merge Sort")
print("Average T(n): ", experiment(arrTT, merge_sort))
print("Best T(n): ", experiment(arrTT, merge_sort))
print("Worst T(n): ", experiment(reverse_order(arrTT), merge_sort))
 
print("\nArray of 100_000 Elements: Merge Sort")
print("Average T(n): ", experiment(arrHT, merge_sort))
print("Best T(n): ", experiment(arrHT, merge_sort))
print("Worst T(n): ", experiment(reverse_order(arrHT), merge_sort))

# Test Quick Sort
print("Array of 100 Elements: Quick Sort")
print("Average T(n): ", experiment(arrH, quick_sort))
print("Best T(n): ", experiment(arrH, quick_sort))
print("Worst T(n): ", experiment(reverse_order(arrH), quick_sort))
  
print("\nArray of 1000 Elements: Quick Sort")
print("Average T(n): ", experiment(arrT, quick_sort))
print("Best T(n): ", experiment(arrT, quick_sort))
print("Worst T(n): ", experiment(reverse_order(arrT), quick_sort))
  
print("\nArray of 10_000 Elements: Quick Sort")
print("Average T(n): ", experiment(arrTT, quick_sort))
print("Best T(n): ", experiment(arrTT, quick_sort))
print("Worst T(n): ", experiment(reverse_order(arrTT), quick_sort))
  
print("\nArray of 100_000 Elements: Quick Sort")
print("Average T(n): ", experiment(arrHT, quick_sort))
print("Best T(n): ", experiment(arrHT, quick_sort))
print("Worst T(n): ", experiment(reverse_order(arrHT), quick_sort))
