# https://practice.geeksforgeeks.org/problems/longest-common-substring/0

"""
Given two strings X and Y. The task is to find the length of the longest common substring.

Input:
First line of the input contains number of test cases T. Each test case consist of three lines, first of which contains 2 space separated integers N and M denoting the size of string X and Y strings respectively. The next two lines contains the string X and Y.

Output:
For each test case print the length of longest  common substring of the two strings .

Constraints:
1 <= T <= 200
1 <= N, M <= 100

Example:
Input:
2
6 6
ABCDGH
ACDGHR
3 2
ABC
AC

Output:
4
1

Example:
Testcase 1: CDGH is the longest substring present in both of the strings.
"""

#code

for _ in range(int(input())):
    n, m = map(int, input().strip().split())
    x = input()
    y = input()
    
    l = [[0]*(n+1) for i in range(m+1)]
    # print(l)
    ans = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[j-1] == y[i-1]:
                l[i][j] = l[i-1][j-1]+1
                ans = max(ans, l[i][j])
            else:
                l[i][j] = 0
                # l[i][j] = max(l[i-1][j], l[i][j-1])
    print(ans)
