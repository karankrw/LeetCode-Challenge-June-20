#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 01:21:23 2020

@author: karanwaghela
"""

"""
Given a set of distinct positive integers, 
find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]

"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        
        if n == 0:
            return result
        
        nums.sort()
        
        next_index = [-1] * n
        sizes = [1] * n
        max_len = 1
        max_index = 0
        
        for i in range(n-1, -1, -1):
            j = i + 1
            _max, _max_index = 0, i
            while j < n:
                if nums[j] % nums[i] == 0 and sizes[j] > _max:
                    _max = sizes[j]
                    _max_index = j
                j += 1
                
            if _max_index != i:
                sizes[i] += sizes[_max_index]
                next_index[i] = _max_index
                if _max + 1 > max_len:
                    max_len = _max + 1
                    max_index = i
                    
        curr = max_index
        while curr >= 0:
            result.append(nums[curr])
            curr = next_index[curr]
            
        return result
                
                
                
                
                
                
                