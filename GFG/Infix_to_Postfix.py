# https://practice.geeksforgeeks.org/problems/infix-to-postfix/0

"""
Given an infix expression in the form of a string str. Conver this infix expression to postfix expression.

Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Input:
The first line of input contains an integer T denoting the number of test cases. The next T lines contains an infix expression.The expression contains all characters and ^,*,/,+,-.

Output:
For each testcase, in a new line, output the infix expression to postfix expression.

Constraints:
1 <= T <= 100
1 <= length of str <= 103

Example:
Input:
2
a+b*(c^d-e)^(f+g*h)-i
A*(B+C)/D

Output:
abcd^e-fgh*+^*+i-
ABC+*D/
"""

for _ in range(int(input())):
    infx = input()
    stac = []
    p = ''
    pri = ['^','*','/','+','-']
    for s in range(len(infx)):
        if infx[s] == "(":
            stac.append(infx[s])
        elif infx[s] == ")":
            while(1):
                if stac[-1] == "(":
                    stac.pop(-1)
                    break
                else:
                    p += stac.pop(-1)
        elif infx[s] == "^":
            while (stac and (stac[-1] in pri[:1])):
                if stac[-1] == "(":
                    stac.pop(-1)
                    break
                p += stac.pop(-1)
            stac.append(infx[s])
            
        elif infx[s] == "*" or infx[s] == "/" :
            while (stac and (stac[-1] in pri[:3])):
                if stac[-1] == "(":
                    stac.pop(-1)
                    break
                p += stac.pop(-1)
            stac.append(infx[s])
            
        elif infx[s] == "+" or infx[s] == "-" :
            while (stac and (stac[-1] in pri)):
                if stac[-1] == "(":
                    stac.pop(-1)
                    break
                p += stac.pop(-1)
            stac.append(infx[s])
        else:
            p += str(infx[s])
            
    for s in range(len(stac)-1,-1,-1):
        p += stac[s]
    print(p)
