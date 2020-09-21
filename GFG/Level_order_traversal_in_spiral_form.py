# https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1

"""
Complete the function to find spiral order traversal of a tree. For below tree, function should return 1, 2, 3, 4, 5, 6, 7.


 
 

Example 1:

Input:
      1
    /   \
   3     2
Output:1 3 2

Example 2:

Input:
           10
         /     \
        20     30
      /    \
    40     60
Output: 10 20 30 60 40 
Your Task:
The task is to complete the function findSpiral() which returns the elements in spiral form of level order traversal as a list. The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
0 <= Number of nodes <= 105
1 <= Data of a node <= 105
"""

import copy
def findSpiral(r):
    if r is None:
        return []
    # Code here
    ans = []
    x = [r]
    ans.append(r.data)
    z = 0
    while(x):
        a = []
        for i in x:
            if i.left is not None:
                a.append(i.left)
            if i.right is not None:
                a.append(i.right)
        x = copy.copy(a)
        if z%2 == 1:
            a = a[::-1]
        for i in a:
            ans.append(i.data)
        
        z += 1
        a = []
    return ans
