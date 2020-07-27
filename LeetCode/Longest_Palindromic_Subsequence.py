# https://leetcode.com/problems/longest-palindromic-subsequence/

"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
 

Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        g = [[0]*n for _ in range(n)]        
        i = 0
        j = 0
        p = 0
        while(p<n):
            i = 0
            j = p
            while(i<n and j<n):
                if i == j:
                    g[i][j] = 1
                elif s[i] == s[j]:
                    g[i][j] = g[i+1][j-1] + 2
                else:
                    g[i][j] = max(g[i+1][j], g[i][j-1])
                i += 1
                j += 1
            p += 1
        return g[0][n-1]
