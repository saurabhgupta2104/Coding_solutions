# https://leetcode.com/problems/binary-tree-maximum-path-sum/

"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def travel(r):
    if not r:
        return 0
    le = travel(r.left)
    ri = travel(r.right)
    
    m = max(le, ri)
    if m >0:
        r.val += m
    maxans[0] = max(r.val, maxans[0], r.val + min(le, ri))
    return r.val
    


maxans = [-float(inf)]

class Solution:
    def maxPathSum(self, r: TreeNode) -> int:        
        ans = travel(r)
        a = maxans[0]
        maxans[0] = -float('inf')
        return a
            
            
