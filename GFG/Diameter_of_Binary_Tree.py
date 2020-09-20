# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1

"""
Given a Binary Tree, find diameter of it.
The diameter of a tree is the number of nodes on the longest path between two leaves in the tree. The diagram below shows two trees each with diameter nine, the leaves that form the ends of a longest path are shaded (note that there is more than one path in each tree of length nine, but no path longer than nine nodes).



Example 1:

Input:
       1
     /  \
    2    3
Output: 3
Example 2:

Input:
         10
        /   \
      20    30
    /   \ 
   40   60
Output: 4
Your Task:
You need to complete the function diameter() that takes node as parameter and returns the diameter.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= Number of nodes <= 10000
1 <= Data of a node <= 1000
"""

def travel(r, w):
    if r is None:
        return w
    l = travel(r.left, w)
    ri = travel(r.right, w)
    # print(r.data, l, ri)
    ans[0] = max(ans[0], l+ri+1)
    return max(l, ri)+1
    
# your task is to complete this function
# function should return the diameter of the tree
ans= [0]
def diameter(r):
    # Code here
    l = 0
    if r is not None:
        l = travel(r, 0)
    else:
        return 0
    # print("l = ",l)
    x = ans[0]
    ans[0] = 0
    return x
