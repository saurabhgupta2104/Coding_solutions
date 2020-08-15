# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:




Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""

class Solution:
    def jobScheduling(self, st: List[int], et: List[int], p: List[int]) -> int:        
        l = []
        d = {}
        for i in range(len(st)):
            l.append((st[i], 0))
            l.append((et[i], 1))
            if et[i] not in d:
                d[et[i]] = [[],[]]
            d[et[i]][0].append(st[i])
            d[et[i]][1].append(p[i])            
        l = sorted(l)
        dp = [0]*len(l)
        dpd = {l[0][0]:0}
        for i in range(1, len(l)):
            if l[i][0] not in dpd:
                dpd[l[i][0]] = 0
            if l[i][1] == 1:
                for j in range(len(d[l[i][0]][1])):
                    dp[i] = max(dp[i], d[l[i][0]][1][j]+ dpd[d[l[i][0]][0][j]])
            else:
                dp[i] = dp[i-1]
            dp[i] = max(dp[i], dp[i-1])
            dpd[l[i][0]] = max(dpd[l[i][0]], dp[i])
        return dp[-1]
