# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:23:13 2017

@author: ASuzanovich
"""

A = [1,3,2,4]
# res = [3,4,4,-1]

s = [A[0]]
out = []

for next_el in A[1:]:
    
    while len(s) > 0:
        pel = s.pop();
    
        if pel < next_el:
            out.append(next_el)
            
    if pel > next_el:
        s.append(pel)
            
    s.append(next_el)
    
out.append(-1)
        
            
print(out)



