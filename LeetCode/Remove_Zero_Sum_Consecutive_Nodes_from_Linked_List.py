# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

"""
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, h: ListNode) -> ListNode:
        l = []
        p = []
        i = 0
        while(h):
            l.append(h.val)
            p.append(h)
            h = h.next
        
        n = len(l)
        t = -1
        start = p[0]
        
        for i in range(n):
            x = None
            z = None
            m = None
            if t<i:
                for j in range(i, n):
                    if j == n-1 or sum(l[i:j+1])==0:
                        if sum(l[i:j+1])==0:
                            # print(i, j)
                            z = i
                            m = j
                            t = j
                        
                if z is not None:
                    if p[z] == start and m==n-1:
                        return None
                    if p[z] == start:
                        start = p[m+1]
                    elif m == n-1:
                        p[z-1].next = None
                    else:
                        p[z-1].next = p[m+1]              
               
        return start
                
            
        
