# https://practice.geeksforgeeks.org/problems/dearrangement-of-balls/0

"""
You are given N balls numbered from 1 to N and there are N baskets numbered from 1 to N in front of you, the ‘i’th basket is meant for the ‘i’th ball. The task is to calculate the number of ways in which none of the balls goes into their respective basket.

Input: The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of a single line containing an integer N.

Output: Corresponding to each test case, print the desired output in a new line. Since the answer can be large, print it modulo 109 + 7.

Constraints :               
1 ≤ T ≤ 100
1 ≤ N ≤ 105

Examples
Input :
2
2
3

Output :
1
2

Explanation : In Second test case there are two ways in which no ball goes into respective basket.
1. Ball 1 will go in basket 2 , ball 2 will go in basket 3 and ball 3 will go into basket 1.
2. Ball 1 will go in basket 3 , ball 2 will go in basket 1 and ball 3 will go into basket 2.
"""

for _ in range(int(input())):
    n = int(input())
    a = 1
    b = 0
    ans = 0
    for i in range(2,n+1):
        ans = (i-1)*(a+b)%(1000000007)
        b, a = ans, b
        
    print((ans)%(1000000007))
