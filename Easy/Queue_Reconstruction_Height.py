#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 00:54:03 2020

@author: karanwaghela
"""

"""
Suppose you have a random list of people standing in a queue.
 
Each person is described by a pair of integers (h, k), 
where h is the height of the person and 
k is the number of people in front of this person who have a height greater than or equal to h. 

Write an algorithm to reconstruct the queue.


Example:

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        people.sort(key = lambda x: (-x[0], x[1]))
        queue = []
        
        for p in people:
            queue.insert(p[1], p)
            
        return queue