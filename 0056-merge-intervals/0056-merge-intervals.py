class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        n = len(intervals)
        for i in range(n):
            start = intervals[i][0] 
            end = intervals[i][1]       
            if ans and end<=ans[-1][1]:
                continue
            j = i+1
            while j<n and intervals[j][0]<=end:
                end = max(end,intervals[j][1])
                j+=1
            ans.append([start,end])
        return ans
               