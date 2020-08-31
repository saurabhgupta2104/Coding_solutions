# https://practice.geeksforgeeks.org/problems/minimum-platforms/0

"""
Given arrival and departure times of all trains that reach a railway station. Your task is to find the minimum number of platforms required for the railway station so that no train waits.

Note: Consider that all the trains arrive on the same day and leave on the same day. Also, arrival and departure times will not be same for a train, but we can have arrival time of one train equal to departure of the other. In such cases, we need different platforms, i.e at any given instance of time, same platform can not be used for both departure of a train and arrival of another.

Input:
The first line of input contains T, the number of test cases. For each test case, first line will contain an integer N, the number of trains. Next two lines will consist of N space separated time intervals denoting arrival and departure times respectively.
Note: Time intervals are in the 24-hour format(hhmm),  of the for HHMM , where the first two charcters represent hour (between 00 to 23 ) and last two characters represent minutes (between 00 to 59).

Output:
For each test case, print the minimum number of platforms required for the trains to arrive and depart safely.

Constraints:
1 <= T <= 100
1 <= N <= 1000
1 <= A[i] < D[i] <= 2359

Example:
Input:
2
6 
0900  0940 0950  1100 1500 1800
0910 1200 1120 1130 1900 2000
3
0900 1100 1235
1000 1200 1240 

Output:
3
1
"""

#code

for _ in range(int(input())):
    n = int(input())
    u = list(map(int, input().strip().split()))
    d = list(map(int, input().strip().split()))
    l = []
    for i in range(n):
        l.append([u[i], 0])
        l.append([d[i], 1])
        
    l.sort()
    mc = 0
    c = 0
    for i in range(len(l)):
        if l[i][1] == 0:
            c += 1
        else:
            c -= 1
        mc = max(mc, c)
    print(mc)
