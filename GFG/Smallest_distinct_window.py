# https://practice.geeksforgeeks.org/problems/smallest-distant-window/0

"""
Given a string 's'. The task is to find the smallest window length that contains all the characters of the given string at least one time.
For eg. A = “aabcbcdbca”, then the result would be 4 as of the smallest window will be “dbca”.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains a string S.

Output:
For each test case in a new line print the length of the smallest such string.

Constraints:
1 <= T <= 100
1 <= |S| <= 105

Example:
Input:
2
aabcbcdbca
aaab

Output:
4
2

Explanation:
Testcase 1: Smallest window size is 4 which is of "dbca" which consists all characters of the string.
"""

for _ in range(int(input())):
    s = input()
    
    i = 0
    j = 0
    n = len(s)
    max_count = [1, 1]
    dic = {}
    dic[s[0]] = 1
    
    while(j<n):
        
        if i == j:
            j += 1
            if j<n:
                dic[s[j]] = dic.get(s[j], 0)+1
        elif s[i] == s[j] or (s[i] in dic and dic[s[i]]>1):
            dic[s[i]] -= 1
            i += 1
        else:
            j += 1
            if j<n:
                dic[s[j]] = dic.get(s[j], 0)+1
        
        if len(dic.keys()) > max_count[1]:
                max_count[0] = j-i+1
                max_count[1] = len(dic.keys())
        elif len(dic.keys()) == max_count[1] and j-i+1 < max_count[0]:
            max_count[0] = j-i+1
        
    print(max_count[0])
