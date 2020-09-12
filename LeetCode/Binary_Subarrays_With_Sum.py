# https://leetcode.com/problems/binary-subarrays-with-sum/

"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

 

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
 

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""

class Solution:
    def numSubarraysWithSum(self, a: List[int], s: int) -> int:
        
        d = {}
        c = 0
        t = 0
        if s == 0:
            for  i in range(len(a)):
                if a[i] == 0:
                    t += 1
                    c += t
                else:
                    t =0
                    
        else:
            for i in range(len(a)):
                t += a[i]
                d[t] = d.get(t, 0) + 1
                if t-s in d:
                    c += (d[t-s])
            if s in d:
                c += d[s]
        return c
            
