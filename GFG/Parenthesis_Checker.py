# https://practice.geeksforgeeks.org/problems/parenthesis-checker/0

"""
Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

Input:
The first line of input contains an integer T denoting the number of test cases.  Each test case consists of a string of expression, in a separate line.

Output:
Print 'balanced' without quotes if the pair of parenthesis is balanced else print 'not balanced' in a separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ |s| ≤ 105

Example:
Input:
3
{([])}
()
([]

Output:
balanced
balanced
not balanced
"""

#code

for _ in range(int(input())):
    s = input()
    l = []
    flag = False
    for i in s:
        # print(i, l)
        if i == '[' or i == '{' or i == '(':
            l.append(i)
        elif i == ']':
            if l and l[-1]=='[':
                l.pop()
                continue
            else:
                flag = True
                break
        elif i == '}':
            if l and l[-1]=='{':
                l.pop()
                continue
            else:
                flag = True
                break
            
        elif i == ')':
            
            if l and l[-1]=='(':
                l.pop()
                continue
            else:
                flag = True
                break
    if flag or l != []:
        print('not balanced')
    else:
        print('balanced')
