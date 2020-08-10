# https://practice.geeksforgeeks.org/problems/ncr/0/

"""
Find nCr for given n and r.

Input:
First line contains number of test cases T. T testcases follow. Each testcase contains 1 line of input containing 2 integers n and r separated by a space.

Output:
For each testcase, in a new line, find the nCr. Modulus your output to 109+7.

Constraints:
1 <= T <= 50
1 <= n <= 103
1 <= r <= 800

Example:
Input:
2
3 2
4 2
Output:
3
6
"""

#code

for _ in range(int(input())):
    n, r = map(int, input().strip().split())
    if r > n:
        print(0)
        continue
    a = 1
    j = 1
    for i in range(n, max(r, n-r), -1):
        a = (a*i)
        a = (a//j)
        j += 1
    print(a%1000000007)
    
