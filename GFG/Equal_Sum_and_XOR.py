# https://practice.geeksforgeeks.org/problems/equal-sum-and-xor/1

"""
Given a positive integer N, Your task is to complete the function countValues which returns an integer denoting the count of all positive integers i such that
0 <= i <= n and n+i = n^i where ^ denotes a XOR operation.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N.

Output:
For each test case in a new line output will be the count of such positive integers.

Constraints:
1<=T<=100
1<=N<=1000

Example(To be used only for expected output):
Input
2
7
12
Output
1
4

Explanation:
For first test case
7^i = 7+i holds only for only for i = 0
7+0 = 7^0 = 7
For second test case
12^i = 12+i hold only for i = 0, 1, 2, 3
for i=0, 12+0 = 12^0 = 10
for i=1, 12+1 = 12^1 = 13
for i=2, 12+2 = 12^2 = 14
for i=3, 12+3 = 12^3 = 15
"""

def countValues(n):
    # Code here

    b = bin(n).replace('0b','')
    tp = [1,2,4,8,16,32,64,128,256,512,1024]
    c = 0
    # print(b)
    for i in str(b):
        if i == '0':
            c += 1
    return tp[c]
