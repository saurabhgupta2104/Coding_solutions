# https://leetcode.com/problems/minimum-path-sum/

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, g: List[List[int]]) -> int: 
        for i in range(len(g)):
            for j in range(len(g[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    g[i][j] += g[i][j-1] 
                elif j == 0:
                    g[i][j] += g[i-1][j]
                else:
                    g[i][j] += min(g[i][j-1], g[i-1][j])
        return g[-1][-1]
                
