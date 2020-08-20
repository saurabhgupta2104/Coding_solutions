# 

"""
Given a pattern as below and an integer n your task is to decode it and print nth row of it. The pattern follows as :
1
11
21
1211
111221
............

Input:
The first line of input is the number of test cases .  Then T test cases follow . The first line of each test case is an integer N.

Output:
For each test case print the required nth row of the pattern.

Expected Time Complexity : O(N2)
Expected Auxilliary Space : O(1)

Constraints:
1<=T<=20
1<=N<=20

Example:
Input:
2
2
3
Output:
11
21
"""
#code

for _ in range(int(input())):
    n = int(input())
    a = '11'
    if n == 1:
        print(1)
        continue
    
    for i in range(n-2):
        x = ''
        c = 1
        for j in range(1, len(a)):

            if a[j] == a[j-1]:
                c += 1
            else:
                x += str(c)
                x += str(a[j-1])
                c = 1

            if j == len(a)-1:
                if a[j] == a[j-1]:
                    x += str(c)
                    x += str(a[j])
                else:
                    x += str(c)
                    x += str(a[j])
        a = x
    print(a)
            
        
