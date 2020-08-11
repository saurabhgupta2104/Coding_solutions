# https://practice.geeksforgeeks.org/problems/length-of-the-longest-substring/0

"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substrings without repeating characters for “ABDEFGABEF” are “BDEFGA” and “DEFGAB”, with length 6.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is str.

Output:

Print the length of longest substring.

Constraints:

1 ≤ T ≤ 20
1 ≤ str ≤ 50

Example:

Input:
2
geeksforgeeks
qwertqwer

Output:
7
5
"""

#code

for _ in range(int(input())):
    s = input()
    d = {}
    ind = {}
    mc = 0
    count = 0
    frm = 0
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        elif ind[s[i]] >= frm:
            frm = ind[s[i]]
            count = i-frm-1
        ind[s[i]] = i
        count += 1
        mc = max(mc, count)
    print(mc)
                
    
