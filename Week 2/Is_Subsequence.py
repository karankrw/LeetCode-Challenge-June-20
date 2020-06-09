#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 01:07:27 2020

@author: karanwaghela
"""

"""
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the 
original string by deleting some (can be none) of the characters without 
disturbing the relative positions of the remaining characters. 
(ie, "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true


Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) == 0:
            return True
        
        si = 0
        for i in range(len(t)):
            if t[i] == s[si]: si += 1
            if si == len(s): return True
        
        return si == len(s)
    