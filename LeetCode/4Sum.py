# https://leetcode.com/problems/4sum/

"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    def fourSum(self, n: List[int], t: int) -> List[List[int]]:
        # ans = []
        # d = set()
        # for i in range(len(n)):
        #     for j in range(i, len(n)):
        #         for k in range(j, len(n)):
        #             for l in range(k, len(n)):
        #                 if i!=j!=k!=l and n[i]+n[j]+n[k]+n[l] == t:
        #                     a = [n[i], n[j], n[k], n[l]]
        #                     a.sort()
        #                     if str(a[0])+str(a[1])+str(a[2])+str(a[3]) not in d:
        #                         ans.append([n[i], n[j], n[k], n[l]])
        #                         d.add(str(a[0])+str(a[1])+str(a[2])+str(a[3]))
        # return ans        
        
        n.sort()
        ans = []
        se = set()
        for i in range(len(n)-3):
            for j in range(i+1, len(n)-2):
                s = n[i]+n[j]
                k = j+1
                l = len(n)-1
                while(k<l):
                    if s+n[k]+n[l]==t and str(n[i])+str(n[j])+str(n[k])+str(n[l]) not in se :
                        ans.append([n[i], n[j], n[k], n[l]])
                        se.add(str(n[i])+str(n[j])+str(n[k])+str(n[l]))
                    elif s+n[k]+n[l] > t:
                        l -= 1
                    else:
                        k += 1
        return ans
