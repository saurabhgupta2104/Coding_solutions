# https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1

"""
You are in a party of N people, where only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. Your task is to find the stranger (celebrity) in party.

Example 1:

Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0}, 
         {0 1 0}}
Output: 1
Explanation: The matrix will look like
0 1 0 
0 0 0
0 1 0
Here,  the celebrity is the person with
index 1 ie id 1 
Example 2:

Input:
N = 2
M[][] = {{0 1},
         {1 0}}
Output: -1
Explanation: The matrix will look like
0 1
1 0
Here, there is no such person who is a
celebrity (a celebrity should know no
one).
Your Task:
You will be given a square matrix M[][] where if an element of row i and column j  is set to 1 it means ith person knows jth person. You need to complete the function getId() which finds the id of the celebrity if present else return -1. The function getId() takes two arguments, the square matrix M and its size N.

Note: 
M[i][i] will be equal to zero always.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
2 <= N <= 501
0 <= M[][] <= 1
"""

You are in a party of N people, where only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. Your task is to find the stranger (celebrity) in party.

Example 1:

Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0}, 
         {0 1 0}}
Output: 1
Explanation: The matrix will look like
0 1 0 
0 0 0
0 1 0
Here,  the celebrity is the person with
index 1 ie id 1 
Example 2:

Input:
N = 2
M[][] = {{0 1},
         {1 0}}
Output: -1
Explanation: The matrix will look like
0 1
1 0
Here, there is no such person who is a
celebrity (a celebrity should know no
one).
Your Task:
You will be given a square matrix M[][] where if an element of row i and column j  is set to 1 it means ith person knows jth person. You need to complete the function getId() which finds the id of the celebrity if present else return -1. The function getId() takes two arguments, the square matrix M and its size N.

Note: 
M[i][i] will be equal to zero always.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
2 <= N <= 501
0 <= M[][] <= 1
