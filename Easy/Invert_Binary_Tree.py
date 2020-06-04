#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 00:19:43 2020

@author: karanwaghela
"""

"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            
            root.left, root.right = root.right, root.left
           
            return root

