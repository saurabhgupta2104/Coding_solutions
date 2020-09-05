# https://practice.geeksforgeeks.org/problems/count-number-of-hops/0

"""
A frog jumps either 1, 2 or 3 steps to go to top. In how many ways can it reach the top.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains one line of input N denoting the total number of steps.

Output:
For each testcase, in a new line, print the number of ways to reach the top.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 50

Example:
Input:
2
1
5
Output:
1
13
"""

#code
l = [1, 2, 4]
s = 3
j = 0
for i in range(2, 51):
    l.append(sum(l[j:i+1]))
    j+=1
for _ in range(int(input())):
    n = int(input())
   
    print(l[n-1])
