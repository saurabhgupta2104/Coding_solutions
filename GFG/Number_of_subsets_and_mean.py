# https://practice.geeksforgeeks.org/problems/number-of-subsets-and-mean/0

"""
Let Max be the maximum possible mean of a multiset of values obtained from an array.
Let Min be the minimum possible mean of a multiset of values obtained from the same array. Note that in a multiset values may repeat.The task is to find the number of multisets with mean as Max and the number of multisets with mean as Min. The answer may be too large so output the number of multisets modulo 109+7.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains a positive integer N which denotes the size of the array. In the next line are N space separated positive integers which are the value of array A.

Output:
Corresponding to each test case, in a new line, print two space separated integers which denote the number of multisets with mean as Max and the number of multisets with mean as Min. The output should be done modulo 109+7.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1≤A[i] ≤1000

Example:
Input:
1
5
3 1 2 3 4
Output:
1 1
"""
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().strip().split()))
    ma = -float('inf')
    mi = float('inf')
    mac = 0
    mic = 0
    ansma = 1
    ansmi = 1
    for i in l:
        if i > ma:
            mac = 1
            ma = i
            ansma = 2
        elif ma == i:
            mac += 1
            ansma *= 2
            ansma %= 1000000007
        
        if i<mi:
            mic = 1
            mi = i
            ansmi = 2
        elif mi == i:
            mic += 1
            ansmi *= 2
            ansmi %= 1000000007
    print(ansma-1, ansmi-1)
            
