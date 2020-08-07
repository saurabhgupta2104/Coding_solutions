# https://practice.geeksforgeeks.org/problems/subset-sum-problem/0

"""
Given a set of numbers, check whether it can be partitioned into two subsets such that the sum of elements in both subsets is same or not.

Input:
The first line contains an integer 'T' denoting the total number of test cases. Each test case constitutes of two lines. First line contains 'N', representing the number of elements in the set and the second line contains the elements of the set.

Output:
Print YES if the given set can be partioned into two subsets such that the sum of elements in both subsets is equal, else print NO.

Constraints:
1 <= T <= 100
1 <= N <= 100
0 <= arr[i] <= 1000

Example:
Input:
2
4
1 5 11 5
3
1 3 5 

Output:
YES
NO

Explanation:
Testcase 1: There exists two subsets such that {1, 5, 5} and {11}.
"""

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().strip().split()))
    
    if sum(l) % 2 == 1:
        print("NO")
        continue
    t = sum(l)//2
    p = set()
    m = set()
    found  = True
    for i in range(n):
        
        if found and p != None:
            for j in p:
                if j+l[i] == t:
                    found = False
                    break
                elif j+l[i] < t:
                    m.add(j+l[i])
            p.add(l[i])
            p.update(m)
            # print(p)
    if found:
        print("NO")
    else:
        print("YES")
