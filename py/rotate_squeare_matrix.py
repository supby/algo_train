# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 17:07:53 2017

@author: ASuzanovich
"""

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

num_rows = len(A)
num_cols = len(A[0])

for i in range(int(num_rows/2) + 1):
    for j in range(int(num_cols/2) + 1):
        tmp = A[i][j]
        A[i][j] = A[num_rows - j - 1][num_cols - i - 1]
        A[num_rows - j - 1][num_cols - i - 1] = tmp
        
print(A)