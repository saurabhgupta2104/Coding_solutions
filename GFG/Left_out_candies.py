# https://practice.geeksforgeeks.org/problems/left-out-candies/0

"""
Given N students sitting in a circle You have to distribute M candies to these students also , ith student takes i candies. if ith student didn't get required candies then he will not take it. you have to distribute the candies starting from 1st student and moving along the circle of students till you cannot distribute to a student. you need to output the left out candies.


Input
The first line of input contains of an integer 'T' denoting number of test cases. Then T test cases follow . The only line of each test case contains two space separated integers N and M .

Output:
For each case print an integer in a new line corresponding to the answer .


CONSTRAINTS:
1<=T<=50
1 ≤ n ≤ 50 
1 ≤ m ≤ 10^4


Example:

Input:

2
4 11
4 12


OUTPUT:
0
1


Explanation:
1. In first test case you first give 1 candy to 1st student, 2 to 2nd , 3 to 3rd , 4 to 4th then again 1 to first and all candies finished with no left out.
2. In second test case you are left out with only one candy
"""


for _ in range(int(input())):
    n, m = map(int, input().strip().split())
    
    req = (n*(n+1))//2
    m = m%req
    if m == 0:
        print(m)
        continue
    for i in range(1, n+1):
        if m < i:
            print(m)
            break
        elif m == i:
            print(0)
            break
        else:
            m -= i
