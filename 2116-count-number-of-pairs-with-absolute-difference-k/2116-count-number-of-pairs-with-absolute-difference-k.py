class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hashDict = defaultdict(int)
        
        count = 0
        for val in nums:
            Needed = val-k
            Needed2 = val+k
            print(Needed)
            if Needed in hashDict:
                count+=hashDict[Needed]
            if Needed!=Needed2:
                if Needed2 in hashDict:
                    count+=hashDict[Needed2]
            hashDict[val]+=1
        return count
        