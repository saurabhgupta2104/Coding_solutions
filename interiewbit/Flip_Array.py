# https://www.interviewbit.com/problems/flip-array/

"""
Given an array of positive elements, you have to flip the sign of some of its elements such that the resultant sum of the elements of array should be minimum non-negative(as close to zero as possible). Return the minimum no. of elements whose sign needs to be flipped such that the resultant sum is minimum non-negative.

Constraints:

 1 <= n <= 100
Sum of all the elements will not exceed 10,000.

Example:

A = [15, 10, 6]
ans = 1 (Here, we will flip the sign of 15 and the resultant sum will be 1 )

A = [14, 10, 4]
ans = 1 (Here, we will flip the sign of 14 and the resultant sum will be 0)
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, a):
        a = list(a)
        a.sort()
        s = sum(a)
        s = s//2
        l = []
        for i in range(len(a)):
            l.append([1]+ [float('inf')]*(s)) 
        if a[0]<s+1: 
            l[0][a[0]] = 1
        
        for i in range(1, len(a)):
            if a[i]<s+1:
                l[i][a[i]] = 1
 
            for j in range(1,s+1):
                if j<a[i]:
                    l[i][j] = l[i-1][j]
                
                else:
                    if l[i-1][j-a[i]] >0:
                        l[i][j] = min(l[i-1][j-a[i]]+1, l[i-1][j], l[i][j])
                    else:
                        l[i][j] = min(l[i][j-1], l[i][j])

        j = s
        i = len(a)-1
        c = 0
        while(l[i][j]==float('inf')):
            
            j-=1
        return l[i][j]

                    
