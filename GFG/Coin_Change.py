# https://practice.geeksforgeeks.org/problems/coin-change/0

"""
Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins. The order of coins doesn’t matter. For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.

Input:
The first line contains an integer 'T' denoting the total number of test cases. In each test cases, the first line contains an integer 'M' denoting the size of array. The second line contains M space-separated integers A1, A2, ..., AN denoting the elements of the array. The third line contains an integer 'N' denoting the cents.

Output:
Print number of possible ways to make change for N cents.

Constraints:
1 ≤ T ≤ 50
1 ≤ N ≤ 300
1 ≤ A[i] ≤ 300

Example:
Input:
2
3
1 2 3
4
4
2 5 3 6
10

Output:
4
5
"""
#code

for _ in range(int(input())):
    m = int(input())
    l = list(map(int, input().strip().split()))
    n = int(input())
    ans = []
    for i in range(m):
        ans.append([1]+[0]*n)
    
    l.sort()
    # print(ans)
    for i in range(l[0], n+1, l[0]):
        # print('i', i)
        ans[0][i] = 1
        
    for i in range(1, m):
        for j in range(n+1):
            if j < l[i]:
                ans[i][j] = ans[i-1][j]
            elif j == l[i]:
                ans[i][j] = ans[i-1][j]+1
            else:
                ans[i][j]  = ans[i-1][j] + ans[i][j-l[i]]
        
    print(ans[-1][-1])
    
