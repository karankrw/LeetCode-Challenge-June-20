#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 02:05:32 2020

@author: karanwaghela
"""

"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. 
Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, 
you should return the itinerary that has the smallest lexical order 
when read as a single string. 

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

All airports are represented by three capital letters (IATA code).

You may assume all tickets form at least one valid itinerary.

One must use all the tickets once and only once.

Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
"""

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.adj = {}
        tickets.sort(key = lambda x: x[1])
        
        for _from, _to in tickets:
            if _from in self.adj:
                self.adj[_from].append(_to)
            else:
                self.adj[_from] = [_to]
                
        self.route = []
        self.dfs("JFK")
        
        return self.route[::-1]
    
    
    def dfs(self, airport):
        while airport in self.adj and len(self.adj[airport]) > 0:
            _to = self.adj[airport][0]
            self.adj[airport].pop(0)
            self.dfs(_to)
        
        self.route.append(airport)
        
        