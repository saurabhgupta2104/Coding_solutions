# https://leetcode.com/problems/jump-game-ii/

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""

class Solution:
    def jump(self, n: List[int]) -> int:
        if len(n)<2:
            return 0
        m = n[0]
        count = 1
        ma = 0
        for i in range(1, len(n)):
            if m >= len(n):
                break
            if i > m:
                m = ma
                ma = 0
                count += 1
            ma = max(ma, i+n[i])                
        return count
