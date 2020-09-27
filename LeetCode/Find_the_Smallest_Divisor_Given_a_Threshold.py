# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

"""
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

 

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
Example 3:

Input: nums = [19], threshold = 5
Output: 4
 

Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6
"""

import math
def divisor(l, n):
    ans = 0
    
    for i in l:
        ans += math.ceil(i/n)
    return ans


class Solution:
    def smallestDivisor(self, l: List[int], t: int) -> int:
        if sum(l)<=t:
            return 1
        s = sum(l)
        ans = 0
        x = 0
        i = 1
        j = 1
        while(x<t):
            j = i
            x = divisor(l, i)
            if x<t:
                i *= 2 
            else:
                break
        mid = 0
        j = max(l)
        p = -1
        # print(i, j)
        
        while(i<j):
            
            mid = (i+j)//2
            x = divisor(l, mid)
            # print('mid',x, mid)                
            if x<t:
                j = mid
            elif x == t:
                break
            else:
                i = mid+1
            if i == j:
                mid = j
                break
        
        while(1):
            # print(mid)
            x = divisor(l, mid-1)
            if x <= t:
                mid -= 1
            else:
                break
                
        return mid
                
                        
        
        
        
