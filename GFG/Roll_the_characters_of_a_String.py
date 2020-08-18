# https://practice.geeksforgeeks.org/problems/roll-the-characters-of-a-string/0

"""
We are given a string s and an array roll where roll[i] represents rolling first roll[i] characters in string. We need to apply every roll[i] on string and output final string. Rolling means increasing ASCII value of character, like rolling ‘z’ would result in ‘a’, rolling ‘b’ would result in ‘c’, etc.

Input : s = "bca"
        roll[] = {1, 2, 3}         
Output : eeb

Explanation :
arr[0] = 1 means roll first character of string -> cca
arr[1] = 2 means roll first two characters of string -> dda
arr[2] = 3 means roll first three characters of string -> eeb
So final ans is "eeb"
Input:
First line consist of T test cases. First line of every test case consists of N. Second and third line consists of String and Array of N size, respectively.

Output:
Single line output, print the modified String.

Constraints:
1<=T<=100
1<=N<=1000

Example:
Input:
1
3
bca
1 2 3
Output:
eeb
"""

#code
import copy
for _ in range(int(input())):
    n = int(input())
    s = input()
    l = list(map(int, input().strip().split()))
    
    ans = [0]*len(s)
    for i in l:
        ans[i-1]  += 1
    
    u = copy.copy(ans)
    u[-1] = u[-1]%26
    for i in range(len(s)-1, -1, -1):
        if i != len(s)-1:
            u[i] += u[i+1]
        u[i] %= 26
        ans[i] = u[i]
        if ans[i] + ord(s[i]) > ord('z'):
            
            ans[i] = chr(((ord(s[i])+ans[i])%ord('z'))+ ord('a')-1)
        else:
            ans[i] = chr((ord(s[i])+ans[i]))
    f = ''
    print(f.join(ans))
        
