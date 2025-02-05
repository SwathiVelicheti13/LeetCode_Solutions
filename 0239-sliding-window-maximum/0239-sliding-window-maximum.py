class Solution:     # please check ranges
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        
        if not nums:
            return []
        
        maxWindowList = []
        queue = deque()  # Stores indices of useful elements in decreasing order

        for idx in range(len(nums)):
            # Remove elements that are out of this window
            if queue and queue[0] < idx - k + 1:
                queue.popleft()
            
            # Remove elements from the back if they are smaller than the current number
            while queue and nums[queue[-1]] <= nums[idx]:
                queue.pop()
            
            queue.append(idx)

            # Append max element of the current window
            if idx >= k - 1:
                maxWindowList.append(nums[queue[0]])  # nums[queue[0]] gives max value
        
        return maxWindowList

        # for num1 in range(0,len(nums)-k+1):
        #     maxVal = nums[num1]
        #     for num2 in range(num1,num1 + k):
        #         maxVal = max(maxVal,nums[num2])

        #     maxWindowList.append(maxVal)
        # return maxWindowList
