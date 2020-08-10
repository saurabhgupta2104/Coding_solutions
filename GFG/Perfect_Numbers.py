# https://practice.geeksforgeeks.org/problems/perfect-numbers/0

"""
Given a number N, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number.

Input:
First line consists of T test cases. Then T test cases follow .Each test case consists of a number N.

Output:
For each testcase, in a new line, output in a single line 1 if a number is a perfect number else print 0.

Constraints:
1 <= T <= 300
1 <= N <= 1018

Example:
Input:
2
6
21
Output:
1
0

"""
#code
for _ in range(int(input())):
    n = int(input())
    s = 1
    i = 2
    while(i*i < n):
        if n%i == 0:
            s += i
            s += n//i
        i += i
    if i*i == n:
        s += i
    if s == n:
        print(1)
    else:
        print(0)
        
