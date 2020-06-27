#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 01:46:13 2020

@author: karanwaghela
"""

"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.


Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        for x in range(n+1):
            min_val = x
            y, sq = 1, 1
            while(sq <= x):
                min_val = min(min_val, 1 + dp[x - sq])
                y += 1
                sq = y*y
            
            dp[x] = min_val
        
        return dp[n]