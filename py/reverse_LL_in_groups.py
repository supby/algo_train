#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 22:37:29 2017

@author: andrej
"""

'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


"""
Given a linked list, write a function to reverse every k nodes 
(where k is an input to the function).If a linked list is given as 
1->2->3->4->5->6->7->8->NULL and k = 3 then output will be 3->2->1->6->5->4->8->7->NULL.

----------------------
Return reference of new head of the reverse linked list
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
    prev_group_tail = head
    group_tail = None
    prev_node = None
    first_group = True
    while cur_node:
        if i < k:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        
        i += 1
        
        if i == k or not cur_node:
            if first_group:
                new_head = prev_node
            
            if not first_group:
                prev_group_tail.next = prev_node
                prev_group_tail = group_tail
                
            group_tail = cur_node
            first_group = False
            
            prev_node = None
            
            i = 0
    
    return new_head
        
        
    
    
        
        
    
    