# -*- coding: utf-8 -*-
# Algorithms project 2
# Due date: October 9, 2022
# Authors: Matt Wagers, ..., ...

import random # May delete later
import numpy as np
import pandas as pd # Could use for graphs

#arrH = []
#for i in range(1,100):
#    arrH[i] = random.randint(1, 100)



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




arrH = randomNumberList(100, 1, 100)
print(arrH)
insertion_sort(arrH)
print(arrH)