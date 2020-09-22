# https://leetcode.com/problems/delete-nodes-and-return-forest/

"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def travel(r, d, l, i):
    
    if r is None:
        return l
    if l[i] == [] and r.val not in d:
        l[i].append(r)
    if r.val in d:       
        if r.left is not None:
            l = travel(r.left, d, l+[[]], len(l))
            if r.left.val in d:
                r.left = None
        if r.right is not None:
            l = travel(r.right, d, l+[[]], len(l))
            if r.right.val in d:
                r.right = None
    else:
        if r.left is not None:
            l = travel(r.left, d, l, i)
            if r.left.val in d:
                r.left = None
        if r.right is not None:
            l = travel(r.right, d, l, i)
            if r.right.val in d:
                r.right = None
    return l
    
    
class Solution:
    def delNodes(self, r: TreeNode, de: List[int]) -> List[TreeNode]:
        d = set()
        for i in de:
            d.add(i)
            
        if r is None:
            return []
        l = [[]]
        l = travel(r, d, l, 0)
        ans = []
        
        for i in l:
            if i:
                ans.append(i[0])
        return ans
        
