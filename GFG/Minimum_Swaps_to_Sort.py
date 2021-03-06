#  https://practice.geeksforgeeks.org/problems/minimum-swaps/1


"""
Given an array of integers. Find the minimum number of swaps required to sort the array in non-decreasing order.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the no of element of the array A[ ]. In the next line are N space separated values of the array A[ ] .

Output:
For each test case in a new line output will be an integer denoting  minimum umber of swaps that are  required to sort the array.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[] <= 106

User Task:
You don't need to read input or print anything. Your task is to complete the function minSwaps() which takes the array arr[] and its size N as inputs and returns an integer denoting the minimum number of swaps required to sort the array. If the array is already sorted, return 0. 

Expected Time Complexity: O(NlogN).
Expected Auxiliary Space: O(N).

Example(To be used only for expected output):
Input:
2
4
4 3 2 1
5
1 5 4 3 2

Output:
2
2

Explanation:
Test Case 1: We need two swaps, swap 1 with 4 and 3 with 2 to make it sorted.
Test Case 2: We need two swaps, swap 2 with 5 and 3 with 4 to make it sorted.

"""


def minSwaps(arr, n):
    import copy
    # Code here
    if n == 1:
        return 0
    slis = copy.copy(arr)
    slis.sort()
    count = 0
    v = set()
    d = {}
    for i in range(n):
        d[slis[i]] = i
        if arr[i] == slis[i]:
            v.add(i)
    
    for ind in range(n):
        if ind in v:
            continue
        c = -1
        while(1):
            if ind not in v:
                v.add(ind)
                ind = d[arr[ind]]
                count += 1
            else:
                break
            
        count += c
    return count
