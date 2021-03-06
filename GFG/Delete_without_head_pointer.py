# https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1

"""
You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes. The task is to delete the node. Pointer/ reference to head node is not given. 
Note: No head reference is given to you.

Example 1:

Input:
N = 2
value[] = {1,2}
node = 1
Output: 2
Explanation: After deleting 1 from the
linked list, we have remaining nodes
as 2.
Example 2:

Input:
N = 4
value[] = {10,20,4,30}
node = 40
Output: 10 4 30
Explanation: After deleting 20 from
the linked list, we have remaining
nodes as 10, 4 and 30.
Your Task:
You only need to complete the function deleteNode that takes reference to the node that needs to be deleted. The printing is done automatically by the driver code.

Expected Time Complexity : O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 <= N <= 103
"""

def deleteNode(curr_node):
    #code here
    c = curr_node
    l = []
    p = None
    while(c.next):
        p = c
        c = c.next
        l.append(c.data)
    if p:
        p.next  = None
    c = curr_node
    for i in l:
        c.data = i
        c = c.next
    
