class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        inter1 = []
        inter2 = []
        if len(intervals) == 1:
            return 1
        for x in range(len(intervals)):
            inter1.append(intervals[x][0])
            inter2.append(intervals[x][1])
        inter1.sort()
        inter2.sort()
        i = 1
        j = 0
        
        count = 1
        maxCount = 1
        while i <len(inter1) and j<len(inter2):
            if inter1[i]<inter2[j]:
                count+=1
                i+=1
            elif inter1[i]>inter2[j]:
                count = count-1
                j+=1
            else:
                i+=1
                j+=1
            maxCount = max(maxCount,count)
        return maxCount

        