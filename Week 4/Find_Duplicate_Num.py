#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 01:22:03 2020

@author: karanwaghela
"""

"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2


Example 2:

Input: [3,1,3,4,2]
Output: 3


Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_idx, max_val = 0, 0
        for i in range(n):
            idx = nums[i] % n
            nums[idx] += n
            
        for i in range(n):
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i
                
            nums[i] %= n
            
        return max_idx