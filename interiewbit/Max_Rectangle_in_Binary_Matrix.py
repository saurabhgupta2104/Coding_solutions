# https://www.interviewbit.com/problems/max-rectangle-in-binary-matrix/

"""
Given a 2D binary matrix filled with 0’s and 1’s, find the largest rectangle containing all ones and return its area.

Bonus if you can solve it in O(n^2) or less.

Example :

A : [  1 1 1
       0 1 1
       1 0 0 
    ]

Output : 4 

As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2)

"""

def maximalRectangle(self, a):
        
        maxarea = 0
        for row in range(len(a)):
            l = []
            for col in range(len(a[0])+1):
                if col<len(a[0]) and row > 0 and a[row][col] > 0:
                    a[row][col] += a[row-1][col]
                area = 0    
                while (col == len(a[0]) or (l and a[row][l[-1] ]>a[row][col])):
                    
                    if l == []:
                        break
                    s = l.pop()
                    if l:
                        area = (col-l[-1]-1)*a[row][s]
                    else:
                        area = col*a[row][s]
                    maxarea = max(area, maxarea)
                    # print(area, l)
                if col<len(a[0]):
                    l.append(col)
            # print(area, l)
        # for i in a:
        #     print(i)
        return maxarea
