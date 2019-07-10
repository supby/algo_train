# -*- coding: utf-8 -*-
"""
Algorith to get minimal distance/way to some target in matrix.
Area is matrix where:
Start cell (0,0)
cell value == 1 if there is way/road
cell value == 0 if there is NO way/road
cell value == 9 if target reached
"""

import sys

# here minimal distance is 4
arr = [[0,1,1,1],
       [1,0,1,0],
       [1,0,9,0],
       [1,1,1,0]]

kernel = [(0,-1),(-1,0),(0,1),(1,0)]

row_num = len(arr)
col_num = len(arr[0])

def get_distance(i, j, visited, d):
    #print((i,j), d)
    
    if arr[i][j] == 9: return d
    
    visited[(i,j)] = True
    
    ret_d =  sys.maxsize
    for k in kernel:
        ti = i+k[0]
        tj = j+k[1]
        
        if ti >= 0 and tj >= 0\
            and ti < row_num and tj < col_num\
            and arr[ti][tj] != 0\
            and not visited.get((ti,tj), False):
                #print((ti,tj))
                tmp_d = get_distance(ti, tj, visited, d+1)
                #print(tmp_d)
                if tmp_d < ret_d:
                    ret_d = tmp_d
                #print(d)
    return ret_d
        
        
print(get_distance(0, 0, dict(), 0))
            
    
    

