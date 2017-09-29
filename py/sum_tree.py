# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

---------------------

Write a function that returns true if the given Binary Tree is SumTree else false. 
A SumTree is a Binary Tree where value of every node x is equal to sum of nodes 
present in its left subtree and right subtree of x. An empty tree is SumTree 
and sum of an empty tree can be considered as 0. A leaf node is also considered 
as SumTree.
"""

'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return True is Tree is SumTree else return False
def isSumTree(root):
    # Code here
    
    if not root:
        return True
    
    return root.data == get_sum(root.left) + get_sum(root.right) 
        and isSumTree(root.left)
        and isSumTree(root.right)
        
def get_sum(node):
    if not node:
        return 0
        
    return get_sum(node.left) + get_sum(node.right)

