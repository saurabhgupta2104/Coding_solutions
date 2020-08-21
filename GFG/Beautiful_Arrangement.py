# https://leetcode.com/problems/beautiful-arrangement/

"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
 

Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
 

Note:

N is a positive integer and will not exceed 15.
"""

def travel(i, d, v, n, l):
    if i == n:
        c[0] += 1
        return 
    
    for j in d[i+1]:
        if v[j-1] == False:
            v[j-1] = True
            l[i] = j
            travel(i+1, d, v, n, l)
            l[i] = 0
            v[j-1] = False
c = [0]
class Solution:
    def countArrangement(self, n: int) -> int:
        if n == 1:
            return 1
        d = {}        
        for i in range(1, n+1):
            d[i] = set()
        for i in range(1, n+1):
            j = i
            while(j<n+1):
                d[i].add(j)
                d[j].add(i)
                j += i
        v = [False]*n    
        ans = [0]*n
        travel(0, d, v, n, ans)
        a = c[0]
        c[0] = 0
        return a
                
        
