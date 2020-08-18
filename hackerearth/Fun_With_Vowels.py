# https://www.hackerearth.com/ja/problem/algorithm/fun-with-vowels/description/

"""
A subsequence is a sequence of letters in a string in order, but with any number of character removed.

For example, 3 letter subsequences of abcd are abc, abd, acd and bcd. Vowels are letters in the string aeiou.

Given a string, determine the length of the longest subsequence that contains all the vowels in order.

For example, the string aeeiiouu contains all the vowels in order. The string aeeiiaou does not because of the ‘a’ at position 5, (0 based indexing). The first string is the longest subsequence of the second string that contains all vowels in order.

Constraints:

5 <  |s|  < 5 x 105

Each character of the string s = {a,e,i,o,u}

Input:

Single line contain a string S.

Output:

Print a single integer which is the length of the longest subsequence that contains all the vowels in order.

SAMPLE INPUT 
aeiaaioooaauuaeiu
SAMPLE OUTPUT 
10
Explanation
a e i a a i o o o a a u u a e i u
"""

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

s = input()
# dp = [0]*len(s)
a = 0
e = 0
i = 0
o = 0
u = 0
for j in range(len(s)):
    if s[j] == 'a':
        a += 1
        # dp[j] = a    
    elif s[j] == 'e':
        e = max(e+1, a+1)
        # dp[j] = e
    elif s[j] == 'i':
        i = max(i+1, e+1)
        # dp[j] = i
    elif s[j] == 'o':
        o = max(o+1, i+1)
        # dp[j] = o
    elif s[j] == 'u':
        u = max(u+1, o+1)
        # dp[j] = u
# x = []
# for z in s:
#     x.append(z)
# print(*x)
# print(*dp)
print(u)
        
