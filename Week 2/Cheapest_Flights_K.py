#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 00:22:43 2020

@author: karanwaghela
"""

"""
There are n cities connected by m flights. 
Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, 
your task is to find the cheapest price from src to dst with up to k stops. 

If there is no such route, output -1.

Example 1:
    
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200

Example 2:
    
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
"""

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        pq = []
        
        for u, v, w in flights:
            graph[u].append((w, v))
            
        pq.append((0, K+1, src))
        
        while pq:
            price, stops, city = heapq.heappop(pq)
            
            if city == dst:
                return price
            
            if stops > 0:
                for price_to_nei, nei in graph[city]:
                    heapq.heappush(pq, (price + price_to_nei, stops - 1, nei))
                    
        return -1