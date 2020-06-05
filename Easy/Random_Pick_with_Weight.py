#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 02:00:23 2020

@author: karanwaghela
"""

"""
Given an array w of positive integers, where w[i] describes the weight of index i, 
write a function pickIndex which randomly picks an index in proportion to its weight.


Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]

Output: [null,0]


Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]

Output: [null,0,1,1,1,0]


Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. 
Solution's constructor has one argument, the array w. pickIndex has no arguments. 
Arguments are always wrapped with a list, even if there aren't any.
"""


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        
        self.prefix_sum = []
        self.pre_sum = 0
        for i in w:
            self.pre_sum += i
            self.prefix_sum.append(self.pre_sum)
                    
        

    def pickIndex(self):
        """
        :rtype: int
        """
        
        rand_num = random.randint(1, self.pre_sum)
        return self.binary_search(rand_num)
    
    
    def binary_search(self, rand_num):   
        l = 0
        r = len(self.prefix_sum)
        
        while l < r:
            mid = l + (r - l) // 2
            
            if self.prefix_sum[mid] < rand_num:
                l = mid + 1
            else:
                r = mid
                
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()