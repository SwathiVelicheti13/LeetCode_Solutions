class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime,endTime,profit))
        dp = {}
        start_times = [job[0] for job in intervals]

        def binary_search(target):
            left, right = 0, len(start_times) - 1
            while left <= right:
                mid = (left + right) // 2
                if start_times[mid] >= target:
                    right = mid - 1  # Move left to find the first valid index
                else:
                    left = mid + 1  # Move right to increase start time
            return left

        def jobProfit(ind):
            if ind == len(intervals):
                return 0

            if ind in dp:
                return dp[ind]
            res = jobProfit(ind+1)

            # while loop for next non overlapping interval

            # j = ind+1
            # while j<len(intervals):
            #     if intervals[ind][1]<=intervals[j][0]:
            #         break
            #     j+=1

            # j = bisect_left(start_times, intervals[ind][1])
            
            j = binary_search(intervals[ind][1])
            dp[ind] =  max(res, intervals[ind][2]+jobProfit(j))
            return dp[ind]
        
        return jobProfit(0)