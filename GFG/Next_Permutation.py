# https://practice.geeksforgeeks.org/problems/next-permutation/0

"""
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers. If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.

For example:
1,2,3 → 1,3,2
3,2,1 → 1,2,3

Input:
The first line contains an integer T, depicting total number of test cases. Then following T lines contains an integer N depicting the size of array and next line followed by the value of array.

Output:
Print the array of next permutation in a separate line.

Constraints:
1 ≤ T ≤ 40
1 ≤ N ≤ 100
0 ≤ A[i] ≤ 100

Example:
Input:
1
6
1 2 3 6 5 4

Output:
1 2 4 3 5 6
"""

#code

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().strip().split()))
    i = None
    flag = True
    for i in range(n-2, -1, -1):
        if l[i]<l[i+1]:
            flag = False
            break
    if flag:
        print(*l[::-1])
        continue
    j = 0
    for j in range(n-1, i,-1):
        if l[j]>l[i] :
            break
    l[i], l[j] = l[j], l[i]
    a = l[i+1:]
    a.sort()
    l[i+1:] = a
    print(*l)
                        
