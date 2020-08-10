# https://practice.geeksforgeeks.org/problems/return-two-prime-numbers/0

"""
Given an even number (greater than 2), return two prime numbers whose sum will be equal to given number. There are several combinations possible. Print only first such pair. 

NOTE: A solution will always exist, read Goldbach’s conjecture. Also, solve the problem in linear time complexity, i.e., O(n).

Input:
The first line contains T, the number of test cases. The following T lines consist of a number each, for which we'll find two prime numbers.

Note: The number would always be an even number.

Output:
For every test case print two prime numbers space separated, such that the smaller number appears first. Answer for each test case must be in a new line.

Constraints:
1 ≤ T ≤ 70
2 < N ≤ 10000

Example:
Input:
5
74
1024
66 
8
9990

Output:
3 71
3 1021
5 61
3 5
17 9973
"""

#code
l = [True]*10001
p = []
for i in range(2, 100):
    if l[i] == True:
        p.append(i)
        j = i
        while(j +i < 10001):
            j += i
            l[j] = False
for i in range(100, len(l)):
    if l[i] == True:
        p.append(i)

for _ in range(int(input())):
    n = int(input())
    j = len(p)-1
    i = 1
    while(j > i):
        if p[i]+p[j] == n:
            break
        if p[i]+p[j] > n: 
            j -= 1
        else:
            i += 1
    print(p[i], p[j])
