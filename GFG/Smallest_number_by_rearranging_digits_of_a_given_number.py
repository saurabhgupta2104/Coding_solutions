# https://practice.geeksforgeeks.org/problems/smallest-number-by-rearranging-digits-of-a-given-number/0

"""
Find the Smallest number (Not leading Zeros) which can be obtained by rearranging the digits of given number.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains the number N.

Output:
Print the smallest number which can be made by rearranging the digits of the given number.

Constraints:
1 <= T <= 100
1 <= N <= 101000

Example:
Input:
2
846903
55010
Output:
304689
10055
"""

#code
for _ in range(int(input())):
    n = input()
    l = []
    for i in n:
        l.append(i)
    l.sort()
    
    i = 0
    while(l[i]<'1'):
        i += 1
    l[0], l[i] = l[i], l[0]
    s = ''
    s = s.join(l)
    print(s)
