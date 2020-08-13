# https://practice.geeksforgeeks.org/problems/path-in-matrix/0/

"""
Given a N X N  matrix Matrix[N][N] of positive integers.  There are only three possible moves from a cell Matrix[r][c].

1. Matrix[r+1][c]

2. Matrix[r+1][c-1]

3. Matrix[r+1][c+1]

Starting from any column in row 0, return the largest sum of any of the paths up to row N-1.

Input:
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the order of matrix. Next line contains N*N integers denoting the elements of the matrix in row-major form.

Output:
Output the largest sum of any of the paths starting from any cell of row 0 to any cell of row N-1. Print the output of each test case in a new line.

Constraints:
1<=T<=20
2<=N<=20
1<=Matrix[i][j]<=1000 (for all 1<=i<=N && 1<=j<=N)

Example:

Input:
1
2
348 391 618 193

Output:
1009

Explanation: In the sample test case, the path leading to maximum possible sum is 391->618.  (391 + 618 = 1009)
"""

#code
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().strip().split()))
    j = 0
    g = []
    for i in range(n,n*n+1,n):
        x = l[j:i]
        g.append(x)
        j = i
    if n == 1:
        print(g[0][0])
        continue
    
    for i in range(n-2, -1, -1):
        for j in range(n):
            if j == 0:
                g[i][j] += max(g[i+1][j], g[i+1][j+1])
            elif j == n-1:
                g[i][j] += max(g[i+1][j-1], g[i+1][j])
            else:
                g[i][j] += max(g[i+1][j-1], g[i+1][j], g[i+1][j+1])

    print(max(g[0]))
                
