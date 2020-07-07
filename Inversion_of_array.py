"""
Given an array of positive integers. The task is to find inversion count of array.

Inversion Count : For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, the size of array. The second line of each test case contains N elements.

Output:
Print the inversion count of array.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
1 ≤ C ≤ 1018

Example:
Input:
1
5
2 4 1 3 5

Output:
3

Explanation:
Testcase 1: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
"""

def travel(l):
    # print(l)
    if len(l) <= 1:
        return l
    else:
        # print(l[:len(l)//2], l[len(l)//2:])
        m = travel(l[:len(l)//2])
        r = travel(l[len(l)//2:])

    i = 0
    j = 0
    t = []
    # print('came back', m, r)
    while(i<len(m) and j<len(r)):
        # print('m[i], r[j] ', m[i], r[j])
        if m[i] > r[j]:
            count[0] += len(m)-i
            t.append(r[j])
            j += 1
        else:
            t.append(m[i])
            i += 1
            
            
    if i<len(m):
        t.extend(m[i:])
    if j<len(r):
        t.extend(r[j:])
    # print('t = ',t )
    return t
            
count = [0]
for _ in range(int(input())):
    count[0] = 0
    n = int(input())
    lis = list(map(int, input().strip().split()))
    if n == 1:
        print(0)
        continue
    travel(lis)
    print(count[0])
