# https://practice.geeksforgeeks.org/problems/largest-square-formed-in-a-matrix/0

"""
Given a binary matrix, find out the maximum size square sub-matrix with all 1s.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is n and m,n is the number of rows and m is the number of columns.
The second line of each test case contains array C[n][m] in row major form.

Output:

Print maximum size square sub-matrix.

Constraints:

1 ≤ T ≤ 100
1 ≤ n,m ≤ 50
0 ≤ C[n][m] ≤ 1

Example:

Input:
3
5 6
0 1 0 1 0 1 1 0 1 0 1 0 0 1 1 1 1 0 0 0 1 1 1 0 1 1 1 1 1 1
2 2
1 1 1 1
2 2
0 0 0 0

Output:
3
2
0
"""

for _ in range(int(input())):
    n, m = map(int, input().strip().split())
    l = list(map(int, input().strip().split()))
    grid = []
    start = 0
    for i in range(m, len(l)+1, m):
        grid.append(list(l[start:i]))
        start = i
    maxarea = 0
    if m == 1 or n == 1:
        flag = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    flag = True
                    break
            if flag:
                break
        if flag:
            print(1)
        else:
            print(0)
        continue
                    
    for i in range(1, n):
        for j in range(1,m):
            if grid[i][j] == 1 :
                grid[i][j] += min(grid[i-1][j-1], grid[i-1][j], grid[i][j-1])
                maxarea = max(grid[i][j], maxarea)
        # print(grid[i])
    print(maxarea)
