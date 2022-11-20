import numpy as np
import pandas as pd

'''
Here is the naive solution without divide and conquer
'''
def brute_force_sort(arr):
    sorted_arr = []
    for i, element_i in enumerate(arr):
        
        if not sorted_arr:
            # if sorted array is empty
            sorted_arr.append(element_i)

        else:
            inserted = False
            for j, element_j in enumerate(sorted_arr):
                # print(element_j)
                if element_i < element_j:
                    # if element i > element j, insert the element i in front of the element j.
                    sorted_arr.insert(j, element_i)
                    inserted = True
                    break
            if not inserted:
                sorted_arr.append(element_i)
                
    return sorted_arr

'''
Here comes our divide and conquer solution
'''

def sortArray(nums):      
    # Length 1 is always sorted
    if len(nums) == 1:
        return nums
    
    # Split array into two subarrays
    half = len(nums) // 2
    left = nums[:half]
    right = nums[half:]
    
    # Recursively break the arrays - O(log n)
    left = sortArray(left)
    right = sortArray(right)
    
    # O(n) sort
    return sort(left, right)

# Merge sort helper method
def sort(a, b):
    out = []
    while a and b:
        if a[0] <= b[0]:
            out.append(a.pop(0))
        else:
            out.append(b.pop(0))
    if a:
        out += a
    else:
        out += b
    return out


small_array = [1,5,6,23,432,54,1,1,1]
large_array = list(np.random.rand(3000)) # 3000 random numbers
super_large_array = list(np.random.rand(30000)) # 30000 random numbers