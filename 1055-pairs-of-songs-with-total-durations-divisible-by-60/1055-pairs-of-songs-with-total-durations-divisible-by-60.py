class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pfSum = 0
        pfDict = defaultdict(int)
        count = 0
        for idx in range(len(time)):
            pfSum = time[idx]%60
            Needed = (60 - pfSum)%60
            if Needed in pfDict:
                count+=pfDict[Needed]
            pfDict[pfSum]+=1
        return count


        