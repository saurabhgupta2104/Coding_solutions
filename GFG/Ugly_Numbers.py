# https://practice.geeksforgeeks.org/problems/ugly-numbers/0

"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included. Write a program to find Nth Ugly Number.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. For each testcase there is one line of input that contains the number N.

Output:
Print the Nth Ugly Number.

Constraints:
1 ≤ T ≤ 104
1 ≤ N ≤ 104

Example:
Input:
2
10
4
Output:
12
4
"""

#code
for t in range(int(input())):
    n = int(input())
    ugly = []
    if t == 0:
        # ugly = [0]*10000
        
        ugly.append(1)
        i2 = i3 = i5 = 0
        nm2 = 2
        nm3 = 3
        nm5 = 5
        a = 0
        for z in range(1, 10000):
            ugly.append(min(nm2, nm3, nm5))
            if ugly[z] == ugly[i2]*2:
                i2 += 1
                nm2 = ugly[i2]*2
            if ugly[z] == ugly[i3]*3:
                i3 += 1
                nm3 = ugly[i3]*3
            if ugly[z] == ugly[i5]*5:
                i5 += 1
                nm5 = ugly[i5]*5
        a = list(ugly)
    print(a[n-1])
