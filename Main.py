# -*- coding: utf-8 -*-
# Algorithms project 2
# Due date: October 9, 2022
# Authors: Matt Wagers, ..., ...

import time
import random 
import pandas as pd # Could use for graphs



# Generates random numbers
def randomNumberList(num, start, end):
    result = []
    for i in range(num):
        temp = random.randint(start, end + 1)
        result. append(temp)
        
    return result

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


# Code for Quick Sort
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx
def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx - 1)
    quick_sort_recursion(array, pivot_idx + 1, end)
def quick_sort(array, begin = 0, end = None):
    if end is None:
        end = len(array) - 1
    return quick_sort_recursion(array, begin, end)


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

# Testing Zone

# Create Lists
arrH = randomNumberList(100, 1, 100)
arrT = randomNumberList(1000, 1, 1000)
arrTT = randomNumberList(10_000, 1, 10_000)
arrHT = randomNumberList(100_000, 1, 100_000)
#print(arrH)

# Record time for array of 100 elements
# After each test, the array(list) is shuffled
start_time = time.time()
bubble_sort(arrH)
arrH_total_time = time.time() - start_time
print("Sorting time of Bubble Sort using 100 elements: ", arrH_total_time, " seconds\n")
random.shuffle(arrH)

start_time = time.time()
merge_sort(arrH)
arrH_total_time = time.time() - start_time
print("Sorting time of Merge Sort using 100 elements: ", arrH_total_time, " seconds\n")
random.shuffle(arrH)

start_time = time.time()
quick_sort(arrH)
arrH_total_time = time.time() - start_time
print("Sorting time of Quick Sort using 100 elements: ", arrH_total_time, " seconds\n")
random.shuffle(arrH)

start_time = time.time()
insertion_sort(arrH)
arrH_total_time = time.time() - start_time
print("Sorting time of Insertion Sort using 100 elements: ", arrH_total_time, " seconds\n\n")
random.shuffle(arrH)


# Record time for array of 1000 elements
start_time = time.time()
bubble_sort(arrT)
arrT_total_time = time.time() - start_time
print("Sorting time of Bubble Sort using 1000 elements: ", arrT_total_time, " seconds\n")
random.shuffle(arrT)

start_time = time.time()
merge_sort(arrT)
arrT_total_time = time.time() - start_time
print("Sorting time of Merge Sort using 1000 elements: ", arrT_total_time, " seconds\n")
random.shuffle(arrT)

start_time = time.time()
quick_sort(arrT)
arrT_total_time = time.time() - start_time
print("Sorting time of Quick Sort using 1000 elements: ", arrT_total_time, " seconds\n")
random.shuffle(arrT)

start_time = time.time()
insertion_sort(arrT)
arrT_total_time = time.time() - start_time
print("Sorting time of Insertion Sort using 1000 elements: ", arrT_total_time, " seconds\n\n")
random.shuffle(arrT)


# Record time for array of 10_000 elements
start_time = time.time()
bubble_sort(arrTT)
arrTT_total_time = time.time() - start_time
print("Sorting time of Bubble Sort using 10000 elements: ", arrTT_total_time, " seconds\n")
random.shuffle(arrTT)

start_time = time.time()
merge_sort(arrTT)
arrTT_total_time = time.time() - start_time
print("Sorting time of Merge Sort using 10000 elements: ", arrTT_total_time, " seconds\n")
random.shuffle(arrTT)

start_time = time.time()
quick_sort(arrTT)
arrTT_total_time = time.time() - start_time
print("Sorting time of Quick Sort using 10000 elements: ", arrTT_total_time, " seconds\n")
random.shuffle(arrTT)

start_time = time.time()
insertion_sort(arrTT)
arrTT_total_time = time.time() - start_time
print("Sorting time of Insertion Sort using 10000 elements: ", arrTT_total_time, " seconds\n\n")
random.shuffle(arrTT)


# Record time for array of 100_000 elements
start_time = time.time()
bubble_sort(arrHT)
arrHT_total_time = time.time() - start_time
print("Sorting time of Bubble Sort using 100000 elements: ", arrHT_total_time, " seconds\n")
random.shuffle(arrHT)

start_time = time.time()
merge_sort(arrHT)
arrHT_total_time = time.time() - start_time
print("Sorting time of Merge Sort using 100000 elements: ", arrHT_total_time, " seconds\n")
random.shuffle(arrHT)

start_time = time.time()
quick_sort(arrHT)
arrHT_total_time = time.time() - start_time
print("Sorting time of Quick Sort using 100000 elements: ", arrHT_total_time, " seconds\n")
random.shuffle(arrHT)

start_time = time.time()
insertion_sort(arrHT)
arrHT_total_time = time.time() - start_time
print("Sorting time of Insertion Sort using 100000 elements: ", arrHT_total_time, " seconds\n\n")
random.shuffle(arrHT)
