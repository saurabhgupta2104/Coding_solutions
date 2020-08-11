# https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1

"""
You are given a linked list of N nodes. The task is to remove the loop from the linked list, if present. 

Note: C is the position of the node to which the last node is connected. If it is 0 then no loop.

Example 1:

Input:
N = 3
value[] = {1,3,4}
C = 2
Output: 1
Explanation: In the first test case
N = 3.The linked list with nodes
N = 3 is given. Here, x = 2 which
means last node is connected with xth
node of linked list. Therefore, there
exists a loop. 

Example 2:
Input:
N = 4
value[] = {1,8,3,4}
C = 0
Output: 1
Explanation: N = 4 and x = 0, which
means lastNode->next = NULL, thus
the Linked list does not contains
any loop.
Your Task:
Your task is to complete the function removeLoop(). The only argument of the function is head pointer of the linked list. Simply remove the loop in the list (if present) without disconnecting any nodes from the list. The driver code will print 1 if your code is correct.

Expected time complexity : O(n)

Expected auxiliary space : O(1)
"""

def removeLoop(head):
    # code here
    # remove the loop without losing any nodes

    f = head
    s = head
    p = head
    while(1):
        p = s
        if f is None or f.next is None:
            return
        f = f.next.next
        s = s.next
        if f == s:
            break
    # print("common ", s.data)
    s = head
    
    while(s!=f):
        p = f
        s = s.next
        f = f.next
        if s == f:
            break
    # print(p.data)
    p.next = None
