# https://practice.geeksforgeeks.org/problems/find-the-maximum-number-of-handshakes/0

"""
There are N persons in a room. Find the maximum number of Handshakes possible. Given the fact that any two persons shake hand exactly once.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains the integer N denoting the number of persons in the room.

Output:
Print the total number of handshakes for between n people. Print the answer for each test case ina new line.

Constraints:
1 <= T <= 100
1 <= N <= 109

Example:
Input:
2
2
10
Output:
1
45
"""

for _ in range(int(input())):
    n = int(input())
    print((n*(n-1))//2)
