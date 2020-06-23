#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:47:04 2020

@author: karanwaghela
"""

"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
    
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left, right = root, root
        l_h, r_h = 0, 0
        
        while left != None:
            l_h += 1
            left = left.left
            
        while right != None:
            r_h += 1
            right = right.right
            
        if l_h == r_h:
            return pow(2, l_h) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)