# https://practice.geeksforgeeks.org/problems/interesting-prime-numbers/0

"""
An interesting prime number is a prime number which can be written as a2 + b4 where a and b are positive integers. The smallest interesting prime is 2 = 12 + 14. You will be given N a positive integer, you have to find the number of interesting primes less than or equal to N.
 

Input:
The first line of input contains a single integer T denoting the number of test cases.
Then T test cases follow. The first and only line of each test case consists of N.
 

Output:
Corresponding to each test case, in a new line, print the number of interesting prime numbers below N.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 105
 

Example:
Input
4
3
10
100
1000
Output
1
2
6
28
"""

#code
import math

n = 100000
l = set(range(2,n+1))
for i in range(2, int(math.sqrt(n)+1)):
    if i in l:
        for t in range(2*i,n+1,i):
            if t in l:
                l.remove(t)
# print(len(l),l)

a = set()
for i in range(1, int(math.sqrt(n))+1):
    for j in range(1, int(math.sqrt(math.sqrt(n)))+1):
        num = (i**2)+(j**4)
        if (num)<=n:
            if num in l:
                a.add(num)
        else:
            break
a = list(a)
a.sort()
        
for t in range(int(input())):
    n = int(input())
    count = 0
    for i in a:
        if i<=n:
            count += 1
        else:
            break
    print(count)

        
    
