#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 22:37:29 2017

@author: andrej
"""

'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""


def reverse(head, k):
    # Code here
    
    i = 0
    cur_node = head
    new_head = None
    prev_group_head = None
    group_tail = head
    prev_node = None
    while cur_node:
        if i < k:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        
        i += 1
        
        if i == k:
            if not new_head:
                new_head = prev_node
            
            if prev_group_head:
                group_tail.next = prev_group_head
                group_tail = cur_node
                
            prev_group_head = prev_node
            prev_node = None
            
            i = 0
    
    return new_head
        
        
    
    
        
        
    
    