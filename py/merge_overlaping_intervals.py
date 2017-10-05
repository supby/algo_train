# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:35:33 2017

@author: ASuzanovich
"""

#intervals = [(1,3), (2,6), (8,10), (15,18)]
#intervals = [(1,3), (2,5), (4,6), (7,8)]
intervals = [(1,7), (2,3), (4,6), (8,9)]

arr = []
for i in intervals:
    arr.append((i[0], 's'))
    arr.append((i[1], 'e'))
    
sorted_arr = sorted(arr)

new_intervals = []
last_start = None
balance = 0
for i in sorted_arr:
    if i[1] == 's' and not last_start:
        last_start = i[0]
        
    balance += 1 if i[1] == 's' else -1
    
    if balance == 0:
        new_intervals.append((last_start, i[0]))
        last_start = None
        
print(new_intervals)
    
    
    
        
    
        
        

