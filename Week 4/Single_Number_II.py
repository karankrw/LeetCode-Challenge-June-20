#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 00:59:23 2020

@author: karanwaghela
"""

"""
Given a non-empty array of integers, every element appears three times except for one, 
which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3

Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(32):
            sum = 0
            
            for num in nums:
                if num & (1<<i) == (1<<i):
                    sum += 1
            result |= (sum % 3) << i
            
        return result if result < (1<<31) else result - (1<<32)