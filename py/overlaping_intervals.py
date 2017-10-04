# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:58:22 2017

@author: ASuzanovich
"""

'''
You have N pairs of intervals, say integers. 
You're required to indentify all intervals that overlap with each other in O(N) time. 
For example, if you have {1, 3} {12, 14} {2, 4} {13, 15} {5, 10}
the answer is {1, 3}, {12, 14}, {2, 4}, {13, 15}. 
Note that you don't need to group them, so the result can be in any order like in the example.
'''

intervals = [(1, 3), (12, 14), (2, 4), (13, 15), (5, 10), (17, 20), (22, 25), (26, 28), (23, 29)]
# sort by start date
sorted_intervals = sorted(intervals)

last_end_interval = None
overlapped_intervals = []
for i in sorted_intervals:
    if last_end_interval and i[0] < last_end_interval[1]:
        overlapped_intervals.append(last_end_interval)
        overlapped_intervals.append(i)
        
    last_end_interval = i
    
print(set(overlapped_intervals))

    
