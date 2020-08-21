# https://practice.geeksforgeeks.org/problems/bleak-numbers/0

"""
Given an integer, check whether it is Bleak or not.

A number ‘n’ is called Bleak if it cannot be represented as sum of a positive number x and set bit count in x, i.e., x + countSetBits(x) is not equal to n for any non-negative number x.

Examples :

3 is not Bleak as it can be represented
as 2 + countSetBits(2).

4 is t Bleak as it cannot be represented 
as sum of a number x and countSetBits(x)
for any number x.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of a single line. The first line of each test case contains a single integer N to be checked for Bleak.

Output:
Print "1" or "0" (without quotes) depending on whether the number is Bleak or not.

Constraints:
1 <= T <= 1000
1 <= N <= 10000

Example:
Input:
3
4
167
3

Output:
1
0
0
"""

#code
s = set()
for i in range(10001):
    a = i
    a = bin(i).replace('0b',"")
    c = 0
    # print('a ',a)
    for j in str(a):
        c += int(j)
        # print('c ', c, j)
    s.add(i+c)
# print(s)
for _ in range(int(input())):
    n = int(input())
    if n in s:
        print(0)
    else:
        print(1)
     
