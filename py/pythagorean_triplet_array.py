# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:27:43 2017

@author: ASuzanovich
----

Given an array of integers, write a function that returns true 
if there is a triplet (a, b, c) that satisfies a^2 + b^2 = c^2.

-------

Input: arr[] = {3, 1, 4, 6, 5}
Output: True
There is a Pythagorean triplet (3, 4, 5).

Input: arr[] = {10, 4, 6, 12, 5}
Output: False
There is no Pythagorean triplet.

"""

# --- O(n) + O(n^2) + O(n^2) => O(n^2)
def is_triplet(arr):
    squares = [i ** 2 for i in arr]
    
    sums = []
    for i in range(len(squares)-1):
        for j in range(len(squares)-i-1):
            sums.append(squares[i] + squares[i+j+1])
            
    for s in sums:
        for sq in squares:
            if s == sq:
                return True
    
    return False

print(is_triplet([3, 1, 4, 6, 5]))
print(is_triplet([10, 4, 6, 12, 5]))
