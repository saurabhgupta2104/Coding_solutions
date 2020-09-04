# https://practice.geeksforgeeks.org/problems/shortest-common-supersequence/0

"""
Given two strings str1 and str2, find the length of the smallest string which has both, str1 and str2 as its sub-sequences.
Note: str1 and str2 can have both uppercase and lowercase letters.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains two space-separated strings.

Output:
For each testcase, in a new line, output the length of the required string.

Expected Time Complexity: O(Length(str1) * Length(str2)).
Expected Auxiliary Space: O(Length(str1) * Length(str2)).

Constraints:
1 <= T <= 100
1<= |str1|, |str2| <= 100

Example:
Input:
2
abcd xycd
efgh jghi
Output:
6
6
"""

#code

for _ in range(int(input())):
    x, y = map(str, input().strip().split())
    
    ans = []
    ans.append(list(range(len(x)+1)))
    for i in range(1,len(y)+1):
        ans.append([i] + [0]*len(x))
    # print(ans)
    for i in range(1, len(y)+1):
        for j in range(1, len(x)+1):
            if x[j-1] == y[i-1]:
                ans[i][j] = ans[i-1][j-1] + 1
            else:
                ans[i][j] = min(ans[i-1][j]+1, ans[i][j-1]+1)
    print(ans[-1][-1])
