# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def get_digits(number):
    return [int(s) for s in str(number)]

def get_power_set(number):
    digits = get_digits(number)
    
    ret = []
    
    a = [0]*len(digits)
    
    combinations(a, 0, ret, digits)
    
    return ret
    
def combinations(a, x, acc, digits):
    if x == len(a) - 1:
        a[x] = 0        
        addSet(a, acc, digits)
        
        a[x] = 1
        addSet(a, acc, digits)
        
        return
    
    a[x] = 0
    combinations(a, x+1, acc, digits)
    
    a[x] = 1
    combinations(a, x+1, acc, digits)
    
def addSet(a, acc, digits):
    cur_set = []
    for i in range(len(a)):
        if a[i] == 1:
            cur_set.append(digits[i])
            
    if len(cur_set) > 0:    
        acc.append(cur_set)
        
def is_colorful(number):
    ps = get_power_set(number)
    
    hm = set()
    
    for s in ps:
        mult = 1
        for ss in s:
            mult *= ss
            
        if mult in hm:
            return False
        
        hm.add(mult)
    
    return True
    
    
    
print(is_colorful(326))
print(is_colorful(3245))


