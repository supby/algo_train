# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

A = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

kernel = [(0,-1),(-1,0),(0,1),(1,0)]

def scan(i, j, word, wi, visited):
    
    if word[wi] != A[i][j]:
        return False
    
    if wi == len(word) - 1:
        return word[wi] == A[i][j]
    
    visited[(i,j)] = True
    
    for k in kernel:
        ti = i+k[0]
        tj = j+k[1]
    
        if ti >= 0 and tj >= 0\
            and ti < len(A) and tj < len(A[0])\
            and A[ti][tj] == word[wi+1]\
            and not visited.get((ti,tj), False)\
            and scan(ti, tj, word, wi+1, visited):
            return True
    
    return False
    

def check_word(word):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if scan(i, j, word, 0, dict()):
                return True
            
    return False

print(check_word('ABCCED'))
print(check_word('SEE'))
print(check_word('ABCB'))
print(check_word('SEEDFBC'))
