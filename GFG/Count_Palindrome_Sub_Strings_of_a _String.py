# https://practice.geeksforgeeks.org/problems/count-palindrome-sub-strings-of-a-string/0

"""
Given a string, the task is to count all palindromic sub-strings present in it.

Input:

The first line of input will contain no of test cases T . Then T test cases follow . Each test case contains 2 lines. The first line of each test case contains an integer N denoting the length of the string, next line of test case contains the string


Output:

For each test case output a single line depecting the number of palindromic substrings present.


Constraints:

1<=T<=100
2<=N<=500


Example:

Input

2
5
abaab
7
abbaeae

Output

3
4

Explanation:

Test Case 1
Input : str = "abaab"
Output: 3
All palindrome substring are : "aba" , "aa" , "baab"

Test Case 2
Input : str = "abbaeae"
Output: 4
All palindrome substring are : "bb" , "abba" ,"aea","eae"
"""

def travel(j, n, s):
    count = 0
    start = j
    i = j
    i -= 1
    j += 1
    
    while(i>-1 and j<n):
        if s[i] == s[j]:
            # print(s[i:j+1])
            count += 1
            i -= 1
            j += 1
        else:
            break
    
    if (start+1 < n) and s[start] == s[start+1]:
        i = start
        j = start + 1
        while(i>-1 and j<n):
            if s[i] == s[j]:
                # print(s[i:j+1])
                count += 1
                i -= 1
                j += 1
            else:
                break
    
    return count
        
for _ in range(int(input())):
    n = int(input())
    s = input()
    count = 0
    for i in range(n):
        count += travel(i, n, s)
    print(count)
