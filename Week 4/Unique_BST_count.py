#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 01:22:54 2020

@author: karanwaghela
"""

"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5

Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        sol = [0] * (n+1)
        sol[0], sol[1] = 1, 1
        
        for i in range(2, n+1):
            for j in range(0, i):
                sol[i] += sol[j] * sol[i-j-1]
                
        return sol[n]