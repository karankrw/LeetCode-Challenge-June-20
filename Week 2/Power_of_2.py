#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:07:39 2020

@author: karanwaghela
"""

"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1


Example 2:

Input: 16
Output: true
Explanation: 24 = 16


Example 3:

Input: 218
Output: false

"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return n & (-n) == n
        
    #FAST
        
        """ 
        if n == 0:
            return False
        
        while n != 1:
            if n % 2 != 0:
                return False
            
            n = n / 2
        
        return True
        SLOW
        """
        
        """
        i = 1
        while i < n:
            i *= 2
        
        return i == n
        
        SLOW
        """
        
        
        
        
        
        
        
            