# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:00:48 2017

@author: ASuzanovich
"""

D = [1, 23, 12, 9, 30, 2, 50]
k = 3

# -------------------- O(n*k) ------

def add_to_list(limit_arr, val, limit):
    
    if len(limit_arr) == 0:
        limit_arr.append(val)
        return
        
    i = 0
    while i < len(limit_arr):
        if limit_arr[i] < val:
            # insert to linked list
            limit_arr.insert(i, val)
            break        
        
        i += 1
        
    if len(limit_arr) > limit:
        del limit_arr[-1]

k_arr = [] # It is Linked list
        
for d in D:
    add_to_list(k_arr, d, k)
    
print(k_arr)
    
# -------------------------
    