# https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1

"""
You are given N elements and your task is to Implement a Stack in which you can get minimum element in O(1) time.

Example 1:

Input:
push(2)
push(3)
pop()
getMin()
push(1)
getMin()
Output: 3 2 1
Explanation: In the first test case for
query 
push(2)  the stack will be {2}
push(3)  the stack will be {2 3}
pop()    poped element will be 3 the
         stack will be {2}
getMin() min element will be 2 
push(1)  the stack will be {2 1}
getMin() min element will be 1
Your Task:
You are required to complete the three methods push() which take one argument an integer 'x' to be pushed into the stack, pop() which returns a integer poped out from the stack and getMin() which returns the min element from the stack. (-1 will be returned if for pop() and getMin() the stack is empty.)

Expected Time Complexity : O(1) for all the 3 methods.
Expected Auixilliary Space : O(1) for all the 3 methods.

Constraints:
1 <= Number of queries <= 100
1 <= values of the stack <= 100
"""

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        #CODE HERE
        if not self.s:
            self.s.append(x)
            self.minEle = x
        elif self.minEle<=x:
            self.s.append(x)
        else:
            self.s.append((2*x)- self.minEle)
            self.minEle = x
        
    def pop(self):
        #CODE HERE
        if self.s:
            if self.s[-1] > self.minEle:
                return self.s.pop()
            else:
                a = self.minEle
                self.minEle = (2*self.minEle)-self.s.pop()
                return a
        else:
            return -1

    def getMin(self):
        #CODE HERE
        if self.s:
            return self.minEle
        else:
            return -1
