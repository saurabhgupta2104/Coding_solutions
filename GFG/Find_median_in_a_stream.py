# https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0

"""
Given an input stream of N integers. The task is to insert these numbers into a new stream and find the median of the stream formed by each insertion of X to the new stream.

Input:
The first line of input contains an integer N denoting the number of elements in the stream. Then the next N lines contains integer x denoting the number to be inserted into the stream.
Output:
For each element added to the stream print the floor of the new median in a new line.
 
Constraints:
1 <= N <= 106
1 <= x <= 106
 
Example:
Input:
4
5
15
1 
3
Output:
5
10
5
4
 
Explanation:
Testcase 1:
Flow in stream : 5, 15, 1, 3
5 goes to stream --> median 5 (5)
15 goes to stream --> median 10 (5, 15)
1 goes to stream --> median 5 (5, 15, 1)
3 goes to stream --> median 4 (5, 15, 1, 3)
"""

import heapq

l = []
r = []
heapq.heapify(l)
heapq.heapify(r)
ans = []
for i in range(int(input())):
    n = int(input())
    heapq.heappush(l, -1*n )
    if r and -1*l[0]>r[0]:
        a = heapq.heappop(l)
        b = heapq.heappop(r)
        heapq.heappush(l, -1*b)
        heapq.heappush(r, -1*a)
    
    if i%2 == 0:
        print(-1*l[0])
    else:
        if len(l)>len(r):
            a = heapq.heappop(l)
            heapq.heappush(r, -1*a )
        print(((-1*l[0])+r[0])//2)
    # print(l, r)
    
l.clear()
r.clear()
