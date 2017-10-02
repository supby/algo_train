#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 21:44:27 2017

@author: andrej
"""

'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.

-------------------

Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. 
The left and right pointers in nodes are to be used as previous and next pointers 
respectively in converted DLL. The order of nodes in DLL must be same as Inorder 
of the given Binary Tree. The first node of Inorder traversal (left most node in BT) 
must be head node of the DLL.

'''

def in_order_traverse(node, arr):
    if not node:
        return
    
    in_order_traverse(node.left, arr)
    
    arr.append(node)
    
    in_order_traverse(node.right, arr)

#Your task is to complete this function
#function should return head to the DLL
def BTToDLL(root):
    # do Code here
    
    arr = []
    in_order_traverse(root, arr)
    
    head = arr[0]
    
    cur_node = head
    for i in arr[1:]:
        cur_node.right = i
        i.left = cur_node
        cur_node = i
    
    return head
