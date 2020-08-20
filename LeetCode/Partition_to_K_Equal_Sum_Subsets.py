# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""

def travel(i, l, ans, val):
    if i == len(l):
        return True
    for j in range(len(ans)):
        if ans[j]+l[i] <= val:
            ans[j] += l[i]
            if travel(i+1, l, ans, val):
                return True
            ans[j] -= l[i]
    return False
    
class Solution:
    def canPartitionKSubsets(self, l: List[int], k: int) -> bool:
        if sum(l)%k != 0:
            return 0
        ans = [0]*k
        val = sum(l)//k
        l.sort(reverse=True)
        for i in range(len(l)):
            return travel(i, l, ans, val)
        
