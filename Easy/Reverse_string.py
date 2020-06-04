#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 00:18:03 2020

@author: karanwaghela
"""


"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]


Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s) // 2):
            s[i], s[-i -1] = s[-i -1], s[i]